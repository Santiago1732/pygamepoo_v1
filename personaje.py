import pygame
import colores

class Personaje:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("01.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_homero = pygame.Rect(x, y, ancho, alto)
        self.rect_boca = pygame.Rect((x + ancho / 2) - 10, y + 90, 40, 20)
        self.score = 0

    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_homero)

    def update(self, incremento_x):
        nueva_x = self.rect_homero.x + incremento_x
        if 0 < nueva_x < 600:
            self.rect_homero.x = nueva_x
            self.rect_boca.x = self.rect_boca.x + incremento_x