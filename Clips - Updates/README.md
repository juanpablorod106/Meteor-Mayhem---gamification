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

#### 7.2 Accede al bucle de enemigos y elimina al enemigo en caso de que SI haya una colisión.

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
### Grafico:
![15-12-2024](https://github.com/user-attachments/assets/845295d7-0cf2-499e-945a-3079d8a27325)

## Test 5 - 16-12-2024
### Notes

Para darle logica a la suma de puntos debemos crear una condicional que incluya la variable "puntos" donde
los puntos suban bajo alguna logica. En este periodo se implemento que al momento de salir enemigos de la ventana se sube un punto.

#### 9.1 Si la posicion del enemigo es mayor al alto de la ventana.
##### 9.1.1 nos suma puntos.
##### 9.1.2 En lo que se elmine/desaparezca un enemigo nos suma un punto.

```
if enemigo.y + enemigo.alto > ALTO: #9.1
    puntos += 1   #9.1.1
    enemigos.remove(enemigo) #9.1.2
```

### 10 - Creacion de clases de balas.
Crearemos un objeto/clase que sera la bala, mas pequena, lenta y de otro color a los otros objetos.
Esta objeto se disparara desde nuestro cubo.

Para disparar este objeto, necesitaremos:
- 10.1 Clase de las balas;
- 10.2 Una lista de balas;
- 10.3 Una funcion para crearlas/dispararlas;
- 10.4 Darle una tecla a las balas para ser disparadas;
- 10.5 Un bucle donde dibujarlas en la ventana del juego.

### 10.1 Clase de las balas

#### 10.1.1 Se crea el objeto, la clase bala, con los argumentos de posicion x,y, y el resto de atributos (self).
#### 10.1.2 El ancho y el alto de las balas es mas pequeno que los anteriores objetos.
#### 10.1.3 Se resta el eje vertical (self.y) con la velocidad para que la bala vaya hacia arriba.

```
class Bala:                       #10.1.1
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20            #10.1.2
        self.velocidad = 10
        self.color = "white"
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)
        
    def dibujar(self,ventana):
        pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.alto)

    def movimiento(self):
        self.y -= self.velocidad  #10.1.3
```
### Class Diagram Example in Python
![Captura desde 2024-12-16 16-31-37](https://github.com/user-attachments/assets/c5a90521-9cb8-4bc7-8272-9f0f84250025)

### 10.2 Lista de balas

#### 10.2.1 Creamos una variable que contenga una lista de balas.
```
balas = [] #10.2.1
```
### 10.3 Una funcion para crearlas;

#### 10.3.1 Creamos una funcion para disparar balas.
#### 10.3.2 Nuestra lista de balas usara el metodo append para almacenar el argumento de posicion de la clase bala que en este caso sera el centro de los dos ejes de posicion del cubo.
```
def crear_bala():                                               #10.3.1
    balas.append(Bala(cubo.rect.centerx,cubo.rect.centery))     #10.3.2
```
### 10.4 Darle una tecla a las balas para ser disparadas;

#### 10.4.1 Asignamos la tecla espacio para ejecutar nuestra funcion [crear_bala]. Esto dentro de nuestra funcion de gestionar teclas con el parametro teclas [gestionar_teclas(teclas)].
```
if teclas[pygame.K_SPACE]:
crear_bala()                    #10.4.1
```
### 10.5 Un bucle donde dibujarlas en la ventana del juego.

#### 10.5.1 Creamos un bucle para generar las balas.
#### 10.5.2 Y las dibujamos en la ventana del juego.
```
for bala in balas:          #10.5.1
    bala.dibujar(VENTANA)   #10.5.2
    bala.movimiento()
```
### Grafico:
![16-12-2024](https://github.com/user-attachments/assets/02156275-9541-4f95-8370-03bd577eb3be)
