'''
All model objects (including agents, environments, and the model itself) are 
equipped with the following default attributes:

1. `model` : is the model instance
2. `id` : is a unique identifier number for each object
3. `p` the model's parameters
4. `log` the object's recorded variables
'''

import agentpy as ap

# System files
import sys
sys.path.append('.')

# We are using the custom agent defined in `custom_agent.py`
from custom_agent import MyAgent


class MyModel(ap.Model):

     def setup(self):
          """ Initiate a list of new agents. """
          self.agents = ap.AgentList(self, self.agents, MyAgent)

     def step(self):
          """ Call a method for every agent. """
          self.agents.agent_method()
     
     def update(self):
          """ Record a dynamic variable. """
          self.agents.record("my_attribute")

     def end(self):
          """ Report an evaluation measure. """
          self.report("my_measure", 1)

