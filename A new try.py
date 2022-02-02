import pygame
import random
 
class Bloque(pygame.sprite.Sprite):
    """ Esta clase representa al bloque. """
    def __init__(self, color):
        # Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([30, 25])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

    def reset_pos(self):
        
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, 700)
 
    def update(self):
        
        # Move block down one pixel
        self.rect.y += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.reset_pos()
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa al Protagonista. """
     
    def __init__(self):
        """ Configuramos al protagonista. """
        # Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(ORANGE)
 
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Actualiza la ubicación del protagonista. """
        # Obtiene la posición actual del ratón. La devuelve como una lista de 
        # dos números.
        pos = pygame.mouse.get_pos()
     
        # Sitúa la posición x del protagonista en la posición x del ratón
        self.rect.x = pos[0] 
         
class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self):
        #  Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Desplaza al proyectil. """
        self.rect.y -= 3
 
pygame.init()

BLUE = [12, 44, 146]
GREEN = [46, 189, 20]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SALMON = [255, 160, 122]
ORANGE = [234, 73, 27]
BROWN = [64, 39, 31]
GREY = [53, 71, 73]
  
# Initial position of the sheep
rect_x = 50
rect_y = 500
X_offset = 0
 
# Sheep's speed to change
sheep_change_x = 2
sheep_change_y = 2

#My screen
dimensions = [900, 700]
 
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("King Lamoni's floks ")

pygame.mixer.music.load("epic_battle.mp3")
pygame.mixer.music.play()
# Esta es una lista de cada sprite, así como de todos los bloques y del protagonista.

lista_de_todos_los_sprites = pygame.sprite.Group()
 
# Lista de cada bloque en el juego
lista_bloques = pygame.sprite.Group()
 
# Lista de cada proyectil
lista_proyectiles = pygame.sprite.Group()
 
# --- Creamos los sprites
 
for i in range(35):
    # Esto representa un bloque
    bloque = Bloque(BLACK) 
    # Configuramos una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(0, 850)
    bloque.rect.y = random.randrange(0, 150)     
    # Añadimos el bloque a la lista de objetos
    lista_bloques.add(bloque)
    lista_de_todos_los_sprites.add(bloque)
 
# Creamos un bloque protagonista ROJO
protagonista = Protagonista()
lista_de_todos_los_sprites.add(protagonista)

reloj = pygame.time.Clock()
pygame.image.load("colina_arroyo.jpeg")
imagen_defondo = pygame.image.load("colina_arroyo.jpeg").convert()

puntuacion = 0
protagonista.rect.y = 370

# Iteramos hasta que el usuario haga click sobre le botón de salida.
hecho = False
while not hecho:
     
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True 
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Disparamos un proyectil si el usuario presiona el botón del ratón
            proyectil = Proyectil()
            # Configuramos el proyectil de forma que esté donde el protagonista
            proyectil.rect.x = protagonista.rect.x
            proyectil.rect.y = protagonista.rect.y
            # Añadimos el proyectil a la lista
            lista_de_todos_los_sprites.add(proyectil)
            lista_proyectiles.add(proyectil)
        
    # --- Lógica del juego-------  
    
    # Llamamos al método update() en todos los sprites
    lista_de_todos_los_sprites.update()
     
    # Calculamos la mecánica para cada proyectil
    for proyectil in lista_proyectiles:
 
        # Vemos si alcanza a un bloque
        lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil, lista_bloques, True)
         
        # Por cada bloque alcanzado, eliminamos el proyectil y aumentamos la puntuación
        for bloque in lista_bloques_alcanzados:
            lista_proyectiles.remove(proyectil)
            lista_de_todos_los_sprites.remove(proyectil)
            puntuacion += 1
            print( puntuacion )
             
        # Eliminamos el proyectil si vuela fuera de la pantalla
        if proyectil.rect.y < -10:
            lista_proyectiles.remove(proyectil)
            lista_de_todos_los_sprites.remove(proyectil)   
    
    rect_x += sheep_change_x
    rect_y += sheep_change_y
 
    if rect_x > 350 or rect_x < -170:          
        sheep_change_x = sheep_change_x * -1 
    if rect_y > 0 or rect_y < 50:         
        sheep_change_y = sheep_change_y * -1   
        
    screen.blit(imagen_defondo, [0, 0])
       
    x_offset = 0
    while x_offset < 320:
      #Drawing second line sheep
      pygame.draw.ellipse(screen, WHITE, [rect_x + 144+ x_offset, 465 , 80, 50 ])
      pygame.draw.ellipse(screen, WHITE, [rect_x + 190 + x_offset, 459, 60, 30])
      #legs of the sheep 
      pygame.draw.rect(screen, SALMON, [rect_x + 160 + x_offset, 510, 10, 20])
      pygame.draw.rect(screen, SALMON, [rect_x + 172+ x_offset, 512 , 10, 20 ])
      pygame.draw.rect(screen, SALMON, [rect_x + 188+ x_offset, 512 , 10, 20 ])
      pygame.draw.rect(screen, SALMON, [rect_x + 200+ x_offset, 510 , 10, 20 ])
      #face of the sheep 
      pygame.draw.ellipse(screen, SALMON , [rect_x + 217 + x_offset, 460 , 38, 29 ])
      #
      pygame.draw.ellipse(screen, WHITE, [rect_x + 208 + x_offset, 445 , 40, 18])
      #tail 
      pygame.draw.ellipse(screen, WHITE, [rect_x + 135 + x_offset, 470 , 17, 25])
      #eye 
      pygame.draw.ellipse(screen, BLACK, [rect_x + 231+ x_offset, 462 , 7, 9])
      #ear  
      pygame.draw.rect(screen, SALMON , [rect_x + 212+ x_offset, 457, 10, 18])
      #mouth 
      pygame.draw.rect(screen, BLACK , [rect_x + 248 + x_offset, 471 , 7, 3])     
               
      #Drawing first line of sheep
      pygame.draw.ellipse(screen, WHITE, [rect_x + 114+ x_offset, 495 , 80, 50 ])
      pygame.draw.ellipse(screen, WHITE, [rect_x + 160 + x_offset, 489, 60, 30])
      #legs of the sheep 
      pygame.draw.rect(screen, SALMON, [rect_x + 130 + x_offset, 540, 10, 20])
      pygame.draw.rect(screen, SALMON, [rect_x + 142+ x_offset, 542 , 10, 20 ])
      pygame.draw.rect(screen, SALMON, [rect_x + 158+ x_offset, 542 , 10, 20 ])
      pygame.draw.rect(screen, SALMON, [rect_x + 170+ x_offset, 540 , 10, 20 ])
      #face of the sheep
      pygame.draw.ellipse(screen, SALMON , [rect_x + 187 + x_offset, 490 , 38, 29 ])
      #
      pygame.draw.ellipse(screen, WHITE, [rect_x + 178 + x_offset, 475 , 40, 18])
      #tail 
      pygame.draw.ellipse(screen, WHITE, [rect_x + 105 + x_offset, 500 , 17, 25])
      #eye 
      pygame.draw.ellipse(screen, BLACK, [rect_x + 201+ x_offset, 492 , 7, 9])
      #ear  
      pygame.draw.rect(screen, SALMON , [rect_x + 182+ x_offset, 487, 10, 18])
      #mouth 
      pygame.draw.rect(screen, BLACK , [rect_x + 218 + x_offset, 501 , 7, 3])   
                
      x_offset = x_offset + 80 
      
    # Dibujamos todos los sprites
    lista_de_todos_los_sprites.draw(screen)    
        
    pygame.display.flip()
    
    reloj.tick(60)      

pygame.quit()