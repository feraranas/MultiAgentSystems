# Pygame
import pygame
from pygame.locals import *


# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Maths
import math
import numpy as np


# System files
import sys
sys.path.append('.')


# OpMat file
from op_mat import OpMat


# Piramid Class
class Piramide:

     # Constructor
     def __init__(self, op: OpMat) -> None:
          self.op3D: OpMat = op
          self.points = np.array([[1.0,   0.0,   1.0,  1.0],
                                  [1.0,   0.0,  -1.0,  1.0],
                                  [-1.0,  0.0,  -1.0,  1.0],
                                  [-1.0,  0.0,   1.0,  1.0],
                                  [0.0,   3.0,   0.0,  1.0]])
     
     # Render function
     def render(self):
          pointsR = self.points.copy()
          self.op3D.mult_points(pointsR)

          glBegin(GL_QUADS)
          for i in range(4):
               glVertex3f(pointsR[i][0], pointsR[i][1], pointsR[i][2])
          glEnd()
          
          for i in range(4):
               glBegin(GL_LINES)
               glVertex3f(pointsR[i][0], pointsR[i][1], pointsR[i][2])
               glVertex3f(pointsR[4][0], pointsR[4][1], pointsR[4][2])
               glEnd()