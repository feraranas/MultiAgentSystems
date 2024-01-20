'''
model.py

'''
# Model design
import agentpy as ap
import numpy as np
import seaborn as sns


def gini(x):
     """ Calculate Gini Coefficient. """

     x = np.array(x)
     mad = np.abs(np.subtract.outer(x,x)).mean() # Mean absolute difference
     rmad = mad / np.mean(x) # Relative mean absolute difference
     return 0.5 * rmad


class WealthAgent(ap.Agent):
     """ An Agent with wealth. """

     def setup(self):
          self.wealth = 1
     
     def wealth_transfer(self):

          if self.wealth > 1:

               partner = self.model.agents.random()
               partner.wealth += 1
               self.wealth -= 1


class WealthModel(ap.Model):
    """ A simple model of random wealth transfers. """
    
    def setup(self):
        """ Defines how many agents should be created at the beginning of the sim. """
        self.agents = ap.AgentList(self, self.p.agents, WealthAgent)

    def update(self):
          """ Calculates and records the current Gini Coefficient after each time-step. """
          self.record("Gini Coefficient", gini(self.agents.wealth))

    def step(self):
          """ Calls all agents during each time-step to perform their wealth_transfer method. """
          self.agents.wealth_transfer()

    def see(self):
        # Define what the model perceives or "sees"
        # For simplicity, let's assume the model sees the current Gini Coefficient
        return {"gini_coefficient": self.datacollector.get_agent_vars_dataframe().mean()}

    def next(self):
        # Define the next action the model will take
        # For simplicity, let's assume the model decides whether to continue the simulation
        return {"continue_simulation": self.schedule.steps < self.p.steps}

    def action(self, decision):
        # Define the action the model will perform
        # For simplicity, let's print the current Gini Coefficient and whether to continue
        gini_coefficient = decision["see_results"]["gini_coefficient"]["wealth"]
        continue_simulation = decision["next_results"]["continue_simulation"]
        
        print(f"Current Gini Coefficient: {gini_coefficient}")
        
        if continue_simulation:
            self.step()
        else:
            print("Simulation complete.")

    def end(self):
          """ Called at the end if the simulation, we record the wealth of each agent. """
          self.agents.record("wealth")

# To prepare, we define a parameter dictionary with a random_seed, 
# the number of agents, and the number of time-steps.
parameters = {
     'agents': 100,
     'steps': 100,
     'seed': 42,
}

# To perform a simulation, we initialize our model with a given
# set of parameters, and call `Model.run()`
model = WealthModel(parameters=parameters)
results = model.run()