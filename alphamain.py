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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
class MainMenu:
    def DrawMainMenu(self):
        font = pg.font.Font("freesansbold.ttf", 100)
        font2 = pg.font.Font("freesansbold.ttf", 50)
        ##mouse position
        mpos = pg.mouse.get_pos()

        ##Tilte
        textS = font.render('Schizo fighting', True, "Black")
        RectS = textS.get_rect()
        RectS.center = (960, 100)
        screen.blit(textS, RectS)

        ##settings
        pg.draw.rect(screen, "black", (30, 200, 500, 780), 10, 25)
        pg.draw.rect(screen, "black", (30, 200, 500, 150), 0, 25)
        textS = font.render('Settings', True, "white")
        RectS = textS.get_rect()
        RectS.center = (280, 275)
        screen.blit(textS, RectS)

        ##leaderboard
        pobednici = ["Igrac 1", "Igrac 2", "Igrac 3", "Igrac 4", "Igrac 5"]
        pobede = [str(5), str(4), str(3), str(2), str(1)]
        pg.draw.rect(screen, "black", (1390, 200, 500, 780), 10, 25)
        pg.draw.rect(screen, "black", (1390, 200, 500, 150), 0, 25)
        textW = font.render('Most win', True, "white")
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

        text1 = font.render('1.', True, "Black")
        Rect1 = text1.get_rect()
        Rect1.topleft = (1410, 365)
        screen.blit(text1, Rect1)
        text2 = font.render('2.', True, "Black")
        Rect2 = text2.get_rect()
        Rect2.topleft = (1410, 480)
        screen.blit(text2, Rect2)
        text3 = font.render('3.', True, "Black")
        Rect3 = text3.get_rect()
        Rect3.topleft = (1410, 595)
        screen.blit(text3, Rect3)
        text4 = font.render('4.', True, "Black")
        Rect4 = text4.get_rect()
        Rect4.topleft = (1410, 710)
        screen.blit(text4, Rect4)
        text5 = font.render('5.', True, "Black")
        Rect5 = text5.get_rect()
        Rect5.topleft = (1410, 825)
        screen.blit(text5, Rect5)

        ##play, singleplayer, credits, quit game
        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 390 and mpos[1] >= 250):
            pg.draw.rect(screen, "gray", (560, 250, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 250, 800, 140), 0, 25)
        textP = font.render('Play', True, "white")
        RectP = textP.get_rect()
        RectP.center = (960, 320)
        screen.blit(textP, RectP)

        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 560 and mpos[1] >= 420):
            pg.draw.rect(screen, "gray", (560, 420, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 420, 800, 140), 0, 25)
        textI = font.render('Singleplayer', True, "white")
        RectI = textI.get_rect()
        RectI.center = (960, 490)
        screen.blit(textI, RectI)

        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 730 and mpos[1] >= 590):
            pg.draw.rect(screen, "gray", (560, 590, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 590, 800, 140), 0, 25)
        textC = font.render('Credits', True, "white")
        RectC = textC.get_rect()
        RectC.center = (960, 660)
        screen.blit(textC, RectC)

        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 900 and mpos[1] >= 760):
            pg.draw.rect(screen, "gray", (560, 760, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 760, 800, 140), 0, 25)
        textQ = font.render('Quit Game', True, "white")
        RectQ = textQ.get_rect()
        RectQ.center = (960, 830)
        screen.blit(textQ, RectQ)
    
    def DetectClicks(self):
        mpos = pg.mouse.get_pos()
        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 390 and mpos[1] >= 250):
            self.R = True
        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 560 and mpos[1] >= 420):
            self.R = True
        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 730 and mpos[1] >= 590):
            self.R = True
        if (mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 900 and mpos[1] >= 760):
            self.R = True

MainMenu = MainMenu()
#MAIN MENU
print(screen.get_size())
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
                if (MainMenu.R):
                    running = False
                

    screen.fill("white")
    
    MainMenu.DrawMainMenu()

    pg.display.update()

    clock.tick(60)





#SKIN SELECTOR KOD 
print(12345)


screen.fill((0,0,0))



#CONNECTED ARDUINO






# Serial setup
port = 'COM3'  # Change 'COM3' to your Arduino's port
baud_rate = 9600

try:
    ser = serial.Serial(port, baud_rate)
    time.sleep(1)
except serial.SerialException:
    print(f"Error: Could not open serial port {port}")
    ser = None
def read_gyro():
    if ser is not None and ser.in_waiting:
        try:
            line = ser.readline().decode('utf-8').strip()
            data = list(map(int, line.split()))
            if len(data) == 3:
                return data[0], data[1], data[2]  # gx, gy, gz
        except Exception as e:
            print(f"Error reading data: {e}")
    return None

def detect_movement(gx, gy, threshold=1000):
    gore,dole,levo,desno = False, False, False, False
    if gx > threshold:
        print("Right")
        desno = True
    elif gx < -threshold:
        print("Left")
        levo = True
    if gy > threshold:
        print("Down")
        gore = True
    elif gy < -threshold:
        print("Up")
        dole = True
    listakontrola = [gore, dole, desno, levo]
    return listakontrola

HIGHV = 69420 #VRV OKO 5000
running = True

