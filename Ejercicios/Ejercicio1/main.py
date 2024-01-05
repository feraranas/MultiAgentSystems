# Pygame
import pygame
from pygame.locals import *

# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Maths
import numpy as np

import sys
sys.path.append('.')

from op_mat import OpMat
from piramide import Piramide

pygame.init()

screen_width = 900
screen_height = 600
#vc para el obser.

# Angularidad
FOVY=60.0


ZNEAR=1.0

# Limites de observación
ZFAR=500.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X=10.0
EYE_Y=10.0
EYE_Z=10.0
CENTER_X=0
CENTER_Y=0
CENTER_Z=0
UP_X=1
UP_Y=0
UP_Z=0
#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500

# Objects
op3D = OpMat()
obj1 = Piramide(op3D)

# Título
pygame.display.set_caption("Ejercicio 1")

def Init():
    screen = pygame.display.set_mode(
    (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: ejes 3D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)

    sphere = gluNewQuadric()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

Init()
done = False
while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    obj1.render()

    pygame.display.flip()
    pygame.time.wait(100)

# pygame.quit()