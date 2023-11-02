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

jump = False
jumpCount = 0
jumpMax = 15

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

        if evento.type == pygame.KEYDOWN and pygame.K_UP:
            jump = True
            jumpCount = jumpMax

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT]:
        player.modificar_eje_x(-2)
    if lista_teclas[pygame.K_RIGHT]:
        player.modificar_eje_x(2)
    if lista_teclas[pygame.K_UP]:
        player.isJump = True

    if lista_teclas[pygame.K_ESCAPE]:
        lista_eventos.append[pygame.QUIT]


    jumpMax = 10
    if jump == True:
        player.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False 

    # jumpMax = 10
    # if jump:
    #     y -= jumpCount
    #     if jumpCount > -jumpMax:
    #         jumpCount -= 1
    #     else:
    #         jump = False 



    # VOLCAR CAMBIOS
    ventana_ppal.fill(colores.BLANCO)
    player.actualizar_pantalla(ventana_ppal)
    for dona in lista_donas:
        dona.actualizar_pantalla(ventana_ppal, player)

    pygame.display.flip()

pygame.quit()





