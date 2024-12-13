import pygame
import pygame.display
from personaje import Cubo 
from enemigo import Enemigos
#Para instalar la libreria Pygame
#sudo apt install python3-pygame

import random

ANCHO = 1280
ALTO = 640
VENTANA = pygame.display.set_mode([ANCHO,ALTO], pygame.FULLSCREEN)
FPS = 60
pygame.display.set_caption('Meteor Mayhem')

jugando = True

reloj = pygame.time.Clock()

tiempo_pasado = 0
tiempo_entre_enemigos = 500


cubo = Cubo(ANCHO/2,ALTO-50)

enemigos = []

enemigos.append(Enemigos(ANCHO/2, 100))


def gestionar_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad   

while jugando:

    tiempo_pasado += reloj.tick(FPS)
    """print(tiempo_pasado)
    #Asi podemos ver el reloj en milisegundos en la consola
    """

    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigos(random.randint(0,ANCHO),100)) 
        tiempo_pasado = 0

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestionar_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()
    pygame.display.update()

quit()