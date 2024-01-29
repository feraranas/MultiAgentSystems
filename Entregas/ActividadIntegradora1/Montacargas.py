from enum import Enum
import math
import time
import pygame
from pygame.locals import *
import numpy as np
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np

class EstadosMontacargas(Enum):
    NAVEGACION = 0
    COLISION = 1
    REORIENTACION = 2
    AVANDESTINO = 3
    DEPOSITANDO = 4

class Montacargas:
    
    def __init__(self, dim, vel, scale, cubos):
        """
        Constructor de la clase Montacargas.

        Parámetros:
        - self: Instancia de la clase.
        - dim: Dimensión del tablero.
        - vel: Velocidad del montacargas.
        - scale: Escala para la figura.
        - cubos: Lista de cubos en el almacén.
        
        Retorna:
        No hay valor de retorno.
        """
        
        self.radius = 10
        self.scale = scale
        self.vel = vel
        self.Cubos = cubos
        self.collided_cube = None
        
        self.Ymin = 0.9
        self.Ymax = 4
        self.estado = EstadosMontacargas.NAVEGACION
        self.altura = self.Ymin

        self.target_rotation_angle = 180.0 # ángulo deseado al centro (0,0,0)
        self.current_rotation_angle = 0.0
        self.rotation_speed = 4.0  # velocidad de rotación
        
        self.DimBoard = dim
        
        # Se inicializa una posicion aleatoria en el tablero
        self.Position = []
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        self.Position.append(5.0)
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        
        # Se inicializa un vector de direccion aleatorio
        self.Direction = []
        self.Direction.append(random.random())
        self.Direction.append(5.0)
        self.Direction.append(random.random())
        
        # Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0]*self.Direction[0] + self.Direction[2]*self.Direction[2])
        self.Direction[0] /= m
        self.Direction[2] /= m
        
        # Se cambia la magnitud del vector direccion
        self.Direction[0] *= vel
        self.Direction[2] *= vel
    
    def collision_detection(self):
        """
        Función que realiza la detección de colisiones entre el montacargas y los cubos en el almacén.
        Actualiza el estado del montacargas a EstadosMontacargas.COLISION si hay colisión.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """     
               
        for cube in self.Cubos:
            if  self != cube and \
                self.collided_cube == None and \
                self.estado != EstadosMontacargas.COLISION and \
                cube.colisionado == False:

                d_x = self.Position[0] - cube.Position[0]
                d_z = self.Position[2] - cube.Position[2]
                d_c = math.sqrt(d_x * d_x + d_z * d_z)
                
                if d_c - (self.radius + cube.radius) < 0.0:
                    self.estado = EstadosMontacargas.COLISION # actualizamos el estado del montacargas a COLISION
                    self.collided_cube = cube  # guardamos la referencia al cubo colisionado
                    cube.colisionado = True # actualizamos el estado del cubo en particular

    def random_movement(self):
        """
        Función que genera un movimiento aleatorio del montacargas en el tablero.
        Realiza la detección de colisiones en la nueva posición.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        
        # Movemos al montacargas a una nueva posición
        new_x = self.Position[0] + self.Direction[0]
        new_z = self.Position[2] + self.Direction[2]
        
        # detectamos que el montacargas no se salga del area de navegacion
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
        
        # verificamos si el montacargas colisionó con un cubo en su nueva posición
        self.collision_detection()

    def platform_animation(self):
        """
        Función que efectúa la animación de la plataforma después de una detección de colisión.
        Incrementa la altura de la plataforma y cambia de estado cuando alcanza la altura máxima.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        
        if self.altura < self.Ymax:
                self.altura += 0.05
        else:
            self.estado = EstadosMontacargas.REORIENTACION
            self.current_rotation_angle = math.atan2(self.Direction[2], self.Direction[0]) * (180 / math.pi) 
            self.target_rotation_angle = math.atan2(-self.Position[2], -self.Position[0]) * (180 / math.pi) 

    def advance_to_destiny(self):
        """
        Función que avanza el montacargas hacia el destino de entrega (centro del sistema).
        Cambia al estado EstadosMontacargas.DEPOSITANDO cuando llega al centro.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        
        if self.collided_cube is not None:

            # volteamos la dirección del montacargas
            new_x = -1 * self.Position[0]
            new_z = -1 * self.Position[2]
            
            # calculamos la norma del vector
            magnitude = math.sqrt(new_x ** 2 + new_z ** 2)

            if magnitude != 0:
                # normalizamos el vector dirección
                new_x /= magnitude
                new_z /= magnitude

                # actualizamos velocidad
                self.Direction[0] = new_x * self.vel
                self.Direction[2] = new_z * self.vel

                # movemos al montacargas en la nueva dirección al centro
                self.Position[0] += self.Direction[0]
                self.Position[2] += self.Direction[2]

                # movemos al cubo colisionado igualmente al centro
                self.collided_cube.Position[0] += self.Direction[0]
                self.collided_cube.Position[2] += self.Direction[2]

                # checamos si hemos llegado al centro
                if abs(self.Position[0]) < self.radius and abs(self.Position[2]) < self.radius:
                        
                    # efectuamos el dropdown
                    self.estado = EstadosMontacargas.DEPOSITANDO

    def reorientacion(self):
        """
        Función que realiza la animación de rotación del montacargas hacia el punto destino.
        Calcula la diferencia de ángulos entre la rotación actual y la deseada.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        
        # Calcular la diferencia entre los ángulos
        angle_difference = self.target_rotation_angle - self.current_rotation_angle

        # Calcular el incremento basado en la velocidad de rotación y el tiempo transcurrido
        rotation_increment = self.rotation_speed 

        if abs(angle_difference) > 0:
            # Si la diferencia de ángulo es mayor que el incremento, rotar en consecuencia
            rotation_direction = 1.0 if angle_difference > 0 else -1.0
            self.current_rotation_angle += rotation_direction * rotation_increment
        else:
            # Si la diferencia de ángulo es menor que el incremento, establecer el ángulo deseado
            self.current_rotation_angle = self.target_rotation_angle

        if abs(angle_difference) < rotation_increment:
            # Si la diferencia es muy pequeña, pasar al siguiente estado
            self.estado = EstadosMontacargas.AVANDESTINO

        # Calcular la dirección basada en el ángulo actual de rotación
        radians = math.radians(self.current_rotation_angle)
        self.Direction[0] = math.cos(radians) * self.vel
        self.Direction[2] = math.sin(radians) * self.vel

        self.drawTruck()

    def animationDown(self):
        """
        Función que realiza la animación del descenso de la plataforma después de la entrega del cubo.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        
        # descendemos el nivel de la plataforma a ymin
        if self.altura > self.Ymin:
            if self.collided_cube is not None:        
                
                self.altura -= 0.05
                self.collided_cube.Position[1] -= 0.3

                self.collided_cube.draw()
        else:
            # eliminamos el collided_cube de la lista Cubos
            if self.collided_cube in self.Cubos:
                self.Cubos.remove(self.collided_cube)

                # restauramos la dirección del montacargas a aleatoria
                self.Direction[0] = random.random()
                self.Direction[2] = random.random()

                # normalizamos
                m = math.sqrt(self.Direction[0] * self.Direction[0] + self.Direction[2] * self.Direction[2])
                self.Direction[0] /= m
                self.Direction[2] /= m

                # actualizamos la velocidad
                self.Direction[0] *= self.vel
                self.Direction[2] *= self.vel

                # reseteamos estado collision y la referencia al collided_cube
                self.estado = EstadosMontacargas.NAVEGACION
                self.collided_cube = None
                            
                new_x = self.Position[0] + self.Direction[0]
                new_z = self.Position[2] + self.Direction[2]

                self.Position[0] = new_x
                self.Position[2] = new_z

    def update(self):
        """
        Función que actualiza el estado del montacargas según la lógica definida para cada estado.
        Llama a las funciones correspondientes dependiendo del estado actual.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        
        if (self.estado == EstadosMontacargas.NAVEGACION):
            self.random_movement()
        elif (self.estado == EstadosMontacargas.COLISION):
            self.platform_animation()
        elif (self.estado == EstadosMontacargas.REORIENTACION):
            self.reorientacion()
        elif (self.estado == EstadosMontacargas.AVANDESTINO):
            self.advance_to_destiny()
        elif (self.estado == EstadosMontacargas.DEPOSITANDO):
            self.animationDown()

    def drawRectangle(self, x, y, z, width, height, depth):
        """
        Función que dibuja un rectángulo en el espacio tridimensional con las dimensiones especificadas.
        
        Parámetros:
        - self: Instancia de la clase.
        - x: Posición del rectángulo en el eje x.
        - y: Posición del rectángulo en el eje y.
        - z: Posición del rectángulo en el eje z.
        - width: Ancho del rectángulo.
        - height: Altura del rectángulo.
        - depth: Profundidad del rectángulo.
        
        Retorna:
        No hay valor de retorno.
        """
        glColor3f(0.925, 0.19, 0.03)
        glBegin(GL_QUADS)
        
        # Bottom face
        glVertex3f(x, y, z)
        glVertex3f(x + width, y, z)
        glVertex3f(x + width, y + height, z)
        glVertex3f(x, y + height, z)

        # Top face
        glVertex3f(x, y, z + depth)
        glVertex3f(x + width, y, z + depth)
        glVertex3f(x + width, y + height, z + depth)
        glVertex3f(x, y + height, z + depth)

        # Front face
        glVertex3f(x, y, z)
        glVertex3f(x + width, y, z)
        glVertex3f(x + width, y, z + depth)
        glVertex3f(x, y, z + depth)

        # Back face
        glVertex3f(x, y + height, z)
        glVertex3f(x + width, y + height, z)
        glVertex3f(x + width, y + height, z + depth)
        glVertex3f(x, y + height, z + depth)

        # Left face
        glVertex3f(x, y, z)
        glVertex3f(x, y + height, z)
        glVertex3f(x, y + height, z + depth)
        glVertex3f(x, y, z + depth)

        # Right face
        glVertex3f(x + width, y, z)
        glVertex3f(x + width, y + height, z)
        glVertex3f(x + width, y + height, z + depth)
        glVertex3f(x + width, y, z + depth)
        glEnd()
        
    def drawPlatform(self, x, platform_height, z, width, height, depth):
        """
        Función que dibuja la plataforma del montacargas en el espacio tridimensional con las dimensiones especificadas.
        
        Parámetros:
        - self: Instancia de la clase.
        - x: Posición de la plataforma en el eje x.
        - platform_height: altura de la plataforma para las animaciones.
        - z: Posición de la plataforma en el eje z.
        - width: Ancho de la plataforma.
        - height: Altura de la plataforma.
        - depth: Profundidad de la plataforma.
        
        Retorna:
        No hay valor de retorno.
        """
        glPushMatrix()
        glColor3f(0.925, 0.19, 0.03)
        glTranslatef(0, platform_height, 0)
        glBegin(GL_QUADS)
        
        # Bottom face
        glVertex3f(x, 0, z)
        glVertex3f(x + width, 0, z)
        glVertex3f(x + width, 0 + height, z)
        glVertex3f(x, 0 + height, z)

        # Top face
        glVertex3f(x, 0, z + depth)
        glVertex3f(x + width, 0, z + depth)
        glVertex3f(x + width, 0 + height, z + depth)
        glVertex3f(x, 0 + height, z + depth)

        # Front face
        glVertex3f(x, 0, z)
        glVertex3f(x + width, 0, z)
        glVertex3f(x + width, 0, z + depth)
        glVertex3f(x, 0, z + depth)

        # Back face
        glVertex3f(x, 0 + height, z)
        glVertex3f(x + width, 0 + height, z)
        glVertex3f(x + width, 0 + height, z + depth)
        glVertex3f(x, 0 + height, z + depth)

        # Left face
        glVertex3f(x, 0, z)
        glVertex3f(x, 0 + height, z)
        glVertex3f(x, 0 + height, z + depth)
        glVertex3f(x, 0, z + depth)

        # Right face
        glVertex3f(x + width, 0, z)
        glVertex3f(x + width, 0 + height, z)
        glVertex3f(x + width, 0 + height, z + depth)
        glVertex3f(x + width, 0, z + depth)
        glEnd()
        glPopMatrix()

    def drawCylinder(self, x, y, z, radius, height, orientation, slices=30):
        """
        Función que dibuja un cilindro en el espacio tridimensional con las dimensiones y orientación especificadas.
        
        Parámetros:
        - self: Instancia de la clase.
        - x: Posición del cilindro en el eje x.
        - y: Posición del cilindro en el eje y.
        - z: Posición del cilindro en el eje z.
        - radius: radio de la base del cilindro.
        - height: altura del cilindro.
        - orientation: eje en el que se orientará el cilindro.
        - slices: número de pedazos para dibujar el cilindro.
        
        Retorna:
        No hay valor de retorno.
        """
        
        slices = int(slices)
        glBegin(GL_QUAD_STRIP)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(slices + 1):
            angle = 2 * math.pi * i / slices

            if orientation == 'x':
                dx, dy, dz = 0, radius * math.cos(angle), radius * math.sin(angle)
                glVertex3f(x + dx, y + dy, z + dz)
                glVertex3f(x + dx + height, y + dy, z + dz)
            elif orientation == 'y':
                dx, dy, dz = radius * math.cos(angle), 0, radius * math.sin(angle)
                glVertex3f(x + dx, y + dy, z + dz)
                glVertex3f(x + dx, y + dy + height, z + dz)
            elif orientation == 'z':
                dx, dy, dz = radius * math.cos(angle), radius * math.sin(angle), 0
                glVertex3f(x + dx, y + dy, z + dz)
                glVertex3f(x + dx, y + dy, z + dz + height)
            else:
                raise ValueError("Invalid orientation. Use 'x', 'y', or 'z'.")
        glEnd()            

        # Draw the top and bottom faces
        glBegin(GL_POLYGON)
        for i in range(slices + 1):
            angle = 2 * math.pi * i / slices

            if orientation == 'x':
                dx, dy, dz = 0, radius * math.cos(angle), radius * math.sin(angle)
            elif orientation == 'y':
                dx, dy, dz = radius * math.cos(angle), 0, radius * math.sin(angle)
            elif orientation == 'z':
                dx, dy, dz = radius * math.cos(angle), radius * math.sin(angle), 0

            glVertex3f(x + dx, y + dy, z + dz)
        glEnd()

        glBegin(GL_POLYGON)
        for i in range(slices + 1):
            angle = 2 * math.pi * i / slices

            if orientation == 'x':
                dx, dy, dz = 0, radius * math.cos(angle), radius * math.sin(angle)
                glVertex3f(x + dx + height, y + dy, z + dz)
            elif orientation == 'y':
                dx, dy, dz = radius * math.cos(angle), 0, radius * math.sin(angle)
                glVertex3f(x + dx, y + dy + height, z + dz)
            elif orientation == 'z':
                dx, dy, dz = radius * math.cos(angle), radius * math.sin(angle), 0
                glVertex3f(x + dx, y + dy, z + dz + height)
        glEnd()
        
    def drawTruck(self):
        """
        Función que dibuja el montacargas en el espacio tridimensional con sus componentes.
        
        Parámetros:
        - self: Instancia de la clase.
        
        Retorna:
        No hay valor de retorno.
        """
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        
        glScalef(self.scale, self.scale, self.scale)

        angle = math.atan2(self.Direction[0], self.Direction[2]) * (180 / math.pi) 

        glRotatef(angle, 0, 1, 0)
        
        if (self.collided_cube): 
            self.collided_cube.modifyPosition(0, self.altura + (self.collided_cube.radius / 4), 0)

        # Base y techo
        self.drawRectangle(0.0, 1.0, 0.0, 2.0, 1.0, -4.0)
        self.drawRectangle(0.0, 4.0, 0.0, 2.0, 0.5, -2.2)
        
        # Plataforma
        self.drawPlatform(0.0, self.altura, 0.0, 2.0, 0.3, 2.0)
        
        # Pilares
        self.drawCylinder(0.2, 2.0, -0.2, 0.2, 2.0, 'y')
        self.drawCylinder(1.8, 2.0, -0.4, 0.2, 2.0, 'y')
        self.drawCylinder(1.8, 2.0, -2.0, 0.2, 2.0, 'y')
        self.drawCylinder(0.2, 2.0, -2.0, 0.2, 2.0, 'y')
        
        # Ruedas
        self.drawCylinder(-0.5, 1.0, -0.7, 0.5, 0.5, 'z')
        self.drawCylinder(-0.5, 1.0, -3.2, 0.5, 0.5, 'z')
        self.drawCylinder(2.0, 1.0, -0.7, 0.5, 0.5, 'z')
        self.drawCylinder(2.0, 1.0, -3.2, 0.5, 0.5, 'z')
        
        glPopMatrix()