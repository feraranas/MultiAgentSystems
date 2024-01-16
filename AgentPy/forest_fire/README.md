# Forest Fire

This agent-based model simulates a forest fire. We use `agentpy` library to work with a spatial grid and create animations, and perform a parameter sweep.

# About the model

The model is based on the NetLogo FireSimple model by Uri Wilensky and William Rand, who describe it as follows:

> This model simulates the spread of a fire through a forest. It shows that the fire's chance of reaching the right edge of the forest depends critically on the density of trees. This is an example of a common feature of complex systems, the presence of a non-linear threshold or critical parameter. [...]

> The fire starts on the left edge of the forest, and spreads to neighboring trees. The fire spreads in four directions: north, east, south, and west.

> The model assumes there is no wind. So, the fire must have trees along its path in order to advance. That is, the fire cannot skip over an unwooded area (patch), so such a patch blocks the fire's motion in that direction.

### References

- [NetLogo FireSimple model](https://ccl.northwestern.edu/netlogo/models/FireSimple)

- [Agentpy forest fire](https://agentpy.readthedocs.io/en/latest/agentpy_forest_fire.html)

- Wilensky, U. & Rand, W. (2015). Introduction to Agent-Based Modeling: Modeling Natural, Social and Engineered Complex Systems with NetLogo. Cambridge, MA. MIT Press.
