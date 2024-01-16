import agentpy as ap

class Person(ap.Agent):
     def setup(self):
          """ Initialize a new variable at agent creation. """
          # Susceptible = 0, # Infected = 1, Recovered = 2
          self.condition = 0

     def being_sick(self):
          """ Spread disease to peers in the network. """
          rng = self.model.random
          for n in self.network.neighbors(self):
               if n.condition == 0 and self.p.infection_chance > rng.random():
                    n.condition = 1 # Infect susceptible peer
          if self.p.recovery_chance > rng.random():
               self.condition = 2 # Recover from infection
     