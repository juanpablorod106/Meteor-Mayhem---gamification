import pygame
from personaje import Cubo 
from enemigo import Enemigos
from balas import Bala
from item import Items
#Para instalar la libreria Pygame
#sudo apt install python3-pygame

import random

pygame.init()

pygame.mixer.init()

ANCHO = 1280
ALTO = 640
VENTANA = pygame.display.set_mode([ANCHO,ALTO], pygame.FULLSCREEN) #pygame.FULLSCREEN dentro del segundo parametro de la funcion set_mode que se obtiene mediante los modulos pygame.display 
FPS = 60
FUENTE = pygame.font.SysFont("Blox BRK", 48) 
pygame.display.set_caption('Meteor Mayhem')
SONIDO_BALA = pygame.mixer.Sound("./resources/roblox.wav")
SONIDO_MUERTE = pygame.mixer.Sound("./resources/crash.mp3")

jugando = True

#background = pygame.image.load("./resources/sky.jpg").convert()

reloj = pygame.time.Clock()

tiempo_pasado = 0
tiempo_entre_enemigos = 500
tiempo_entre_items = 5000

vida = 5
puntos = 0

cubo = Cubo(ANCHO/2,ALTO-95)

enemigos = []

balas = []

items = []

ultima_bala = 0
tiempo_entre_balas = 200

ultimo_item = 0

enemigos.append(Enemigos(ANCHO/2, 100))

def crear_bala():  
    global ultima_bala 
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Bala(cubo.rect.centerx -7,cubo.rect.centery))  
        ultima_bala = pygame.time.get_ticks()

def crear_item():
    global ultimo_item
    if pygame.time.get_ticks() - ultimo_item > tiempo_entre_items:
        ultimo_item = pygame.time.get_ticks()
        items.append(Items(random.randint(100, ANCHO-100), random.randint(-1000,-100))) 

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
    crear_item()
    
    texto_nombre = FUENTE.render("Meteor Mayhem", True, "White")
    texto_vida = FUENTE.render(f"LIFE {vida}", True, "White")
    texto_puntos = FUENTE.render(f"PUNTOS {puntos}", True, "White")

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    #VENTANA.blit(background, [0,0])
    cubo.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        if enemigo.vida <= 0:
            enemigos.remove(enemigo)
            SONIDO_MUERTE.play()
            puntos += 3        

        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):   
            print ("COLLISION!!!")
            vida -= 1                        
            print (f"TE HAN QUITADO UNA VIDA, TE QUEDAN {vida} vidas")
            #quit() para cerrar
            enemigos.remove(enemigo)
            tiempo_entre_balas = 200 

        if enemigo.y > ALTO:
            enemigos.remove(enemigo)

        for bala in balas:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigo.vida -= 1 
                balas.remove(bala)
                SONIDO_BALA.play()

    for bala in balas:
        bala.dibujar(VENTANA)
        bala.movimiento()

        if bala.y < 0:
            balas.remove(bala)

    for item in items: 
        item.dibujar(VENTANA)
        item.movimiento()

        if pygame.Rect.colliderect(item.rect, cubo.rect):
            items.remove(item)
            if tiempo_entre_balas >= 200: 
                tiempo_entre_balas -= 50 

        if item.y > ALTO:
            items.remove(item)

    VENTANA.blit(texto_vida, (1120,10))
    VENTANA.blit(texto_nombre, (1000/2,10))
    VENTANA.blit(texto_puntos, (10,10))  

    pygame.display.update()

pygame.quit()

nombre = input("Introduce tu nombre: ")
with open('puntuaciones.txt', 'a') as archivo:
    archivo.write(f"{nombre} - {puntos}\n")