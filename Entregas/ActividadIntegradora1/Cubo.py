from typing import Optional
import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np

class Cubo:
    
    def __init__(self, dim, scale, color, colisionado):
        """
        Función que inicializa un objeto de la clase Cubo con los parámetros especificados.

        Parámetros:
        - dim (int): Dimensión del tablero en el que se encuentra el cubo.
        - scale (list): Lista que especifica la escala del cubo en los ejes x, y, z.
        - color (list): Lista que representa el color del cubo en formato RGB.
        - colisionado (bool): Indica si el cubo ha colisionado con otro objeto.
        
        Retorna:
        No hay valor de retorno.
        """
        
        self.scale = scale
        self.radius = math.sqrt(4)
        self.color = color
        self.colisionado = False
        self.Rotation = [0,0,0,0]

        # vertices del cubo
        pointsCube = np.array([[-1.0,-1.0, 1.0], [1.0,-1.0, 1.0], [1.0,-1.0,-1.0], [-1.0,-1.0,-1.0],
                                [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0,-1.0], [-1.0, 1.0,-1.0]])
        # Calculate center of the cube
        center = np.mean(pointsCube, axis=0)

        # Calculate half side length
        half_side_length = np.max(np.abs(pointsCube - center))

        # Adjust the coordinates to center the cube
        self.points = pointsCube - center + [half_side_length, half_side_length, half_side_length]
        
        self.DimBoard = dim
        
        #Se inicializa una posicion aleatoria en el tablero
        self.Position = []
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        self.Position.append(5.0)
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))

    def drawFaces(self):
        """
        Función que dibuja las caras de un cubo utilizando OpenGL.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        
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
        """
        Función que dibuja el cubo en la posición actual y con la escala y rotación especificadas.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        if (self.colisionado): return
        
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glRotate(self.Rotation[0], self.Rotation[1], self.Rotation[2], self.Rotation[3])
        glScaled(self.scale[0], self.scale[1], self.scale[2])
        glColor3f(self.color[0], self.color[1], self.color[2])
        self.drawFaces()
        glPopMatrix()
        
    def modifyPosition(self, x, y, z):
        """
        Función que modifica temporalmente la posición del cubo para realizar operaciones específicas.

        Parámetros:
        - x: Nueva coordenada x de la posición.
        - y: Nueva coordenada y de la posición.
        - z: Nueva coordenada z de la posición.
        
        Retorna:
        No hay valor de retorno.
        """
        glPushMatrix()
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(x, y, z)
        self.drawFaces()
        glPopMatrix()