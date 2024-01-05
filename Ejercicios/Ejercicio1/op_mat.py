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

class OpMat:
    def __init__(self) -> None:
        self.T = np.identity(4)
        self.R = np.identity(4)
        self.A = np.identity(4)
        
        # or:
        # self.I = np.identity(4)
        # self.T = self.I.copy()
        # self.R = self.I.copy()
        # self.A = self.I.copy()
        
    def translate(self, x, y, z):
        self.T[0][3] = x
        self.T[1][3] = y
        self.T[2][3] = z
        self.T[3][3] = 1
        self.A = self.T @ self.R
        
        # or
        # self.T[:, 3] = [x, y, z, 1]
        # self.A = self.T @ self.R
        
    
    def rotate_x(self, deg):
        self.R = np.identity(4)
        radians = np.radians(deg)
        self.R[1][1] = np.cos(radians)
        self.R[1][2] = -1 * np.sin(radians)
        self.R[2][1] = np.sin(radians)
        self.R[2][2] = np.cos(radians)
        self.A = self.R @ self.A
        
        # or 
        # radians = np.radians(deg)
        # rotation_matrix = np.array([[1, 0, 0, 0],
        #                         [0, np.cos(radians), -np.sin(radians), 0],
        #                         [0, np.sin(radians), np.cos(radians), 0],
        #                         [0, 0, 0, 1]])
        # self.A = rotation_matrix @ self.A    
        
    
    def mult_points(self, points):
        pointsR = (self.A @ points.T).T
        for i in range(0, pointsR.shape[1] + 1):
            for j in range(0, 4):
                points[i][j] = pointsR[i][j]
                
        # or
        # pointsR = (self.A @ points.T).T
        # for i in range(0, pointsR.shape[0]):
        #     for j in range(0, 4):
        #         points[i, j] = pointsR[i, j]
