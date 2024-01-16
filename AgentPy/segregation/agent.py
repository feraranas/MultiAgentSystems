import agentpy as ap

class Person(ap.Agent):

     def setup(self):
          """ Initiate agent attributes. """

          self.grid = self.model.grid
          self.random = self.model.random
          self.group = self.random.choice(range(self.p.n_groups))
          self.share_similar = 0
          self.happy = False
     
     def update_happiness(self):
          """ Be happy if rate of similar neighbors is high enough. """

          neighbors = self.grid.neighbors(self)
          similar = len([n for n in neighbors if n.group == self.group])
          ln = len(neighbors)
          self.share_similar = similar / ln if ln > 0 else 0
          self.happy = self.share_similar >= self.p.want_similar
     
     def find_new_home(self):
          """ Move to random free spot and update free spots. """

          new_spot = self.random.choice(self.model.grid.empty)
          self.grid.move_to(self, new_spot)