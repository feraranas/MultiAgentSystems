'''
gini.py

Method to calculate the Gini Coefficient, which will
measure the inequality among our agents.
'''

import numpy as np

def gini(x):
     """ Calculate Gini Coefficient. """

     x = np.array(x)
     mad = np.abs(np.subtract.outer(x,x)).mean() # Mean absolute difference
     rmad = mad / np.mean(x) # Relative mean absolute difference
     return 0.5 * rmad