class Character:
    def __init__(self, HP, skin, name, poz):
        self.HP = HP
        self.skin = skin
        self.name = name
        self.poz = poz
    def update(self, keys):
        if keys[pg.K_LEFT]:
            self.HP -=5
        if keys[pg.K_RIGHT]:
            self.HP += 5
        if(self.HP < 0):
            self.HP = 0
        elif(self.HP > 100):
            self.HP = 100

font = pg.font.Font(None, 54) 

def formatiraj(tacka, offset, multi):
    return offset + multi * tacka

def rot(x, y, teta):
    return ((x * math.cos(teta * math.pi / 180) - y * math.sin(teta * math.pi / 180)), (x * math.sin(teta * math.pi / 180) + y * math.cos(teta * math.pi / 180)))

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
    pg.draw.polygon(screen, boja, [(formatiraj(a[0][0], ox, m), formatiraj(a[0][1], oy, m)), (formatiraj(a[1][0], ox, m), formatiraj(a[1][1], oy, m)), (formatiraj(a[2][0], ox, m), formatiraj(a[2][1], oy, m)), (formatiraj(a[3][0], ox, m), formatiraj(a[3][1], oy, m)), (formatiraj(a[4][0], ox, m), formatiraj(a[4][1], oy, m)), (formatiraj(a[5][0], ox, m), formatiraj(a[5][1], oy, m)), (formatiraj(a[6][0], ox, m), formatiraj(a[6][1], oy, m)), (formatiraj(a[7][0], ox, m), formatiraj(a[7][1], oy, m))])

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
        self.speed = 1
        self.teta = teta
        self.vertices = koordi(self.boja, self.x, self.y, self.m, self.teta)
        self.g = 0.5 

    def update(self):
        nacrtajstrelicu(BLACK, self.x, self.y, self.m, self.teta)
        self.y += self.speed
        #self.speed += self.g
        self.vertices = koordi(self.boja, self.x, self.y, self.m, self.teta)

    def draw(self):
        print(self.vertices)
        #pg.draw.polygon(screen, RED, self.vertices)
        nacrtajstrelicu(self.boja, self.x, self.y, self.m, self.teta)


strel = [    Strelica(RED, 400, 400, 15, 270),
             Strelica(RED, 585, 445, 15, 180),
             Strelica(RED, 725, 355, 15, 0),
             Strelica(RED, 910, 400, 15, 90),
        ]
#PLAYER DEF
PLAYER_WIDTH, PLAYER_HEIGHT = 75/1200*W, 75/800*H  
PLAYER1_POS = (100/1200*W, H - PLAYER_HEIGHT)
PLAYER2_POS = (W - 100/1200*W - PLAYER_WIDTH, H - PLAYER_HEIGHT)
player1 = Character(HP=100, skin="RED", name="Player 1", poz = (*PLAYER1_POS, PLAYER_WIDTH, PLAYER_HEIGHT))
player2 = Character(HP=100, skin="WHITE",  name="Player 2", poz = (*PLAYER2_POS, PLAYER_WIDTH, PLAYER_HEIGHT ))
player1_name_text = font.render(player1.name, True, WHITE)
player2_name_text = font.render(player2.name, True, WHITE)

BAR_WIDTH, BAR_HEIGHT = 320/1200*W, 35/800*H 


def drawgore():
    pg.draw.rect(screen, RED, (100/1200*W, 70/800*H, BAR_WIDTH, BAR_HEIGHT))
    pg.draw.rect(screen, GREEN, (100/1200*W, 70/800*H, BAR_WIDTH * (player1.HP / 100), BAR_HEIGHT))
    pg.draw.rect(screen, RED, (W - 400/1200*W, 70/800*H, BAR_WIDTH, BAR_HEIGHT))
    pg.draw.rect(screen, GREEN, (W - 400/1200*W, 70/800*H, BAR_WIDTH * (player2.HP / 100), BAR_HEIGHT))
    screen.blit(player1_name_text, (100/1200*W, 20/800*H))  
    player2_text_width = player2_name_text.get_width()
    screen.blit(player2_name_text, (W - 400/1200*W + BAR_WIDTH - player2_text_width, 20/800*H))





#MAIN GAME



while running:
    kontrole = [False,False,False,False]
    if ser is None:
        print("Sranje nije povezano")
        running = False
        break
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    gyro_data = read_gyro()
    if gyro_data:
        gx, gy, gz = gyro_data
        kontrole = detect_movement(gx, gy, HIGHV)

    print(kontrole)

    # Draw players ZAMENITI SA ANIMACIJAMA KASNIJE
    pg.draw.rect(screen, player1.skin, (*PLAYER1_POS, PLAYER_WIDTH, PLAYER_HEIGHT))
    pg.draw.rect(screen, player2.skin, (*PLAYER2_POS, PLAYER_WIDTH, PLAYER_HEIGHT))

    drawgore()

    for x in strel:
        x.update()
        x.draw()

    pg.display.flip()
    clock.tick(600)
    #crkavanje
    pobeda = ""
    if(player1.HP <= 0 or player2.HP <= 0):
        running = False
        if(player1.HP <= 0 and player2.HP <= 0):
            pobeda = "Draw"
        elif(player1.HP <= 0):
            pobeda = "Second player has won the game!"
        else:
            pobeda = "First player has won the game!"
        
        #STEFIJEV KOD + MARKOVE ANIMACIJE PADAJU OVDE
    
    
if ser is not None:
    ser.close()
pg.quit()
