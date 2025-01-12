import pygame

class Items:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 40 #14.1.1
        self.alto = 40
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        self.imagen = pygame.image.load("./resources/item.png") #14.1.2
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))
        
    def dibujar(self,ventana):
        #pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        ventana.blit(self.imagen,(self.x,self.y))

    def movimiento(self):
        self.y += self.velocidad