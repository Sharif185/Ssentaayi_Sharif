import numpy as np
import matplotlib.pyplot as plt
from time import sleep

class RoadCrossingEnv:
    def __init__(self):
        self.action_space = ['left', 'right', 'forward', 'wait']
        self.reset()
        
    def reset(self):
        self.x_position = 0  # Progress across road (0-10)
        self.y_position = 0  # Lateral position (-2 to 2)
        self.steps = 0
        self.action_history = []
        return (self.x_position, self.y_position)
        
    def step(self, action):
        self.action_history.append(action)
        self.steps += 1
        
        # Movement rules
        if action == 'forward':
            self.x_position += 1
        elif action == 'left':
            self.y_position = max(-2, self.y_position - 1)
        elif action == 'right':
            self.y_position = min(2, self.y_position + 1)
        # 'wait' does not change position
        
        # Calculate reward
        reward = -0.1  # Small penalty per step
        
        # Check for successful crossing
        if self.x_position >= 10:
            # Bonus for using the specified sequence somewhere in the episode
            if any(self.action_history[i:i+3] == ['right', 'left', 'right'] 
                   for i in range(len(self.action_history)-2)):
                reward += 20  # Big bonus for correct sequence
            else:
                reward += 10  # Standard success reward
            return (self.x_position, self.y_position), reward, True, {}
            
        # Check for failure conditions
        if self.steps > 100:  # Timeout
            return (self.x_position, self.y_position), -5, True, {}
        if abs(self.y_position) > 2:  # Out of bounds
            return (self.x_position, self.y_position), -10, True, {}
            
        return (self.x_position, self.y_position), reward, False, {}

    def render(self):
        """Simple text visualization of the agent's position"""
        road_width = 5  # -2 to 2
        print(f"\nStep {self.steps}:")
        print(f"Position: ({self.x_position}, {self.y_position})")
        print("Road:")
        for y in range(-2, 3):
            marker = "A" if y == self.y_position and self.x_position < 10 else "."
            print(f"{'|' if y == 0 else ' '} {marker} {'|' if y == 0 else ' '}", end="")
        print("\n" + "-"*15)

class QLearningAgent:
    def __init__(self, env):
        self.env = env
        self.q_table = np.zeros((11, 5, len(env.action_space)))  # x:0-10, y:-2to2
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1
        self.training_stats = {'rewards': [], 'successes': []}
        
    def choose_action(self, state):
        x, y = state
        if np.random.random() < self.epsilon:
            return np.random.choice(self.env.action_space)
        else:
            return self.env.action_space[np.argmax(self.q_table[x, y+2])]
            
    def learn(self, state, action, reward, next_state):
        x, y = state
        next_x, next_y = next_state
        action_idx = self.env.action_space.index(action)
        
        current_q = self.q_table[x, y+2, action_idx]
        max_next_q = np.max(self.q_table[next_x, next_y+2])
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[x, y+2, action_idx] = new_q

def train_agent(episodes=1000, show_progress=True):
    env = RoadCrossingEnv()
    agent = QLearningAgent(env)
    
    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        success = False
        
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            total_reward += reward
            
            # Show last few episodes
            if episode >= episodes - 3 and show_progress:
                env.render()
                sleep(0.3)
                
        success = (env.x_position >= 10)
        agent.training_stats['rewards'].append(total_reward)
        agent.training_stats['successes'].append(int(success))
        
        # Epsilon decay
        agent.epsilon = max(0.01, agent.epsilon * 0.995)
        
        if show_progress and episode % 100 == 0:
            print(f"Episode {episode}: Reward {total_reward:.1f}, Success {success}, Epsilon {agent.epsilon:.2f}")
    
    return agent

def plot_training(agent):
    plt.figure(figsize=(12, 4))
    
    # Plot rewards
    plt.subplot(1, 2, 1)
    plt.plot(agent.training_stats['rewards'])
    plt.title("Rewards per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    
    # Plot success rate
    plt.subplot(1, 2, 2)
    success_rate = np.convolve(agent.training_stats['successes'], np.ones(50)/50, mode='valid')
    plt.plot(success_rate)
    plt.title("Success Rate (50-episode moving avg)")
    plt.xlabel("Episode")
    plt.ylabel("Success Rate")
    
    plt.tight_layout()
    plt.show()

# Run the training
agent = train_agent(episodes=1000)

# Show training results
plot_training(agent)

# Run a demo episode
print("\nFinal Demo Episode:")
env = RoadCrossingEnv()
state = env.reset()
done = False
while not done:
    action = agent.choose_action(state)
    next_state, reward, done, _ = env.step(action)
    env.render()
    sleep(0.5)
    state = next_state
print(f"Final reward: {reward}")