# Virus Spread
*keywords*: [*network enviroments*], [*agent sequences*]

This is an agent-based model that simulates the propagation of a disease through a network. We are creating visualizing networks, using the interactive module of `agentpy` and perform different types of sensitivity analysis.

# About the model

The agents of this model are people, which can be in one of the following three conditions: susceptible to the disease (S), infected (I), or recovered (R). The agents are connected to each other through a small-world network of peers. At every time-step, infected agents can infect their peers or recover from the disease based on random chance.

# Defining the model

- Agent : [Person](./agent.py) We define a new agent type `Person` by creating a subclass of `Agent`. This agent has two methods: `setup()` will be called automatically at the agent's creation, and `being_sick()` will be called by the `Model.step()` function. Three tools are used within this class:

- `Agent.p` : returns the parameters of the model.
- `Agent.neighbors()` : returns a list of agents' peers in the network.
- `random.random()` : returns a uniform random draw between 0 and 1.

- Model : [VirusModel](./model.py) is defined by creating a subclass of Model. The four methods of this class will be called automatically at different steps of the simulation.

#### Reference

[Agentpy virus model](https://agentpy.readthedocs.io/en/latest/agentpy_virus_spread.html)