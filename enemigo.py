import pygame

class Enemigos:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 80
        self.alto = 80
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        self.vida = 3
        self.imagen = pygame.image.load("./resources/Enemigos.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))
        
    def dibujar(self,ventana):
        #pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        ventana.blit(self.imagen,(self.x,self.y))

    def movimiento(self):
        self.y += self.velocidad       