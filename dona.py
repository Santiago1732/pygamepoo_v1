import pygame
import colores
import random

class Dona:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("00.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.visible = True
        self.speed = random.randrange(10, 20, 1)

    def update(self):
        self.rect.y += self.speed

    def actualizar_pantalla(self, ventana_ppal, personaje):
        if personaje.rect_boca.colliderect(self.rect):
            personaje.score += 1
            self.reiniciar()

        if self.rect.y > 800:
            self.reiniciar()

        ventana_ppal.blit(self.surface, self.rect)

    def reiniciar(self):
        self.rect.x = random.randrange(0, 740, 60)
        self.rect.y = random.randrange(-1000, 0, 60)

def crear_lista_donas(cantidad):
    lista_donas = []
    for _ in range(cantidad):
        y = random.randrange(-1000, 0, 60)
        x = random.randrange(0, 740, 60)
        dona = Dona(x, y, 60, 60)
        lista_donas.append(dona)
    return lista_donas