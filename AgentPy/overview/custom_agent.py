'''
Agent

Creating a custom agent type

The `Agent.setup()` method is meant to be overwritten
It is called automatically after an agent's creation.
All variables of an agent should be initialized within
this method.

Any other methods can represent actions that the agent will
be able to take during a simulation.
'''
import agentpy as ap

class MyAgent(ap.Agent):
     
     def setup(self):
          """ Initiates all variables of the agent. """

          # Initialize an attribute with a parameter
          self.my_attribute = self.p.my_parameter

     def agent_method(self):
          """ Actions that the agent can take. """

          # Define custom actions here
          pass