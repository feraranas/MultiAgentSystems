# Pygame
import pygame
from pygame.locals import *


# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Sphere Class
class Sphere:
     '''
     Clase Sphere recibe 4 parámetros:
     - radius : radio de una esfera
     - color : color rgb para la esfera
     - angular_velocity : velocidad angular de la esfera
     - distance_from_parent : distancia del origen (0,0,0)
     '''

     # Constructor
     def __init__(self, radius, color, angular_velocity, distance_from_parent) -> None:
          self.radius = radius
          self.color = color
          self.angular_velocity = angular_velocity
          self.distance_from_parent = distance_from_parent
     
     def draw_sphere(self):
          glRotatef(self.angular_velocity * pygame.time.get_ticks() / 100, 0, 1, 0) # rotate around y-axis
          glTranslatef(self.distance_from_parent, 0, 0) # translate to the orbit distance
          glColor3fv(self.color) # color of the sphere
          glutSolidSphere(self.radius, 50, 50) # draw sphere

# Solar System Class
class SolarSystem:

    # Constructor
    def __init__(self) -> None:
        self.sun = Sphere(radius=1.2, color=(1, 0, 0), angular_velocity=0.5, distance_from_parent=0)  # creating the sun
        self.planets = [
            Sphere(radius=0.4, color=(1, 1, 1), angular_velocity=1, distance_from_parent=2),  # first planet (white)
            Sphere(radius=0.65, color=(0, 1, 0), angular_velocity=1.2, distance_from_parent=6.5),  # second planet (green)
            Sphere(radius=0.85, color=(0.906, 0.314, 0.969), angular_velocity=1.6, distance_from_parent=10),  # third planet (pink)
        ]
        self.planet_moons = [
            [], # no moons for planet 1
            [
               Sphere(radius=0.3, color=(1, 1, 0.1), angular_velocity=2, distance_from_parent=1.2),  # creating yellow moon 1 for planet 2
               Sphere(radius=0.2, color=(1, 1, 0.2), angular_velocity=3, distance_from_parent=1.5),  # creating yellow moon 2 for planet 2
            ],
            [
               Sphere(radius=0.28, color=(0, 0.2, 0.8), angular_velocity=1, distance_from_parent=1.5),  # creating blue moon 1 for planet 3
               Sphere(radius=0.35, color=(0, 0.3, 0.9), angular_velocity=2, distance_from_parent=2.2),  # creating blue moon 2 for planet 3
               Sphere(radius=0.22, color=(0, 0.4, 0.86), angular_velocity=1.5, distance_from_parent=2),  # creating blue moon 3 for planet 3
               Sphere(radius=0.15, color=(0, 0.5, 0.7), angular_velocity=0.5, distance_from_parent=2),  # creating blue moon 4 for planet 3
            ],
        ]

    def draw(self):
        glPushMatrix()  # save the matrix
        glRotatef(1, 0, 1, 0)  # Rotate entire SolarSystem around y-axis
        self.sun.draw_sphere()  # Drawing sun

        for planet, moons in zip(self.planets, self.planet_moons):
            glPushMatrix()  # save the matrix so that the sun is the parent
            planet.draw_sphere()  # drawing the planet

            for moon in moons:
               glPushMatrix()  # save the matrix so that planet is the parent
               moon.draw_sphere()  # Drawing moons around the planet
               glPopMatrix()  # pop modelview matrix from the stack

            glPopMatrix()  # pop modelview matrix from the stack

        glPopMatrix()  # pop modelview matrix from the stack
