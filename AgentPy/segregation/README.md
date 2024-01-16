# Segregation

Agent-based model of segregation dynamics.

The model is based on the NetLogo Segregation model from Uri Wilensky, who describes it as follows:

This project models the behavior of two types of agents in a neighborhood. The orange agents and blue agents get along with one another. But each agent wants to make sure that it lives near some of "its own". That is, each orange agent wants to live near at least some orange agents, and eeach blue agent wants to live near at least some blue agents. The simulation shows how these individual preferences ripple through the neighborhood, leasing to large-scale patterns.

## Model definition

To start, we define our agents who initiate with a random group and have two methods to check whether they are happy and to move to a new location if they are not.

Next, we define our model, which consists of our agents and a spatial grid environment. At every step, unhappy people move to a new location. After every step (update), agents update their happiness. If all agents are happy, the simulation is stopped.

