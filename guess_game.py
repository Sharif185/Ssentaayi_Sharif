import random
secret_number = random.randint(1,16)
print("You are welcome to the guessing game")
print("You have only 5 attempts to guess the game")

attempts = 5
scored_mark = 0
while attempts > 0:
    guess = int(input(f"Attempts{6 - attempts} Enter the number: "))
    if guess != secret_number:
        scored_mark -=2
        print("Wrong number! try again, Your mark is:" ,scored_mark)
    else:
        scored_mark +=10
        print("You guessed the number, Your mark is:  ", scored_mark)  
        
        break
    attempts -= 1
    if attempts ==0:
        print(f"The secret number is: {secret_number}")  
        
        
    
    