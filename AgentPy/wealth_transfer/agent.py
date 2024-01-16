'''
Agent.py

'''

import agentpy as ap

class WealthAgent(ap.Agent):
     """ An Agent with wealth. """

     def setup(self):
          self.wealth = 1
     
     def wealth_transfer(self):

          if self.wealth > 1:

               partner = self.model.agents.random()
               partner.wealth += 1
               self.wealth -= 1