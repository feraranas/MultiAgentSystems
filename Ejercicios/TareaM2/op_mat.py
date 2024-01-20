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

# Matrix Operations Class
class OpMat:
    
    # Constructor
    def __init__(self) -> None:
        self.I = np.identity(4) # Matriz de Identidad
        self.T = np.identity(4) # Matriz de Traslación
        self.R = np.identity(4) # Matriz de Rotación
        self.A = np.identity(4) # Matriz de Modelado
    
    # Función de traslación
    def translate(self, x, y, z):
        self.T[:, 3] = [x, y, z, 1]
        self.A = self.T @ self.R

    # Función de Escalamiento
    def scale(self, sx, sy, sz):
        scale_matrix = np.array([[sx, 0, 0, 0],
                                 [0, sy, 0, 0],
                                 [0, 0, sz, 0],
                                 [0, 0, 0, 1]])
        self.A = scale_matrix @ self.A

    # Función de Rotación Eje X
    def rotate_x(self, deg):
        self.R = np.identity(4)
        radians = np.radians(deg)
        self.R[1][1] = np.cos(radians)
        self.R[1][2] = -1 * np.sin(radians)
        self.R[2][1] = np.sin(radians)
        self.R[2][2] = np.cos(radians)
        self.A = self.R @ self.A

    # Función de Rotación Eje Y
    def rotate_y(self, deg):
        radians = np.radians(deg)
        rotation_matrix = np.array([
            [np.cos(radians), 0, np.sin(radians), 0],
            [0, 1, 0, 0],
            [-np.sin(radians), 0, np.cos(radians), 0],
            [0, 0, 0, 1]
        ])

        self.A = rotation_matrix @ self.A

    # Función de Rotación Eje Z
    def rotate_z(self, deg):
        self.R = np.identity(4)
        radians = np.radians(deg)
        self.R[1][1] = np.cos(radians)
        self.R[1][2] = -1 * np.sin(radians)
        self.R[2][1] = np.sin(radians)
        self.R[2][2] = np.cos(radians)
        self.A = self.R @ self.A
     
    # Función de Rotación Libre
    def rotate(self, theta, a, b, c):
        
        if (b == 0 and c == 0):
            return self.rotate_x(theta)

        # Normalizar el vector de rotación
        norm = np.sqrt(a**2 + b**2 + c**2)
        a /= norm
        b /= norm
        c /= norm
        d = np.sqrt(b ** 2 + c ** 2)

        Rx = np.identity(4)
        Rx[1][1] = c / d
        Rx[1][2] = -1 * b / d
        Rx[2][1] = b / d
        Rx[2][2] = c / d

        Ry = np.identity(4)
        Ry[0][0] = d
        Ry[0][2] = a
        Ry[2][0] = -1 * a
        Ry[2][2] = d

        Rx_inv = np.identity(4)
        Rx_inv[1][1] = c / d
        Rx_inv[1][2] = b / d
        Rx_inv[2][1] = -1 * b / d
        Rx_inv[2][2] = c / d

        Ry_inv = np.identity(4)
        Ry_inv[0][0] = d
        Ry_inv[0][2] = -1 * a
        Ry_inv[2][0] = a
        Ry_inv[2][2] = d

        RxRy = Ry @ Rx
        RxRy_inv = Ry_inv @ Rx_inv
        self.rotate_z(theta) 
        RxRy_inv @ self.A @ RxRy


    def mult_points(self, points):
        pointsR = (self.A @ points.T).T
        for i in range(0, pointsR.shape[0]):
            for j in range(0, 4):
                points[i, j] = pointsR[i, j]

    def loadIdentity(self):
        self.A = np.identity(4)



