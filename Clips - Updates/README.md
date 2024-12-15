# Meteor-Mayhem---gamification
## Test 1 - 12-12-2024
### Notes
#### Theoretical Framework

In Python, this code snippet defines a special method called __init __ within a class. This method has a very specific function: to initialize the objects of that class.

**def**: *Indicates the beginning of a function definition in Python.*

**__init__**: *Is a magic or dunder (double underscore) method that is automatically executed when a new instance of a class is created (that is, when a new object is created).*

**self**: *Is a reference to the object that is being created. It is used to access the attributes and methods of the object.*

**x and y**: *Are parameters that are passed to the init method when an object is created. These parameters are used to initialize the attributes of the object.*

```
import pygame  
    # The Pygame library is imported to import the video game objects. 
    # In this case this object will be the spaceship and will have x, y as parameters. These belong to the argument of the 
    # method/function __init__.

class Cubo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 10
        self.color = "red"
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        
    def dibujar(self,ventana):
        pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
```
### Class Diagram Example in Python

![Diagram of my class called  Cubo](https://github.com/user-attachments/assets/0691da04-a85b-43fd-a180-1b7b84d3b9c8)


![12-12-2024](https://github.com/user-attachments/assets/a01cb102-7d33-42f5-bc45-0bf1c803e04d)

## Test 2 - 13-12-2024
### Notes
![13-12-2024](https://github.com/user-attachments/assets/273f85f5-67be-40e0-a9c9-cdd43acb8f6a)

## Test 3 - 14-12-2024
### Notes

#### 7.1 [colliderect] es una Función del modulo de rectángulo del modulo pygame se encarga de reconocer choques de instancias de objetos. Con este condicional podemos realizar diversas acciones.

#### 7.2 Accede al bucle de enemigos y elimina al enemigo en caso de que SI halla una colisión.

```
if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
print ("COLLISION!!!")                                      #7.1             
vida -= 1                         
print (f"TE HAN QUITADO UNA VIDA, TE QUEDAN {vida} vidas")   
# Siguiente Linea de codigo:
enemigos.remove(enemigo)                                    #7.2
```
#### 7.3 El bucle del juego funcionara SI tenemos mas de 0 vidas
```
while jugando and vida > 0:
```
### Grafico:
![14-12-2024](https://github.com/user-attachments/assets/9c870273-4b31-4620-b2a0-728141bfdafe)

## Test 4 - 15-12-2024
### Notes

#### 8.1 Importante para el proceso siguiente
```
pygame.init()   #8.1
```
#### 8.2 Se crea la constante de fuente con el modulo [font] de Pygame que nos permitira por medio de una funcion con dos parametros tienen como argumento el nombre de la fuente y su numero.
```
FUENTE = pygame.font.SysFont("Blox BRK", 48)  #8.2
```
#### 8.3 Almacenar en una variable para renderizar texto con nuestra conestante y el metodo render.
```
texto_nombre = FUENTE.render("Meteor Mayhem", True, "White")
texto_vida = FUENTE.render(f"LIFE {vida}", True, "White")      #8.3
texto_puntos = FUENTE.render(f"PUNTOS {puntos}", True, "White")
```
#### 8.4 [blit] sirve como funcion que mostrara en la ventana del juego la instacia del texto, como argumento tiene la instancia de vida y las coordenadas de posicion del texto en la pantalla. 
```
VENTANA.blit(texto_vida, (1120,10))          #8.4
VENTANA.blit(texto_nombre, (1000/2,10))
VENTANA.blit(texto_puntos, (10,10))
``` 
### Grafico
![15-12-2024](https://github.com/user-attachments/assets/845295d7-0cf2-499e-945a-3079d8a27325)