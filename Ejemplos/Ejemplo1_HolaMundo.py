# Importamos la biblioteca gráfica
import pygame
# Importamos las definiciones locales
from pygame.locals import *

# Iniciamos PyGame
pygame.init()

# Configuramos el tamaño de la pantalla (ventana mejor dicho)
screen_width = 900
screen_height = 600

# Iniciamos La pantalla con los tamaños, doble buffer y opengl
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

# Poedmos cambiar el título
pygame.display.set_caption("OpenGL en Python")

# Variable de control del bucle gráfico
done = False
while not done:
    # Procesamiento de las entradas
    for event in pygame.event.get():
        # El botón de salir finaliza el bucle
        if event.type == pygame.QUIT:
            done = True
    
    # Copiamos el contenido renderizado al segundo buffer
    pygame.display.flip()
    # Esperamos unos milisegundos para no saturar el procesador
    pygame.time.wait(100)

# Finalmente salimos de PyGame
pygame.quit()