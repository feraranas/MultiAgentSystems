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

        # Outputs an Identity Matrix
        # array([ [1., 0., 0., 0.],
        #         [0., 1., 0., 0.],
        #         [0., 0., 1., 0.],
        #         [0., 0., 0., 1.]])
        
    def translate(self, x, y, z):
        self.T[0][3] = x
        self.T[1][3] = y
        self.T[2][3] = z
        self.T[3][3] = 1
        self.A = self.T @ self.R
        
        # or
        # self.T[:, 3] = [x, y, z, 1]
        # self.A = self.T @ self.R

        # Outputs:
        # array([[1., 0., 0., x],
        #        [0., 1., 0., y],
        #        [0., 0., 1., z],
        #        [0., 0., 0., 1.]])


    def scale(self, sx, sy, sz):
        scale_matrix = np.array([[sx, 0, 0, 0],
                                 [0, sy, 0, 0],
                                 [0, 0, sz, 0],
                                 [0, 0, 0, 1]])
        self.A = scale_matrix @ self.A

    
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
        
    def rotate(self, angle, x, y, z):
        # Convertir el ángulo a radianes
        angle_rad = np.radians(angle)

        # Normalizar el vector de rotación
        length = np.sqrt(x**2 + y**2 + z**2)
        x /= length
        y /= length
        z /= length

        # Matriz de rotación para el eje arbitrario
        c = np.cos(angle_rad)
        s = np.sin(angle_rad)
        t = 1 - c

        rotation_matrix = np.array([
            [t*x**2 + c, t*x*y - s*z, t*x*z + s*y, 0],
            [t*x*y + s*z, t*y**2 + c, t*y*z - s*x, 0],
            [t*x*z - s*y, t*y*z + s*x, t*z**2 + c, 0],
            [0          , 0          , 0         , 1]
        ])

        self.A = rotation_matrix @ self.A
    
    def mult_points(self, points):
        pointsR = (self.A @ points.T).T
        # for i in range(0, pointsR.shape[1] + 1):
        #     for j in range(0, 4):
        #         points[i][j] = pointsR[i][j]
                
        # or
        for i in range(0, pointsR.shape[0]):
            for j in range(0, 4):
                points[i, j] = pointsR[i, j]

    def loadIdentity(self):
        self.A = np.identity(4)