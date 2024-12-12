import pygame
import pygame.display
from personaje import Cubo 

#Para instalar la libreria Pygame
#sudo apt install python3-pygame

ANCHO = 1280
ALTO = 720
VENTANA = pygame.display.set_mode([ANCHO,ALTO])
pygame.display.set_caption('Meteor Mayhem')

jugando = True

cubo = Cubo(100,100)

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
    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestionar_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    pygame.display.update()

quit()