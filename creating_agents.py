from agents import Agent
import random

min_value = 0
max_value = 100
num_agents = 40


def create_agent(seed):
    random.seed(seed)
    
    agents = [Agent(random.randint(min_value, max_value), random.randint(min_value, max_value)) for i in range(num_agents)]
    
    for agent in agents:
        agent.define_neighbors(agents)
        
    return agents
        
        
def calculate_new_agent_positions(agents):
    for agent in agents:
        agent.calculate_new_position()
        
def update_agents(agents):
    for agent in agents:
        agent.update()
        
def create_x_y_values(agents):   
    return [agent.x for agent in agents], [agent.y for agent in agents]

if __name__ == "__main__":
    agents = create_agent(42)
    calculate_new_agent_positions(agents)