import pygame

class Cubo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 80
        self.alto = 80
        self.velocidad = 10
        self.color = "red"
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        self.imagen = pygame.image.load("./resources/personaje.png") #13.1.1
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto)) #13.1.2  
  
    def dibujar(self,ventana):
        #pygame.draw.rect(ventana, self.color, self.rect) #13.1.4
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        ventana.blit(self.imagen,(self.x,self.y)) #13.1.3
