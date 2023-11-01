import pygame
import colores
from dona import Dona, crear_lista_donas
from personaje import Personaje

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

# TAMANO DE LA VENTANA
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# TITULO DE LA VENTANA
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer, 100)

# CREACION DE ELEMENTOS
player = Personaje(ANCHO_VENTANA / 2, ALTO_VENTANA - 200, 200, 200)
lista_donas = crear_lista_donas(20)

# LOGICA DEL JUEGO
flag_run = True
while flag_run:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == timer:
            for dona in lista_donas:
                dona.update()

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT]:
        player.update(-2)
    if lista_teclas[pygame.K_RIGHT]:
        player.update(2)

    # VOLCAR CAMBIOS
    ventana_ppal.fill(colores.BLANCO)
    player.actualizar_pantalla(ventana_ppal)
    for dona in lista_donas:
        dona.actualizar_pantalla(ventana_ppal, player)

    pygame.display.flip()

pygame.quit()





