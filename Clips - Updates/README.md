# Meteor-Mayhem---gamification
## Test 1 - 12-12-2024
### Notes
#### Theoretical Framework

In Python, this code snippet defines a special method called init within a class. This method has a very specific function: to initialize the objects of that class.

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
![12-12-2024](https://github.com/user-attachments/assets/a01cb102-7d33-42f5-bc45-0bf1c803e04d)
## Test 2 - 13-12-2024
### Notes
![13-12-2024](https://github.com/user-attachments/assets/273f85f5-67be-40e0-a9c9-cdd43acb8f6a)
