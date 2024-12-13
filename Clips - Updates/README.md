# Meteor-Mayhem---gamification
## Test 1 - 12-12-2024
### Notes
#### Marco Teorico
En Python, este fragmento de código define un método especial llamado __init__ dentro de una clase. Este método tiene una función muy específica: inicializar los objetos de esa clase.

- **def**: *Indica el inicio de una definición de función en Python.*
- **__init__** : *Es un método mágico o dunder (de double underscore) que se ejecuta automáticamente cuando se crea una nueva instancia de una clase (es decir, cuando se crea un nuevo objeto).*
- **self** : *Es una referencia al objeto que se está creando. Se utiliza para acceder a los atributos y métodos del objeto.*
- **x y y** : Son parámetros que se pasan al método __init__ cuando se crea un objeto. Estos parámetros se utilizan para inicializar los atributos del objeto.
    
```Python
import pygame 
    #Se importa la libreria Pygame para importar los objetos del videojuego.
    #En este caso este objeto sera la nave espacial y tendra como parametros x, y. Estos pertenenecen al argumento del
    # metodo/funcion __init__.

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
![12-12-2024](https://github.com/user-attachments/assets/a01cb102-7d33-42f5-bc45-0bf1c803e04d)
## Test 2 - 13-12-2024
### Notes
![13-12-2024](https://github.com/user-attachments/assets/273f85f5-67be-40e0-a9c9-cdd43acb8f6a)
