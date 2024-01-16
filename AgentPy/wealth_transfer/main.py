'''
main.py

Simulation run
'''

import sys
sys.path.append('.')
from model import WealthModel

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
'''
Completed: 100 steps
Run time: 0:00:00.016699
Simulation finished
'''

# General information about the simulation.
print(results.info)
'''
{
     'model_type': 'WealthModel',
     'time_stamp': '2024-01-15 14:33:12',
     'agentpy_version': '0.1.5',
     'python_version': '3.11.',
     'experiment': False,
     'completed': True,
     'created_objects': 100,
     'completed_steps': 100,
     'run_time': '0:00:00.010194'
}
'''