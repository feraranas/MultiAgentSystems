import agentpy as ap
import networkx as nx

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

     def see(self):
        """ Define what the agent perceives or 'sees' """
        # We let's return the agent's current condition
        return {"condition": self.condition}

     def next(self, see_results):
        """ Define the next action the agent will take """
        # We return a decision on whether to stay in the current condition
        return {"stay_in_current_condition": True}

     def action(self, next_results):
        """ Define the action the agent will perform """
        # In this case, do nothing if the decision is to stay in the current condition
        pass

class VirusModel(ap.Model):

    def setup(self):
        """ Initialize the agents and network of the model. """

        # Prepare a small-world network
        graph = nx.watts_strogatz_graph(
            self.p.population,
            self.p.number_of_neighbors,
            self.p.network_randomness)

        # Create agents and network
        self.agents = ap.AgentList(self, self.p.population, Person)
        self.network = self.agents.network = ap.Network(self, graph)
        self.network.add_agents(self.agents, self.network.nodes)

        # Infect a random share of the population
        I0 = int(self.p.initial_infection_share * self.p.population)
        self.agents.random(I0).condition = 1

    def update(self):
        """ Record variables after setup and each step. """

        # Record share of agents with each condition
        for i, c in enumerate(('S', 'I', 'R')):
            n_agents = len(self.agents.select(self.agents.condition == i))
            self[c] = n_agents / self.p.population
            self.record(c)

        # Stop simulation if disease is gone
        if self.I == 0:
            self.stop()

    def step(self):
        """ Define the models' events per simulation step. """

        # Call 'being_sick' for infected agents
        self.agents.select(self.agents.condition == 1).being_sick()

    def end(self):
        """ Record evaluation measures at the end of the simulation. """

        # Record final evaluation measures
        self.report('Total share infected', self.I + self.R)
        self.report('Peak share infected', max(self.log['I']))
    
    def see(self):
        """ Define what the model perceives or 'sees' """
        # Return the overall share of infected agents
        share_infected = self.I / self.p.population if self.p.population > 0 else 0
        return {"share_infected": share_infected}

    def next(self, see_results):
        """ Define the next action the model will take """
        # Return a decision on whether to continue the simulation
        return {"continue_simulation": self.schedule.steps < self.p.steps}

    def action(self, next_results):
        """ Define the action the model will perform """
        # In this case, continue the simulation if the decision is to continue
        if next_results["continue_simulation"]:
            self.step()
        else:
            print("Simulation complete.")

parameters = {
    'population': 1000,
    'infection_chance': 0.3,
    'recovery_chance': 0.1,
    'initial_infection_share': 0.1,
    'number_of_neighbors': 2,
    'network_randomness': 0.5
}


model = VirusModel(parameters)
results = model.run()