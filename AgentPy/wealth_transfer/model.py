'''
model.py

'''
# Model design
import agentpy as ap
import numpy as np

# Visualization
import seaborn as sns

import sys
sys.path.append('.')
from gini import gini
from agent import WealthAgent

class WealthModel(ap.Model):
     """ A simple model of random wealth transfers. """

     def setup(self):
          """ Defines how many agents should be created at the beginning of the sim. """
          self.agents = ap.AgentList(self, self.p.agents, WealthAgent)

     def step(self):
          """ Calls all agents during each time-step to perform their wealth_transfer method. """
          self.agents.wealth_transfer()

     def update(self):
          """ Calculates and records the current Gini Coefficient after each time-step. """
          self.record("Gini Coefficient", gini(self.agents.wealth))
     
     def end(self):
          """ Called at the end of the simulation, we record the wealth of each agent. """
          self.agents.record("wealth")

