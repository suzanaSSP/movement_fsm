import matplotlib.pyplot as plt
from creating_agents import *

nt = 500
L = 100
plotRealTime = True
agents = create_agent(42)

def main():
    for i in range(500):
        
        ax, fig = plt.subplots()
        calculate_new_agent_positions(agents)
        update_agents(agents)
        x, y = create_x_y_values(agents)
        
        if plotRealTime or (i == nt-1):
            plt.cla()
            plt.scatter(x, y)
            ax.set(xlim=(0, L), ylim=(0,L))
            ax.set_aspect('equal')
            plt.pause(.1)
            
            plt.show()
            
if __name__ == "__main__":
    main()
        
