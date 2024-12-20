import pygame
from personaje import Cubo 
from enemigo import Enemigos
from balas import Bala
#Para instalar la libreria Pygame
#sudo apt install python3-pygame

import random

pygame.init()

ANCHO = 1280
ALTO = 640
VENTANA = pygame.display.set_mode([ANCHO,ALTO], pygame.FULLSCREEN) #pygame.FULLSCREEN dentro del segundo parametro de la funcion set_mode que se obtiene mediante los modulos pygame.display 
FPS = 60
FUENTE = pygame.font.SysFont("Blox BRK", 48) 
pygame.display.set_caption('Meteor Mayhem')

jugando = True

reloj = pygame.time.Clock()

tiempo_pasado = 0
tiempo_entre_enemigos = 500

vida = 5
puntos = 0

cubo = Cubo(ANCHO/2,ALTO-95)

enemigos = []

balas = []

ultima_bala = 0
tiempo_entre_balas = 200

enemigos.append(Enemigos(ANCHO/2, 100))

def crear_bala():
    global ultima_bala 
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Bala(cubo.rect.centerx,cubo.rect.centery)) 
        ultima_bala = pygame.time.get_ticks()  

def gestionar_teclas(teclas):   #3.2 Funcion que gestiona el teclado que cambiara la posicion del eje x y y de la instancia Cubo.
    #if teclas[pygame.K_w]:
    #    cubo.y -= cubo.velocidad
    #if teclas[pygame.K_s]:
    #    cubo.y += cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_SPACE]:
        crear_bala()
    if teclas[pygame.K_ESCAPE]:
        exit()

while jugando and vida > 0:

    tiempo_pasado += reloj.tick(FPS)
    """print(tiempo_pasado)
    #Asi podemos ver el reloj en milisegundos en la consola
    """

    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigos(random.randint(0,ANCHO),100)) 
        tiempo_pasado = 0

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()  # 3.1 Variable que almacena el modulo principal de la libreria que accede a    
    gestionar_teclas(teclas)           #otro modulo de la misma para luego desde ese modulo acceder a la funcion get_pressed.
                                       #Esta variable tiene como objetivo servir como argumento de una funcion que va a gestionar las teclas de los objetos 
   
    texto_nombre = FUENTE.render("Meteor Mayhem", True, "White")
    texto_vida = FUENTE.render(f"LIFE {vida}", True, "White")
    texto_puntos = FUENTE.render(f"PUNTOS {puntos}", True, "White")

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):   
            print ("COLLISION!!!")
            vida -= 1                        
            print (f"TE HAN QUITADO UNA VIDA, TE QUEDAN {vida} vidas")
            #quit() para cerrar
            enemigos.remove(enemigo) 

        if enemigo.y + enemigo.alto > ALTO:
            enemigos.remove(enemigo)
            puntos += 1 

        for bala in balas:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigos.remove(enemigo)
                balas.remove(bala)
                puntos += 1

    for bala in balas:
        bala.dibujar(VENTANA)
        bala.movimiento()

    VENTANA.blit(texto_vida, (1120,10))
    VENTANA.blit(texto_nombre, (1000/2,10))
    VENTANA.blit(texto_puntos, (10,10))  


    pygame.display.update()


quit()