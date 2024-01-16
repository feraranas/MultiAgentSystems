# Wealth Transfer

Simple agent-based model with `agentpy` package.

Demonstrates how to create a basic model with a custom agent type, run a simulation, record data, and visualize results.

#### The model explores the distribution of wealth under a trading population of agents.

> Each agent starts with one unit of wealth. During each *time-step*, each agents with positive wealth randomly selects a trading partner and gives them one unit of their wealth. We will see that this random interaction will create an inequality of wealth that follows a **Boltzmann distribution**.