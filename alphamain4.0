import pygame as pg
import serial
import random
import time
import math
import sys

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
clock = pg.time.Clock()
running = True

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
orange = (255, 100, 10)
yellow = (255, 255, 0)
blue_green = (0, 255, 170)
marroon = (115, 0, 0)
lime = (180, 255, 100)
pink = (255, 100, 180)
purple = (240, 0, 255)
gray = (127, 127, 127)
magenta = (255, 0, 230)
brown = (100, 40, 0)
forest_green = (0, 50, 0)
navy_blue = (0, 0, 100)
rust = (210, 150, 75)
dandilion_yellow = (255, 200, 0)
highlighter = (255, 255, 100)
sky_blue = (0, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (50, 50, 50)
tan = (230, 220, 170)
coffee_brown = (200, 190, 140)
moon_glow = (235, 245, 255)

sveboje = [
    white,
    blue,
    green,
    red,
    black,
    orange,
    yellow,
    blue_green,
    marroon,
    lime,
    pink,
    purple,
    gray,
    magenta,
    brown,
    forest_green,
    navy_blue,
    rust,
    dandilion_yellow,
    highlighter,
    sky_blue,
    light_gray,
    dark_gray,
    tan,
    coffee_brown,
    moon_glow,
]


class MainMenu:
    def DrawMainMenu(self):
        font = pg.font.Font("freesansbold.ttf", 100)
        font2 = pg.font.Font("freesansbold.ttf", 50)
        ##mouse position
        mpos = pg.mouse.get_pos()

        ##Tilte
        textS = font.render("Schizo fighting", True, "Black")
        RectS = textS.get_rect()
        RectS.center = (960, 100)
        screen.blit(textS, RectS)

        ##settings
        pg.draw.rect(screen, "black", (30, 200, 500, 780), 10, 25)
        pg.draw.rect(screen, "black", (30, 200, 500, 150), 0, 25)
        textS = font.render("Settings", True, "white")
        RectS = textS.get_rect()
        RectS.center = (280, 275)
        screen.blit(textS, RectS)

        ##leaderboard
        pobednici = ["Igrac 1", "Igrac 2", "Igrac 3", "Igrac 4", "Igrac 5"]
        pobede = [str(5), str(4), str(3), str(2), str(1)]
        pg.draw.rect(screen, "black", (1390, 200, 500, 780), 10, 25)
        pg.draw.rect(screen, "black", (1390, 200, 500, 150), 0, 25)
        textW = font.render("Most win", True, "white")
        RectW = textW.get_rect()
        RectW.center = (1640, 275)
        screen.blit(textW, RectW)

        pg.draw.rect(screen, "gray", (1765, 365, 100, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1765, 480, 100, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1765, 595, 100, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1765, 710, 100, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1765, 825, 100, 100), 0, 25)

        pg.draw.rect(screen, "gray", (1500, 365, 250, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1500, 480, 250, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1500, 595, 250, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1500, 710, 250, 100), 0, 25)
        pg.draw.rect(screen, "gray", (1500, 825, 250, 100), 0, 25)

        ## pobednici
        textP1 = font2.render(pobednici[0], True, "Black")
        RectP1 = textP1.get_rect()
        RectP1.center = (1625, 415)
        screen.blit(textP1, RectP1)
        textP2 = font2.render(pobednici[1], True, "Black")
        RectP2 = textP2.get_rect()
        RectP2.center = (1625, 530)
        screen.blit(textP2, RectP2)
        textP3 = font2.render(pobednici[2], True, "Black")
        RectP3 = textP3.get_rect()
        RectP3.center = (1625, 645)
        screen.blit(textP3, RectP3)
        textP4 = font2.render(pobednici[3], True, "Black")
        RectP4 = textP4.get_rect()
        RectP4.center = (1625, 760)
        screen.blit(textP4, RectP4)
        textP5 = font2.render(pobednici[4], True, "Black")
        RectP5 = textP5.get_rect()
        RectP5.center = (1625, 875)
        screen.blit(textP5, RectP5)

        ## broj pobeda
        textW1 = font.render(pobede[0], True, "Black")
        RectW1 = textW1.get_rect()
        RectW1.center = (1815, 415)
        screen.blit(textW1, RectW1)
        textW2 = font.render(pobede[1], True, "Black")
        RectW2 = textW2.get_rect()
        RectW2.center = (1815, 530)
        screen.blit(textW2, RectW2)
        textW3 = font.render(pobede[2], True, "Black")
        RectW3 = textW3.get_rect()
        RectW3.center = (1815, 645)
        screen.blit(textW3, RectW3)
        textW4 = font.render(pobede[3], True, "Black")
        RectW4 = textW4.get_rect()
        RectW4.center = (1815, 760)
        screen.blit(textW4, RectW4)
        textW5 = font.render(pobede[4], True, "Black")
        RectW5 = textW5.get_rect()
        RectW5.center = (1815, 875)
        screen.blit(textW5, RectW5)

        text1 = font.render("1.", True, "Black")
        Rect1 = text1.get_rect()
        Rect1.topleft = (1410, 365)
        screen.blit(text1, Rect1)
        text2 = font.render("2.", True, "Black")
        Rect2 = text2.get_rect()
        Rect2.topleft = (1410, 480)
        screen.blit(text2, Rect2)
        text3 = font.render("3.", True, "Black")
        Rect3 = text3.get_rect()
        Rect3.topleft = (1410, 595)
        screen.blit(text3, Rect3)
        text4 = font.render("4.", True, "Black")
        Rect4 = text4.get_rect()
        Rect4.topleft = (1410, 710)
        screen.blit(text4, Rect4)
        text5 = font.render("5.", True, "Black")
        Rect5 = text5.get_rect()
        Rect5.topleft = (1410, 825)
        screen.blit(text5, Rect5)

        ##play, singleplayer, credits, quit game
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 390 and mpos[1] >= 250:
            pg.draw.rect(screen, "gray", (560, 250, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 250, 800, 140), 0, 25)
        textP = font.render("Play", True, "white")
        RectP = textP.get_rect()
        RectP.center = (960, 320)
        screen.blit(textP, RectP)

        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 560 and mpos[1] >= 420:
            pg.draw.rect(screen, "gray", (560, 420, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 420, 800, 140), 0, 25)
        textI = font.render("Singleplayer", True, "white")
        RectI = textI.get_rect()
        RectI.center = (960, 490)
        screen.blit(textI, RectI)

        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 730 and mpos[1] >= 590:
            pg.draw.rect(screen, "gray", (560, 590, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 590, 800, 140), 0, 25)
        textC = font.render("Credits", True, "white")
        RectC = textC.get_rect()
        RectC.center = (960, 660)
        screen.blit(textC, RectC)

        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 900 and mpos[1] >= 760:
            pg.draw.rect(screen, "gray", (560, 760, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 760, 800, 140), 0, 25)
        textQ = font.render("Quit Game", True, "white")
        RectQ = textQ.get_rect()
        RectQ.center = (960, 830)
        screen.blit(textQ, RectQ)

    def DetectClicks(self):
        mpos = pg.mouse.get_pos()
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 390 and mpos[1] >= 250:
            self.R = True
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 560 and mpos[1] >= 420:
            self.R = True
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 730 and mpos[1] >= 590:
            self.R = True
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 900 and mpos[1] >= 760:
            self.R = True


MainMenu = MainMenu()
# MAIN MENU
screen_info = pg.display.Info()
MAXW = screen_info.current_w
MAXH = screen_info.current_h
W = screen_info.current_w
H = screen_info.current_h

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                MainMenu.DetectClicks()
                if MainMenu.R:
                    running = False

    screen.fill("white")

    MainMenu.DrawMainMenu()

    pg.display.update()

    clock.tick(60)


# SKIN SELECTOR KOD


screen.fill((0, 0, 0))


running = True


class Character:
    def __init__(self, HP, skin, name, poz):
        self.HP = HP
        self.skin = skin
        self.name = name
        self.poz = poz



font = pg.font.Font(None, 54)


def formatiraj(tacka, offset, multi):
    return offset + multi * tacka


def rot(x, y, teta):
    return (
        (x * math.cos(teta * math.pi / 180) - y * math.sin(teta * math.pi / 180)),
        (x * math.sin(teta * math.pi / 180) + y * math.cos(teta * math.pi / 180)),
    )


def nacrtajstrelicu(boja, ox, oy, m, teta):
    a = []
    a.append(rot(0, 0, teta))
    a.append(rot(-3, 3, teta))
    a.append(rot(-1, 3, teta))
    a.append(rot(-1, 6, teta))
    a.append(rot(1, 6, teta))
    a.append(rot(1, 3, teta))
    a.append(rot(3, 3, teta))
    a.append(rot(0, 0, teta))
    pg.draw.polygon(
        screen,
        boja,
        [
            (formatiraj(a[0][0], ox, m), formatiraj(a[0][1], oy, m)),
            (formatiraj(a[1][0], ox, m), formatiraj(a[1][1], oy, m)),
            (formatiraj(a[2][0], ox, m), formatiraj(a[2][1], oy, m)),
            (formatiraj(a[3][0], ox, m), formatiraj(a[3][1], oy, m)),
            (formatiraj(a[4][0], ox, m), formatiraj(a[4][1], oy, m)),
            (formatiraj(a[5][0], ox, m), formatiraj(a[5][1], oy, m)),
            (formatiraj(a[6][0], ox, m), formatiraj(a[6][1], oy, m)),
            (formatiraj(a[7][0], ox, m), formatiraj(a[7][1], oy, m)),
        ],
    )


def nacrtajstrelicu2(boja, ox, oy, m, teta, debljina):
    a = []
    a.append(rot(0, 0, teta))
    a.append(rot(-3, 3, teta))
    a.append(rot(-1, 3, teta))
    a.append(rot(-1, 6, teta))
    a.append(rot(1, 6, teta))
    a.append(rot(1, 3, teta))
    a.append(rot(3, 3, teta))
    a.append(rot(0, 0, teta))
    pg.draw.polygon(
        screen,
        boja,
        [
            (formatiraj(a[0][0], ox, m), formatiraj(a[0][1], oy, m)),
            (formatiraj(a[1][0], ox, m), formatiraj(a[1][1], oy, m)),
            (formatiraj(a[2][0], ox, m), formatiraj(a[2][1], oy, m)),
            (formatiraj(a[3][0], ox, m), formatiraj(a[3][1], oy, m)),
            (formatiraj(a[4][0], ox, m), formatiraj(a[4][1], oy, m)),
            (formatiraj(a[5][0], ox, m), formatiraj(a[5][1], oy, m)),
            (formatiraj(a[6][0], ox, m), formatiraj(a[6][1], oy, m)),
            (formatiraj(a[7][0], ox, m), formatiraj(a[7][1], oy, m)),
        ],
        debljina,
    )


def koordi(boja, ox, oy, m, teta):
    a = []
    a.append(rot(0, 0, teta))
    a.append(rot(-3, 3, teta))
    a.append(rot(-1, 3, teta))
    a.append(rot(-1, 6, teta))
    a.append(rot(1, 6, teta))
    a.append(rot(1, 3, teta))
    a.append(rot(3, 3, teta))
    a.append(rot(0, 0, teta))
    vr = []
    for i in range(8):
        vr.append((formatiraj(a[i][0], ox, m), formatiraj(a[i][1], oy, m)))
    return vr


class Strelica:
    def __init__(self, boja, ox, oy, m, teta):
        self.x = ox
        self.y = oy
        self.boja = boja
        self.m = m
        self.speed = 5
        self.teta = teta
        self.staraboja = boja
        self.vertices = koordi(self.boja, self.x, self.y, self.m, self.teta)
        self.g = 0.5

    def update(self):
        nacrtajstrelicu(black, self.x, self.y, self.m, self.teta)
        self.y += self.speed

    def draw(self):
        nacrtajstrelicu(self.boja, self.x, self.y, self.m, self.teta)


# ovde imamo koorde
# strel = [    Strelica(red, 400, 400, 15, 270),
# Strelica(red, 585, 445, 15, 180),
# Strelica(red, 725, 355, 15, 0),
# Strelica(red, 910, 400, 15, 90),
# ]

strel = []


def generisistrelicu():
    koja = random.randint(0, 3)
    i = random.randint(0, len(sveboje) - 1)
    while sveboje[i] == green or sveboje[i] == black or sveboje[i] == white:
        i = random.randint(0, len(sveboje) - 1)
    if koja == 0:
        strel.append(Strelica(sveboje[i], 400, 200, 15, 270))
    elif koja == 1:
        strel.append(Strelica(sveboje[i], 585, 245, 15, 180))
    elif koja == 2:
        strel.append(Strelica(sveboje[i], 725, 155, 15, 0))
    else:
        strel.append(Strelica(sveboje[i], 910, 200, 15, 90))


def clearstarestrelice():
    for st in strel:
        if st.y > 1200:
            strel.remove(st)


def glavnestrelice():
    debljina = 5
    nacrtajstrelicu2(white, 400, 900, 15, 270, debljina)
    nacrtajstrelicu2(white, 585, 945, 15, 180, debljina)
    nacrtajstrelicu2(white, 725, 855, 15, 0, debljina)
    nacrtajstrelicu2(white, 910, 900, 15, 90, debljina)
    # nacrtajstrelicu(black, 400, 900, 15, 270)
    # nacrtajstrelicu(black, 585, 945, 15, 180)
    # nacrtajstrelicu(black, 725, 855, 15, 0)
    # nacrtajstrelicu(black, 910, 900, 15, 90)


def apdejtajskorudobro():
    print("BRAVO!")


def apdejtajskorulose():
    print("LOSE")


def proverizelenekoorde():
    v = True
    for strelica in strel:
        if strelica.x == 400:
            if (strelica.y >= 895) and (strelica.y <= 905):
                strelica.staraboja = strelica.boja
                strelica.boja = green
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        pass
                    else:
                        v = False
                else:
                    v = False
            elif strelica.y > 905:
                strelica.boja = strelica.staraboja
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        v = False
            else:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        v = False

        elif strelica.x == 585:
            if (strelica.y >= 940) and (strelica.y <= 950):
                strelica.staraboja = strelica.boja
                strelica.boja = green
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        # apdejtajskor(1)
                        pass
                    else:
                        v = False
                else:
                    v = False
            elif strelica.y > 950:
                strelica.boja = strelica.staraboja
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        v = False
            else:
                if event.type == pg.KEYDOWN:
                    v = False
        elif strelica.x == 725:
            if (strelica.y >= 850) and (strelica.y <= 860):
                strelica.staraboja = strelica.boja
                strelica.boja = green
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        # apdejtajskor(1)
                        pass
                    else:
                        v = False
            elif strelica.y > 960:
                strelica.boja = strelica.staraboja
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        v = False
            else:
                if event.type == pg.KEYDOWN:
                    v = False
        else:
            if (strelica.y >= 895) and (strelica.y <= 905):
                strelica.staraboja = strelica.boja
                strelica.boja = green
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        # apdejtajskor(1)
                        pass
                    else:
                        v = False
                else:
                    v = False
            elif strelica.y > 905:
                strelica.boja = strelica.staraboja
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        v = False
                        pass
            else:
                if event.type == pg.KEYDOWN:
                    v = False

                    # -z je gore, +z je dole, +y je levo, -y je desno

    if v == False:
        # apdejtajskor(0)
        pass


def akcija(kontrole):
    if kontrole[3]:
        apdejtajudobro = False
        for x in strel:
            if x.x == 400:
                if x.y <= 915 and x.y >= 885:
                    apdejtajudobro = True
        if apdejtajudobro:
            apdejtajskorudobro()
        else:
            apdejtajskorulose()

    elif kontrole[1]:
        apdejtajudobro = False
        for x in strel:
            if x.x == 585:
                if x.y <= 960 and x.y >= 930:
                    apdejtajudobro = True
        if apdejtajudobro:
            apdejtajskorudobro()
        else:
            apdejtajskorulose()
    elif kontrole[0]:
        apdejtajudobro = False
        for x in strel:
            if x.x == 725:
                if x.y <= 870 and x.y >= 840:
                    apdejtajudobro = True
        if apdejtajudobro:
            apdejtajskorudobro()
        else:
            apdejtajskorulose()
    elif kontrole[2]:
        apdejtajudobro = False
        for x in strel:
            if x.x == 910:
                if x.y <= 915 and x.y >= 885:
                    apdejtajudobro = True
        if apdejtajudobro:
            apdejtajskorudobro()
        else:
            apdejtajskorulose()


# PLAYER DEF
PLAYER_WIDTH, PLAYER_HEIGHT = 75 / 1200 * W, 75 / 800 * H
PLAYER1_POS = (100 / 1200 * W, H - PLAYER_HEIGHT)
PLAYER2_POS = (W - 100 / 1200 * W - PLAYER_WIDTH, H - PLAYER_HEIGHT)
player1 = Character(
    HP=100, skin="red", name="Player 1", poz=(*PLAYER1_POS, PLAYER_WIDTH, PLAYER_HEIGHT)
)
player2 = Character(
    HP=100,
    skin="white",
    name="Player 2",
    poz=(*PLAYER2_POS, PLAYER_WIDTH, PLAYER_HEIGHT),
)
player1_name_text = font.render(player1.name, True, white)
player2_name_text = font.render(player2.name, True, white)

BAR_WIDTH, BAR_HEIGHT = 320 / 1200 * W, 35 / 800 * H


def drawgore():
    #pg.draw.rect(screen, red, (100 / 1200 * W, 70 / 800 * H, BAR_WIDTH, BAR_HEIGHT))
    #pg.draw.rect(
        #screen,
        #green,
        #(100 / 1200 * W, 70 / 800 * H, BAR_WIDTH * (player1.HP / 100), BAR_HEIGHT),
    #)
    #pg.draw.rect(screen, red, (W - 400 / 1200 * W, 70 / 800 * H, BAR_WIDTH, BAR_HEIGHT))
    #pg.draw.rect(
        #screen,
        #green,
        #(W - 400 / 1200 * W, 70 / 800 * H, BAR_WIDTH * (player2.HP / 100), BAR_HEIGHT),
    #)
    screen.blit(player1_name_text, (100 / 1200 * W, 20 / 800 * H))
    player2_text_width = player2_name_text.get_width()
    screen.blit(
        player2_name_text,
        (W - 400 / 1200 * W + BAR_WIDTH - player2_text_width, 20 / 800 * H),
    )


# ARDUINO
ser = None
try:
    ser = serial.Serial("/dev/ttyACM0", 9600)  # Open serial port
    print("Serial port opened successfully")
except serial.SerialException as e:
    print(f"Error: {e}")
TRESH = 35
# MAIN GAME

framecnt = 0

while running:
    kontrole = [False, False, False, False]
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif(event.key == pg.K_UP):
                    kontrole[0] = True
            elif(event.key == pg.K_DOWN):
                kontrole[1] = True
            elif(event.key == pg.K_RIGHT):
                kontrole[2] = True
            elif(event.key == pg.K_LEFT):
                kontrole[3] = True

    if ser is not None and ser.in_waiting > 0:
        line = ser.readline().decode("utf-8").rstrip()
        data = list(map(float, line.split()))
        if len(data) == 3:

            if data[2] < -TRESH:
                print("gore")
                kontrole[0] = True
            if data[2] > TRESH:
                print("dole")
                kontrole[1] = True
            if data[1] < -TRESH:
                print("desno")
                kontrole[2] = True
            if data[1] > TRESH:
                print("levo")
                kontrole[3] = True
               
    akcija(kontrole)

    # Draw players ZAMENITI SA ANIMACIJAMA KASNIJE
    pg.draw.rect(screen, player1.skin, (*PLAYER1_POS, PLAYER_WIDTH, PLAYER_HEIGHT))
    pg.draw.rect(screen, player2.skin, (*PLAYER2_POS, PLAYER_WIDTH, PLAYER_HEIGHT))

    glavnestrelice()
    clearstarestrelice()
    drawgore()

    proverizelenekoorde()

    if framecnt >= 60:
        generisistrelicu()
        framecnt = 0

    for x in strel:
        x.update()
        x.draw()

    pg.display.flip()
    clock.tick(30)
    # crkavanje
    pobeda = ""
    if player1.HP <= 0 or player2.HP <= 0:
        running = False
        if player1.HP <= 0 and player2.HP <= 0:
            pobeda = "Draw"
        elif player1.HP <= 0:
            pobeda = "Second player has won the game!"
        else:
            pobeda = "First player has won the game!"
    framecnt += 1


if ser is not None:
    ser.close()
pg.quit()
