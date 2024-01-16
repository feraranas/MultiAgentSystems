import sys
import agentpy as ap
sys.path.append('.')

from agent import Person

class SegregationModel(ap.Model):

     def setup(self):

          # Parameters
          s = self.p.size
          n = self.n = int(self.p.density * (s ** 2))

          # Create grid and agents

          # Environment that contains agents with a discrete spatial topology, 
          # supporting multiple agents and attribute fields per cell.
          self.grid = ap.Grid(
               
               # model (Model): The model instance.
               self,

               # shape (tuple of int): Size of the grid. 
               # The length of the tuple defines the number of dimensions, 
               # and the values in the tuple define the length of each dimension.
               (s, s),

               # torus (bool, optional): Whether to connect borders (default False).
               # If True, the grid will be toroidal, meaning that agents who move over a 
               # border will re-appear on the opposite side. If False, they will 
               # remain at the edge of the border.
               torus=False,

               # track_empty (bool, optional): Whether to keep track of empty cells (default False).
               # If true, empty cells can be accessed via Grid.empty.
               track_empty=True)
          
          ''' Grid Class Attributes :
               agents (GridIter):
                    Iterator over all agents in the grid.
               positions (dict of Agent):
                    Dictionary linking each agent instance to its position.
               grid (numpy.rec.array):
                    Structured numpy record array with a field 'agents'
                    that holds an AgentSet in each position.
               shape (tuple of int):
                    Length of each dimension.
               ndim (int):
                    Number of dimensions.
               all (list):
                    List of all positions in the grid.
               empty (ListDict):
                    List of unoccupied positions, only available if the Grid was initiated with track_empty=True.
          '''

          self.agents = ap.AgentList(self, n, Person)

          # Adds agents to the grid environment.
          self.grid.add_agents(
               # agents : Iterable of agents to be added.
               agents=self.agents,
               
               # The positions of the agents. Must have the same length as 'agents', 
               # with each entry being a tuple of integers. If none is passed, positions 
               # will be chosen automatically based on the arguments 'random' and 'empty':
               positions=None,
               
               # 1. random and empty: Random selection without repetition from Grid.empty
               # 2. random and not empty: Random selection with repetition from Grid.all
               # 3. not random and empty: Iterative selection from Grid.empty
               # 4. not random and not empty: Iterative selection from Grid.all
               random=True,
               empty=True)


     # After every step (update), agents update their happiness.
     # If all agents are happy, the simulation is stopped.
     def update(self):
         # Update list of unhappy people
        self.agents.update_happiness()
        self.unhappy = self.agents.select(self.agents.happy == False)

        # Stop simulation if all are happy
        if len(self.unhappy) == 0:
            self.stop()
     
      
     # At every step, unhappy people move to a new location.
     # Recall that this function is called for every agent in the model.
     def step(self):
        # Move unhappy people to new location
        self.unhappy.find_new_home()
     

parameters = {
     'want_similar': 0.3, # For agents to be happy
     'n_groups': 2, # Number of groups
     'density': 0.95, # Density of population
     'size': 50, # Height and length of the grid
     'steps': 50, # Maximum number of steps
}