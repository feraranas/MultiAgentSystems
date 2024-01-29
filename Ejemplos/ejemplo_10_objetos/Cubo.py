#Autor: Ivan Olmos Pineda


import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import random
import math

class Cubo:
    
    def __init__(self, dim, vel, Scale):
        self.points = np.array([[-1.0,-1.0, 1.0], [1.0,-1.0, 1.0], [1.0,-1.0,-1.0], [-1.0,-1.0,-1.0],
                                [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0,-1.0], [-1.0, 1.0,-1.0]])
        self.scale = Scale
        self.radio = math.sqrt(self.scale*self.scale + self.scale*self.scale)
        self.DimBoard = dim
        #Se inicializa una posicion aleatoria en el tablero
        self.Position = []
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        self.Position.append(self.scale)
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        #Se inicializa un vector de direccion aleatorio
        self.Direction = []
        self.Direction.append(random.random())
        self.Direction.append(self.scale)
        self.Direction.append(random.random())
        #Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0]*self.Direction[0] + self.Direction[2]*self.Direction[2])
        self.Direction[0] /= m
        self.Direction[2] /= m
        #Se cambia la maginitud del vector direccion
        self.Direction[0] *= vel
        self.Direction[2] *= vel
        #deteccion de colision
        self.collision = False
        #arreglo de cubos
        self.Cubos = []

    def getCubos(self, Ncubos):
        self.Cubos = Ncubos

    def update(self):
        self.CollitionDetection()
        if self.collision == False:
            new_x = self.Position[0] + self.Direction[0]
            new_z = self.Position[2] + self.Direction[2]
            
            if(abs(new_x) <= self.DimBoard):
                self.Position[0] = new_x
            else:
                self.Direction[0] *= -1.0
                self.Position[0] += self.Direction[0]
            
            if(abs(new_z) <= self.DimBoard):
                self.Position[2] = new_z
            else:
                self.Direction[2] *= -1.0
                self.Position[2] += self.Direction[2]

    def drawFaces(self):
        glBegin(GL_QUADS)
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[2])
        glVertex3fv(self.points[3])
        glEnd()
        glBegin(GL_QUADS)
        glVertex3fv(self.points[4])
        glVertex3fv(self.points[5])
        glVertex3fv(self.points[6])
        glVertex3fv(self.points[7])
        glEnd()
        glBegin(GL_QUADS)
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[5])
        glVertex3fv(self.points[4])
        glEnd()
        glBegin(GL_QUADS)
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[2])
        glVertex3fv(self.points[6])
        glVertex3fv(self.points[5])
        glEnd()
        glBegin(GL_QUADS)
        glVertex3fv(self.points[2])
        glVertex3fv(self.points[3])
        glVertex3fv(self.points[7])
        glVertex3fv(self.points[6])
        glEnd()
        glBegin(GL_QUADS)
        glVertex3fv(self.points[3])
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[4])
        glVertex3fv(self.points[7])
        glEnd()
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(self.scale,self.scale,self.scale)
        glColor3f(1.0, 1.0, 1.0)
        self.drawFaces()
        glPopMatrix()
        
    def CollitionDetection(self):
        for obj in self.Cubos:
            if self != obj:
                d_x = self.Position[0] - obj.Position[0]
                d_z = self.Position[2] - obj.Position[2]
                d_c = math.sqrt(d_x * d_x + d_z * d_z)
                if d_c - (self.radio + obj.radio) < 0.0:
                    self.collision = True
                