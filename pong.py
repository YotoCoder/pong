import pygame
import sys
from pygame.locals import *
from random import randint


class app():

    def __init__(self):
        ancho = 400
        alto = 400
        vidas = 3
        level = 1
        framerate = 140
        salir = False
        premiocontador = 0
        pygame.init()
        pygame.display.set_caption('Pong')
        ventana = pygame.display.set_mode((ancho, alto))
        color = (0, 255, 40)
        x = 200
        y = 380
        xPos = randint(0, 400)
        yPos = 0
        sentido = {'y': 'bajando', 'x': 'izquierda'}
        frameloop = pygame.time.Clock()
        velocidadJugador = 2
        velocidadPelota = 1
        listaladrillos = []
        listaPremios = []
        miFuente = pygame.font.SysFont('Arial', 14)

        class ladrillo:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def dibujar(self):
                self.ladrillo = pygame.draw.rect(
                    ventana, (255, 100, 100), (self.x, self.y, 30, 10))

        class premio:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def dibujar(self):
                self.premio = pygame.draw.rect(
                    ventana, (0, 255, 255), (self.x, self.y, 10, 10))

        def level1():
            map1x = [10, 130, 240, 350]
            map1y = [80, 100, 120]

            for i in map1x:
                for j in map1y:
                    listaladrillos.append(ladrillo(i, j))

        def level2():
            map1x = [10, 130, 240, 350]
            map1y = [80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

            for i in map1x:
                for j in map1y:
                    listaladrillos.append(ladrillo(i, j))

        def level3():
            map1x = [10, 80, 130, 200, 250, 298, 350]
            map1y = [60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

            for i in map1x:
                for j in map1y:
                    listaladrillos.append(ladrillo(i, j))

        def level4():
            map1x = [10, 50, 90, 130, 170, 250, 290, 330, 368]
            map1y = [40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

            for i in map1x:
                for j in map1y:
                    listaladrillos.append(ladrillo(i, j))

        def level5():
            map1x = [10, 50, 90, 130, 170, 250, 290, 330, 368]
            map1y = [20, 40, 60, 80, 100, 120, 140, 160, 180,
                     200, 220, 240, 260, 280, 300, 320, 340, 360,]

            for i in map1x:
                for j in map1y:
                    listaladrillos.append(ladrillo(i, j))

        while True:
            frameloop.tick(framerate)
            ventana.fill((0, 0, 0))
            miTexto = miFuente.render('Vidas: ' + str(vidas), 1, color)
            ventana.blit(miTexto, (345, 0))
            miTexto = miFuente.render('Level: '+ str(level-1), 1, color)
            ventana.blit(miTexto, (345, 20))
            player1 = pygame.draw.rect(ventana, color, (x, y, 50, 10))
            pelota = pygame.draw.rect(ventana, color, (xPos, yPos, 10, 10))

            if len(listaladrillos) == 0:
                if level == 1:
                    level1()
                    level = 2
                    yPos = 0
                    framerate += 20
                elif level == 2:
                    level = 3
                    level2()
                    yPos = 0
                    framerate += 20
                elif level == 3:
                    level = 4
                    level3()
                    yPos = 0
                    framerate += 20
                elif level == 4:
                    level = 5
                    level4()
                    yPos = 0
                    framerate += 20
                elif level == 5:
                    level = 6
                    level5()
                    yPos = 0
                    framerate += 20
                elif level == 6:
                    vidas = 0
                    yPos = 450

            for l in listaladrillos:
                l.dibujar()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[K_LEFT]:
                x -= velocidadJugador
                if x <= -1:
                    x = 0
            if keys[K_RIGHT]:
                x += velocidadJugador
                if x >= 350:
                    x = 350
            if player1.colliderect(pelota):
                if keys[K_RIGHT]:
                    sentido['x'] = 'derecha'
                    sentido['y'] = 'subiendo'
                elif keys[K_LEFT]:
                    sentido['x'] = 'izquierda'
                    sentido['y'] = 'subiendo'
                else:
                    sentido['y'] = 'subiendo'
            if sentido['y'] == 'bajando':
                yPos += velocidadPelota
            elif sentido['y'] == 'subiendo':
                yPos -= velocidadPelota
            if yPos <= 0:
                sentido['y'] = 'bajando'
            if xPos <= 0:
                sentido['x'] = 'derecha'
            elif xPos >= 400:
                sentido['x'] = 'izquierda'
            if sentido['x'] == 'izquierda':
                xPos -= velocidadPelota
            elif sentido['x'] == 'derecha':
                xPos += velocidadPelota

            for l in listaladrillos:

                if pelota.colliderect(l.ladrillo):

                    premiocontador += 1

                    if l.ladrillo.bottom == pelota.top+1:
                        sentido['y'] = 'bajando'
                        listaladrillos.remove(l)
                    elif l.ladrillo.top == pelota.bottom-1:
                        sentido['y'] = 'subiendo'
                        listaladrillos.remove(l)
                    elif l.ladrillo.right == pelota.left + 1:
                        sentido['x'] = 'derecha'
                        listaladrillos.remove(l)
                    elif l.ladrillo.left == pelota.right - 1:
                        sentido['x'] = 'izquierda'
                        listaladrillos.remove(l)

            if yPos > 400:
                vidas -= 1
                yPos = 0

                if vidas <= 0:
                    while salir != True:
                        ventana.fill((0, 0, 0))
                        fuente = pygame.font.SysFont('Arial', 30)
                        miTexto = fuente.render(
                            '- Para salir presione "S"', 0, color)
                        miTexto1 = fuente.render(
                            '- Para reiniciar presione "R"', 0, (255, 0, 0))
                        ventana.blit(miTexto, (60, 160))
                        ventana.blit(miTexto1, (60, 200))
                        keys = pygame.key.get_pressed()

                        if keys[K_s]:
                            pygame.quit()
                            sys.exit()

                        elif keys[K_r]:
                            app()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()

            if premiocontador == 20 or premiocontador == 40:
                listaPremios.append(premio(pelota.x, pelota.y))
                premiocontador = 21

            for p in listaPremios:
                p.dibujar()
                p.y += 0.4

                if p.y > 400:
                    listaPremios.remove(p)

                if p.premio.colliderect(player1):
                    vidas += 1
                    listaPremios.remove(p)

            pygame.display.update()

app()