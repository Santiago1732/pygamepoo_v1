import pygame
import colores

class Personaje:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("01.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_homero = pygame.Rect(x, y, ancho, alto)
        self.rect_boca = pygame.Rect((x + ancho / 2) - 10, y + 90, 40, 20)
        self.score = 0
        self.isJump = False
        self.y = y

    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_homero)

    def modificar_eje_x(self, incremento_x):
        nueva_x = self.rect_homero.x + incremento_x
        if 0 < nueva_x < 600:
            self.rect_homero.x = nueva_x
            self.rect_boca.x = self.rect_boca.x + incremento_x

    def modificar_eje_y(self, incremento_y):
        nueva_y = self.rect_homero.y + incremento_y
        if 0 < nueva_y < 600:
            self.rect_homero.y = nueva_y
            self.rect_boca.y = self.rect_boca.y + incremento_y

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.rect_homero.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10        