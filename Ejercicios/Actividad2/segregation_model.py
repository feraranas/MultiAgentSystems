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
     
     def see(self):
        """ Define what the agent perceives or 'sees' """
        # We return the agent's group and its happiness level
        return {"group": self.group, "happiness": self.happy}

     def next(self, see_results):
        """ Define the next action the agent will take """
        # We return a decision on whether to move
        # based on the agent's happiness level
        return {"move": not see_results["happiness"]}

     def action(self, next_results):
        """ Define the action the agent will perform """
        # In this case, move to a new spot if the decision is to move
        if next_results["move"]:
            self.find_new_home()

class SegregationModel(ap.Model):

     def setup(self):

          # Parameters
          s = self.p.size
          n = self.n = int(self.p.density * (s ** 2))

          # Create grid and agents

          # Environment that contains agents with a discrete spatial topology, 
          # supporting multiple agents and attribute fields per cell.
          self.grid = ap.Grid(
               self,
               (s, s),
               torus=False,
               track_empty=True
               )
     
          self.agents = ap.AgentList(self, n, Person)

          # Adds agents to the grid environment.
          self.grid.add_agents(
               agents=self.agents,
               positions=None,
               random=True,
               empty=True
               )

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
        """ Move unhappy people to new location """
        self.unhappy.find_new_home()

     def see(self):
        """ Define what the model perceives or 'sees' """
        # We return the overall happiness level of the population
        happiness_levels = [agent.happy for agent in self.agents]
        overall_happiness = sum(happiness_levels) / len(happiness_levels) if happiness_levels else 0
        return {"overall_happiness": overall_happiness}

     def next(self, see_results):
        """ Define the next action the model will take """
        # We return a decision on whether to continue the simulation
        return {"continue_simulation": self.schedule.steps < self.p.steps}

     def action(self, next_results):
        """ Define the action the model will perform """
        # We continue the simulation if the decision is to continue
        if next_results["continue_simulation"]:
            self.step()
        else:
            print("Simulation complete.")
     

parameters = {
     'want_similar': 0.3, # For agents to be happy
     'n_groups': 2, # Number of groups
     'density': 0.95, # Density of population
     'size': 50, # Height and length of the grid
     'steps': 50, # Maximum number of steps
}


model = SegregationModel(parameters=parameters)
results = model.run()