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

# OpMat file & Piramid class
from op_mat import OpMat
from piramide import Piramide

# Init pygame module
pygame.init()

# Window size
screen_width = 900
screen_height = 600

# Window angularity
FOVY=60.0
ZNEAR=1.0

# Observation limits
ZFAR=500.0

# Definition of observer position
EYE_X=10.0
EYE_Y=10.0
EYE_Z=10.0
CENTER_X=0
CENTER_Y=0
CENTER_Z=0

# Axis orientation
UP_X=0
UP_Y=1
UP_Z=0

# Drawing the system edges
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500

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


# Main function for Initializing view config
def Init():
    screen = pygame.display.set_mode(
    (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: ejes 3D")

    glMatrixMode(GL_MODELVIEW)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(1.0,1.0,1.0,1.0)
    glEnable(GL_DEPTH_TEST)

    sphere = gluNewQuadric()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


# Initializing Matrix Operations Class
op3d = OpMat()

# Defining an object & passing Matrix Operations reference
object1 = Piramide(op3d)

# Initializing main view configs
Init()

# Main Rendering 
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    op3d.loadIdentity()
    
    Axis()

    glColor3f(0.0,0.0,0.0)
    op3d.scale(1.5, 1.0, 1.5)
    op3d.rotate(15, 0.5, 0.5, 0.0)
    op3d.translate(3.0, -5.0, 1.0)
    object1.render()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()