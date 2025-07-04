import os
import time
import openai # type: ignore
from telegram import Bot
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import threading
import asyncio

# Load environment variables
load_dotenv()

# Configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize bot
bot = Bot(token=TOKEN)
last_post_date = None  # Initialize global variable

def generate_content(prompt="Create a short post about Uganda"):
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"AI Error: {e}")
        return None

async def post_to_telegram(text):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text)
        print(f"Posted: {text[:50]}...")
        return True
    except Exception as e:
        print(f"Posting Error: {e}")
        return False

async def start(update, context):
    await update.message.reply_text("🇺🇬 Uganda Post Bot\nCommands:\n/post [text]\n/generate [prompt]")

async def post(update, context):
    text = ' '.join(context.args) if context.args else "Default post from Uganda"
    if await post_to_telegram(text):
        await update.message.reply_text("✅ Posted successfully!")
    else:
        await update.message.reply_text("❌ Failed to post")

async def generate(update, context):
    prompt = ' '.join(context.args) if context.args else "Create a short post about Uganda"
    content = generate_content(prompt)
    if content:
        if await post_to_telegram(content):
            await update.message.reply_text(f"✅ Generated post:\n{content}")
        else:
            await update.message.reply_text("❌ Failed to post generated content")
    else:
        await update.message.reply_text("❌ Failed to generate content")

def run_scheduler(application):
    """Run in a separate thread to check time periodically"""
    global last_post_date  # Declare we're using the global variable
    while True:
        now = time.localtime()
        if now.tm_hour == 9 and now.tm_min == 0:
            if last_post_date != now.tm_yday:
                content = generate_content()
                if content:
                    # Use run_coroutine_threadsafe to safely call async function from another thread
                    future = asyncio.run_coroutine_threadsafe(
                        post_to_telegram(content),
                        application.create_task
                    )
                    try:
                        future.result()  # Wait for completion
                        last_post_date = now.tm_yday
                    except Exception as e:
                        print(f"Scheduled post error: {e}")
        time.sleep(30)

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("post", post))
    application.add_handler(CommandHandler("generate", generate))
    
    # Start scheduler in a separate thread
    scheduler_thread = threading.Thread(
        target=run_scheduler,
        args=(application,),
        daemon=True
    )
    scheduler_thread.start()
    
    print("🤖 Sharif Post Bot is running...")
    print(f"Channel ID: {CHAT_ID}")
    print("Auto-posting at 9:00 AM  daily")
    print("Press Ctrl+C to stop")
    
    application.run_polling()

if __name__ == "__main__":
    main()