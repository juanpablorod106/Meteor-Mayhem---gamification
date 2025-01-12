import pygame

class Bala:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 15
        self.alto = 50
        self.velocidad = 40
        self.color = "white"
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        self.imagen = pygame.image.load("./resources/Bala.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))
        
    def dibujar(self,ventana):
        #pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        ventana.blit(self.imagen,(self.x,self.y))

    def movimiento(self):
        self.y -= self.velocidad