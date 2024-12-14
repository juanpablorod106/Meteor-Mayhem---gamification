import pygame
import pygame.display
from personaje import Cubo 
from enemigo import Enemigos
#Para instalar la libreria Pygame
#sudo apt install python3-pygame

import random

ANCHO = 1280
ALTO = 640
VENTANA = pygame.display.set_mode([ANCHO,ALTO], pygame.FULLSCREEN) #pygame.FULLSCREEN dentro del segundo parametro de la funcion set_mode que se obtiene mediante los modulos pygame.display 
FPS = 60
pygame.display.set_caption('Meteor Mayhem')

jugando = True

reloj = pygame.time.Clock()

tiempo_pasado = 0
tiempo_entre_enemigos = 500

vida = 5
puntos = 0

cubo = Cubo(ANCHO/2,ALTO-75)

enemigos = []

enemigos.append(Enemigos(ANCHO/2, 100))


def gestionar_teclas(teclas):   # 3.2 Funcion que gestiona el teclado que cambiara la posicion del eje x y y de la instancia Cubo
    #if teclas[pygame.K_w]:
    #    cubo.y -= cubo.velocidad
    #if teclas[pygame.K_s]:                    
    #    cubo.y += cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad   

while jugando and vida > 0: #7.3 El bluce del juego funcionara SI tenemos mas de 0 vidas

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
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        if pygame.Rect.colliderect(cubo.rect, enemigo.rect): #7.1 Funcion del modulo de rectangulo del modulo pygame se encarga  
            print ("COLLISION!!!")                           #de reconocer choques de instancias de objetos. Con este condicional podemos realizar diversas acciones.
            vida -= 1                        
            print (f"TE HAN QUITADO UNA VIDA, TE QUEDAN {vida} vidas")
            #quit() para cerrar
            enemigos.remove(enemigo) #7.2 Accede al bucle de enemigos y elimina al enemigo en caso de que SI haya una collision

    pygame.display.update()


quit()