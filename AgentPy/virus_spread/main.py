import sys
sys.path.append('.')
from model import VirusModel


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