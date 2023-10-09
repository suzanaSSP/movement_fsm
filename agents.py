import numpy as np
import math

# DEAL WITH NAN ERRORS
class Agent:
    speed = 5
    dt = 0.1
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.c = np.array([self.x, self.y])
        
        self.theta  = np.random.uniform(-np.pi, np.pi) # angular heading
        self.direction = np.array([np.cos(self.theta), np.sin(self.theta)]) # angular velocity
        self.new_positions = None
        
        
        self.group_radius = 5
        self.agents = None
        self.neighbors = None
      
    
    def define_neighbors(self, agents):
        self.agents = agents
        self.neighbors = [agent for agent in agents if math.dist(agent.c, self.c) < 5 and agent is not self]
    
    def update(self):
        self.theta = self.new_positions["Theta"]
        self.direction = self.new_positions["Direction"]
        self.c = self.new_positions["Position"]
        
        self.x = self.c[0]
        self.y = self.c[1]
        
        self.new_positions = None
        
    def calculate_new_position(self):
        attraction = self.calculate_attraction()
        orientaion = self.calculate_orientation()
        repulsion = self.calculate_repulsion()
        u = attraction + orientaion + repulsion
        
        new_theta = 0.5*(np.arctan2(u[1], u[0]) - self.theta)
        new_direction = np.array([np.cos(new_theta), np.sin(new_theta)])
        new_c = (self.speed*self.dt*new_direction) + self.c
        
        self.new_positions = {"Theta": new_theta, "Direction": new_direction, "Position": new_c}
    
    def calculate_attraction(self):
        attraction_factor = [math.dist(agent.c, self.c) for agent in self.neighbors]
        try:
            norm = np.linalg.norm(attraction_factor)
            Ua = attraction_factor/norm
            return Ua
        except RuntimeWarning as e:
            print("Norm is weird")
            
    
    def calculate_orientation(self):
        orientation_factor = sum([agent.direction for agent in self.neighbors])
        
        Uo = (self.direction + orientation_factor) / np.linalg.norm(self.direction + orientation_factor)
        return Uo
    
    def calculate_repulsion(self):
        repulsion_factor = sum([(agent.c - self.c)/(np.linalg.norm(agent.c-self.c)**2) for agent in self.neighbors])
        
        Ur = -1 * repulsion_factor
        return Ur
    
    

    