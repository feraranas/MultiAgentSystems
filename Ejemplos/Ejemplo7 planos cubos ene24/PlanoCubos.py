#Autor: Ivan Olmos Pineda
#Curso: Multiagentes - Graficas Computacionales

import math
import numpy as np
import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Se carga el archivo de la clase Cubo
import sys
sys.path.append('..')
from Cubo import Cubo

screen_width = 500
screen_height = 500
#vc para el obser.
FOVY=60.0
ZNEAR=0.01
ZFAR=900.0

# Variables para definir la posicion (coordenadas) del observador

# EYE_X=300.0
# EYE_Y=200.0
# EYE_Z=300.0
EYE_X=0
EYE_Y=5.0
EYE_Z=0

#Variables para definir hacia dónde ve el observador
CENTER_X=1.0
CENTER_Y=5.0
CENTER_Z=0.0

UP_X=0
UP_Y=1
UP_Z=0

#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500

#Dimension del plano
DimBoard = 200

# Variable de control del observador
dir = [1.0, 0.0, 0.0]
theta = 0.0


pygame.init()

#cubo = Cubo(DimBoard, 1.0)
cubos = []
ncubos = 50

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)

def Init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: cubos")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    for i in range(ncubos):
        cubos.append(Cubo(DimBoard, 1.0))

def lookat():
    global CENTER_X
    global CENTER_Z
    # EYE_X = (math.cos(math.radians(theta)) + math.sin(math.radians(theta)))
    # EYE_Z = (-math.sin(math.radians(theta)) + math.cos(math.radians(theta)))
    radians = np.radians(deg)
    rotation_matrix = np.array([
        [np.cos(radians), 0, np.sin(radians), 0],
        [0, 1, 0, 0],
        [-np.sin(radians), 0, np.cos(radians), 0],
        [0, 0, 0, 1]
    ])
    glLoadIdentity()
    gluLookAt( EYE_X,     # Posición (coordenada) X
               EYE_Y,  # Posición (coordenada) Y
               EYE_Z,     # Posición (coordenada) Z
               CENTER_X,  # Posición Apunta Camara X
               CENTER_Y,  # Posición Apunta Camara Y
               CENTER_Z,  # Posición Apunta Camara Z
               UP_X,
               UP_Y,
               UP_Z
            )
    

def display():  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Axis()
    #Se dibuja el plano gris
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    #Se dibuja cubos
    for obj in cubos:
        obj.draw()
        obj.update()
    
done = False
Init()
while not done:

    keys = pygame.key.get_pressed()

    # Right arrow or 'D' letter
    # if keys[pygame.K_d]:
    #     if theta < 1.0:
    #         theta = 360.0
    #     else:
    #         theta += -1.0
    
    # Left arrow or 'A' letter
    if keys[pygame.K_a]:
        dir = 
        theta = 1
        glRotatef(theta, CENTER_X + theta, CENTER_Y, CENTER_Z)
        glPopMatrix()
    

    # Up arrow or 'W' letter
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        EYE_X = EYE_X + dir[0]
        EYE_Z = EYE_Z + dir[2]
        CENTER_X = CENTER_X + dir[0]
        CENTER_Z = CENTER_Z + dir[2]
        lookat()

    # Down arrow or 'S' letter
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        EYE_X = EYE_X - dir[0]
        EYE_Z = EYE_Z - dir[2]
        CENTER_X = CENTER_X + dir[0]
        CENTER_Z = CENTER_Z + dir[2]
        lookat()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()