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
#SLIKE



# Constants
ARROW_DISPLAY_TIME = 15  # Number of frames to display the arrow

# Initialize variables
left_arrow_display_count = 15
right_arrow_display_count = 15

#BOJE 
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


bob = pg.image.load('freaky.jpg')
locked = pg.image.load("lock.png")
arrow_left_da = pg.image.load('arrow_left_da.png')
arrow_left_ne = pg.image.load('arrow_left_ne.png')
arrow_right_da = pg.image.load('arrow_right_da.png')
arrow_right_ne = pg.image.load('arrow_right_ne.png')

idle_goblin = pg.image.load("goblin.png")
idle_goblin2 = pg.image.load("goblin_2.png")
goblin_perfect = pg.image.load("goblin_perfect.png")
goblin_bad= pg.image.load("goblin_bad.png")

idle_bird1 = pg.image.load("bird_1.png")
idle_bird2 = pg.image.load("bird_2.png")
bird_perfect = pg.image.load("bird_perfect.png")
bird_bad = pg.image.load("bird_bad.png")


idle_svemirac1 = pg.image.load("svemirac_1.png")
idle_svemirac2 = pg.image.load("svemirac_2.png")
svemirac_bad = pg.image.load("svemirac_bad.png")
svemirac_perfect = pg.image.load("svemirac_perfect.png")

idle_flora1 = pg.image.load("boginjacveca_1.png")
idle_flora2 = pg.image.load("boginja_cveca_2.png")
flora_perfect = pg.image.load("boginja_cveca_perfect.png")
flora_bad = pg.image.load("boginja_cveca_bad.png")

idle_demoncina1 = pg.image.load("demoncina_1.png")
idle_demoncina2 = pg.image.load("demoncina_2.png")

idle_vojnik1 = pg.image.load("vojnik_1.png")
idle_vojnik2 = pg.image.load("vojnik_2.png")

Animacije = {
    
    "goblin" : {
        "goblin": [idle_goblin, idle_goblin2],
        "goblin_perfect" : [idle_goblin, idle_goblin2],
        "goblin_bad" : [idle_goblin, idle_goblin2],       
    },
    "bird" : {

        "bird": [idle_bird1, idle_bird2],
        "bird_perfect": [idle_bird1, bird_perfect],
        "bird_bad": [idle_bird2, bird_bad],
    },
    #"yellow bird": [idle_yellow_bird1, idle_yellow_bird2],
    #"yellow bird_perfect": [idle_yellow_bird1, yellow_bird_perfect],
    #"yellow bird_bad": [idle_yellow_bird1, yellow_bird_bad],
    
    "svemirac" :  {
        "svemirac": [idle_svemirac1, idle_svemirac2],
        "svemirac_bad" : [idle_svemirac1, svemirac_bad],
        "svemirac_perfect": [idle_svemirac1, svemirac_perfect]
    },
    
    "flora" : {
        "flora" : [idle_flora1, idle_flora2],
        "flora_bad" : [idle_flora1, flora_bad],
        "flora_perfect" : [idle_flora1, flora_perfect]
    }
    
}


ser = None
#GLOBALI

map = "white"
mainmenu = True
singlplayer = False
multiplayer = False
credits = False
quituj = False
screen_info = pg.display.Info()
MAXW = screen_info.current_w
MAXH = screen_info.current_h
W = screen_info.current_w
H = screen_info.current_h
font = pg.font.Font(None, 54)
skin1 = ""
skin2 = ""
ime1 = ""
ime2 = ""
skinplejera=""
imeplejera = ""
skor1 = 0
skor2 = 0
combo1 = 0
combo2 = 0
perfsound = pg.mixer.Sound('perfect.mp3')
goodsound = pg.mixer.Sound('good.mp3')
badsound = pg.mixer.Sound('bad.mp3')
locked = pg.transform.scale(locked, (350,400))


#mesto za obradu fajla
import json
from operator import itemgetter

with open('savegame.json', 'r') as file:
    game_data = json.load(file)
levelstignut = int(game_data['level'])

top5 = dict(sorted(game_data['score'].items(), key=itemgetter(1), reverse=True)[:5])
topuser = list(top5.keys())
topscore = list(top5.values())



class Character:
    def __init__(self, skin, name, poz):

        self.skin = skin
        self.name = name
        self.poz = poz

PLAYER_WIDTH, PLAYER_HEIGHT = 200, 200*H/800
PLAYER1_POS = (50 / 1200 * W, H - PLAYER_HEIGHT)
PLAYER2_POS = (W - 50 / 1200 * W- PLAYER_WIDTH, H - PLAYER_HEIGHT)
player1 = Character(
    skin= skin1, 
    name=ime1,
    poz=(*PLAYER1_POS, PLAYER_WIDTH, PLAYER_HEIGHT)
)
player2 = Character(
    skin= skin2,
    name=ime2,
    poz=(*PLAYER2_POS, PLAYER_WIDTH, PLAYER_HEIGHT)
)


class MainMenu:
    def __init__(self, R):
        self.R = R

    def DrawMainMenu(self):
        font = pg.font.Font("freesansbold.ttf", 100)
        font2 = pg.font.Font("freesansbold.ttf", 50)
        ##mouse position
        mpos = pg.mouse.get_pos()

        ##Tilte
        textS = font.render("Petljovizija™ Simulator", True, "Black")
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
        pobednici = topuser
        pobede = topscore
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
        textP1 = font2.render(str(pobednici[0]), True, "Black")
        RectP1 = textP1.get_rect()
        RectP1.center = (1625, 415)
        screen.blit(textP1, RectP1)
        textP2 = font2.render(str(pobednici[1]), True, "Black")
        RectP2 = textP2.get_rect()
        RectP2.center = (1625, 530)
        screen.blit(textP2, RectP2)
        textP3 = font2.render(str(pobednici[2]), True, "Black")
        RectP3 = textP3.get_rect()
        RectP3.center = (1625, 645)
        screen.blit(textP3, RectP3)
        textP4 = font2.render(str(pobednici[3]), True, "Black")
        RectP4 = textP4.get_rect()
        RectP4.center = (1625, 760)
        screen.blit(textP4, RectP4)
        textP5 = font2.render(str(pobednici[4]), True, "Black")
        RectP5 = textP5.get_rect()
        RectP5.center = (1625, 875)
        screen.blit(textP5, RectP5)

        ## broj pobeda
        textW1 = font2.render(str(pobede[0]), True, "Black")
        RectW1 = textW1.get_rect()
        RectW1.center = (1815, 415)
        screen.blit(textW1, RectW1)
        textW2 = font2.render(str(pobede[1]), True, "Black")
        RectW2 = textW2.get_rect()
        RectW2.center = (1815, 530)
        screen.blit(textW2, RectW2)
        textW3 = font2.render(str(pobede[2]), True, "Black")
        RectW3 = textW3.get_rect()
        RectW3.center = (1815, 645)
        screen.blit(textW3, RectW3)
        textW4 = font2.render(str(pobede[3]), True, "Black")
        RectW4 = textW4.get_rect()
        RectW4.center = (1815, 760)
        screen.blit(textW4, RectW4)
        textW5 = font2.render(str(pobede[4]), True, "Black")
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
        textP = font.render("Singleplayer", True, "white")
        RectP = textP.get_rect()
        RectP.center = (960, 320)
        screen.blit(textP, RectP)

        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 560 and mpos[1] >= 420:
            pg.draw.rect(screen, "gray", (560, 420, 800, 140), 0, 25)
        else:
            pg.draw.rect(screen, "black", (560, 420, 800, 140), 0, 25)
        textI = font.render("Multiplayer", True, "white")
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
        global mainmenu
        mpos = pg.mouse.get_pos()
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 390 and mpos[1] >= 250:
            self.R = True
            global singlplayer
            singlplayer = True
            mainmenu = False
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 560 and mpos[1] >= 420:
            self.R = True
            global multiplayer
            multiplayer = True
            mainmenu = False
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 730 and mpos[1] >= 590:
            self.R = True
            global credits
            credits = True
            mainmenu = False
        if mpos[0] >= 560 and mpos[0] <= 1360 and mpos[1] <= 900 and mpos[1] >= 760:
            self.R = True
            global quituj
            quituj = True
            mainmenu = False
MainMenu = MainMenu(False)
def Mainmenu():
    global running
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    MainMenu.DetectClicks()
                    if MainMenu.R:
                        running = False
                        MainMenu.R = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        screen.fill("white")
    
        MainMenu.DrawMainMenu()
    
        pg.display.update()
    
        clock.tick(60)


class SkinSelector:
    def __init__ (self, user1, user2, active1, active2, R, num1, num2, skinnum, skins, skinname):
        self.user1 = user1
        self.user2 = user2
        self.active1 = active1
        self.active2 = active2
        self.R = R
        self.num1 = num1
        self.num2 = num2
        ##broj skinova i skinovi i imena skinova
        self.skinnum = skinnum
        self.skins = skins
        self.skinname = skinname

    def DrawSkinSelector(self):
        mpos = pg.mouse.get_pos()
        font = pg.font.Font("freesansbold.ttf", 100)
        font2 = pg.font.Font("freesansbold.ttf", 40)

        pg.draw.rect(screen, "black", (150, 500, 300, 450), 5)
        pg.draw.rect(screen, "black", (1470, 500, 300, 450), 5)

        if (mpos[0] >= 600 and mpos[0] <= 1320 and mpos[1] <= 250 and mpos[1] >= 50):
            pg.draw.rect(screen, "gray", (600, 50, 720, 200), 0, 25)
        else:
            pg.draw.rect(screen, "black", (600, 50, 720, 200), 0, 25)
        textP = font.render("Next", True, "white")
        RectP = textP.get_rect()
        RectP.center = (960, 150)
        screen.blit(textP, RectP)

        self.input_rect1 = pg.Rect(100, 250, 400, 100)
        color_active = pg.Color('gray')
        color_passive = pg.Color('black')
        if self.active1: 
            color1 = color_active 
        else: 
            color1 = color_passive
        text1 = font.render(self.user1, True, "black")
        screen.blit(text1, (self.input_rect1.x + 5, self.input_rect1.y + 5))
        self.input_rect1.w = max(400, text1.get_width() + 10)
        pg.draw.rect(screen, color1, self.input_rect1, 5)
        
        self.input_rect2 = pg.Rect(1420, 250, 400, 100)
        color_active = pg.Color('gray')
        color_passive = pg.Color('black')
        if self.active2: 
            color2 = color_active
        else: 
            color2 = color_passive
        text2 = font.render(self.user2, True, "black")
        screen.blit(text2, (self.input_rect2.x + 5, self.input_rect2.y + 5))
        self.input_rect2.w = max(400, text2.get_width() + 10)
        pg.draw.rect(screen, color2, self.input_rect2, 5)

        skincen1 = pg.Rect(0, 0, 100, 100)
        skincen1.center = (300, 725)
        ##crta skin levo
        if (self.num1 != self.skinnum):
            screen.blit(Animacije[self.skins[self.num1]][self.skins[self.num1]][0], skincen1)
            textskin1 = font2.render(self.skinname[self.num1], True, "black")
            Rect1 = textskin1.get_rect()
            Rect1.center = (300, 1000)
            screen.blit(textskin1, Rect1)
        elif self.user1 == "freaky":
            Rect1 = bob.get_rect()
            Rect1.center = (300, 725)
            screen.blit(bob, Rect1)
            textskin1 = font2.render("pick up", True, "black")
            Rect1 = textskin1.get_rect()
            Rect1.center = (300, 1000)
            screen.blit(textskin1, Rect1)
        elif self.user1 == "help":
            pg.quit()
        else:
            pg.draw.rect(screen, "black", skincen1)
            textskin1 = font2.render("???", True, "black")
            Rect1 = textskin1.get_rect()
            Rect1.center = (300, 1000)
            screen.blit(textskin1, Rect1)

        skincen2 = pg.Rect(0, 0, 100, 100)
        skincen2.center = (1620, 725)
        ##crta skin desno
        screen.blit(Animacije[self.skins[self.num2]][self.skins[self.num2]][0], skincen2)
        textskin2 = font2.render(self.skinname[self.num2], True, "black")
        Rect2 = textskin2.get_rect()
        Rect2.center = (1620, 1000)
        screen.blit(textskin2, Rect2)

        if 50 <= mpos[0] <= 150 and 50 <= mpos[1] <= 150:
            pg.draw.rect(screen, "gray", (50, 50, 100, 100), 0, 25)
        else:
            pg.draw.rect(screen, "black", (50, 50, 100, 100), 0, 25)
        

    def DetectClick(self):
        mpos = pg.mouse.get_pos()
        if (mpos[0] >= 600 and mpos[0] <= 1320 and mpos[1] <= 250 and mpos[1] >= 50):
            self.R = True
        if self.input_rect1.collidepoint(mpos):
            self.active1 = True
        else:
            self.active1 = False
        if self.input_rect2.collidepoint(mpos):
            self.active2 = True
        else:
            self.active2 = False
        if 50 <= mpos[0] <= 150 and 50 <= mpos[1] <= 150:
            self.R = True
            global multiplayer
            multiplayer = False
            global mainmenu
            mainmenu = True
SkinSelector = SkinSelector("", "", False, False, False, 0, 0, 4, ["goblin", "bird", "svemirac", "flora"], ["goblin", "bird", "svemirac", "flora"])
def skinselectormulti():
    global running, map
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    SkinSelector.DetectClick()
                    if (SkinSelector.R):
                        running = False
                        SkinSelector.R = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if SkinSelector.num2 == 0:
                        SkinSelector.num2 = SkinSelector.skinnum - 1
                    else:
                        SkinSelector.num2 -= 1
                elif event.key == pg.K_RIGHT:
                    if SkinSelector.num2 == SkinSelector.skinnum - 1:
                        SkinSelector.num2 = 0
                    else:
                        SkinSelector.num2 += 1
                elif event.key == pg.K_BACKSPACE:
                    if SkinSelector.active1:
                        SkinSelector.user1 = SkinSelector.user1[:-1]
                    elif SkinSelector.active2:
                        SkinSelector.user2 = SkinSelector.user2[:-1]
                elif SkinSelector.active1 or SkinSelector.active2:
                    if SkinSelector.active1:
                        SkinSelector.user1 += event.unicode
                    elif SkinSelector.active2:
                        SkinSelector.user2 += event.unicode
                elif event.key == pg.K_a:
                    if SkinSelector.num1 == 0:
                        SkinSelector.num1 = SkinSelector.skinnum
                    else:
                        SkinSelector.num1 -= 1
                elif event.key == pg.K_d:
                    if SkinSelector.num1 == SkinSelector.skinnum:
                        SkinSelector.num1 = 0
                    else:
                        SkinSelector.num1 += 1
                ##mape
                elif event.key == pg.K_1:
                    map = "white"
                elif event.key == pg.K_2:
                    map = "pink"
                elif event.key == pg.K_3:
                    map = "dark blue"
                elif event.key == pg.K_4:
                    map = "brown"
                elif event.key == pg.K_ESCAPE:
                    running = False


        screen.fill(map)

        SkinSelector.DrawSkinSelector()

        ##screen.blit(carImg, (700, 400))

        pg.display.update()

        clock.tick(60)




class SkinSelectorSingle:
    def __init__(self, user1, active1, R, num1, skinnum, skins, skinname):
        self.user1 = user1
        self.active1 = active1
        self.R = R
        self.num1 = num1
        self.skinnum = skinnum
        self.skins = skins
        self.skinname = skinname

    def DrawSkinSelector(self):
        global left_arrow_display_count, right_arrow_display_count

        mpos = pg.mouse.get_pos()
        font = pg.font.Font("freesansbold.ttf", 100)
        font2 = pg.font.Font("freesansbold.ttf", 40)

        pg.draw.rect(screen, "black", (810, 500, 300, 450), 5)

        if 600 <= mpos[0] <= 1320 and 50 <= mpos[1] <= 250:
            pg.draw.rect(screen, "gray", (600, 50, 720, 200), 0, 25)
        else:
            pg.draw.rect(screen, "black", (600, 50, 720, 200), 0, 25)
        textP = font.render("Next", True, "white")
        RectP = textP.get_rect()
        RectP.center = (960, 150)
        screen.blit(textP, RectP)
        
        self.input_rect1 = pg.Rect(760, 300, 400, 100)
        color_active = pg.Color('gray')
        color_passive = pg.Color('black')
        color1 = color_active if self.active1 else color_passive
        text1 = font.render(self.user1, True, "black")
        screen.blit(text1, (self.input_rect1.x + 5, self.input_rect1.y + 5))
        self.input_rect1.w = max(400, text1.get_width() + 10)
        pg.draw.rect(screen, color1, self.input_rect1, 5)
        
        skincen1 = pg.Rect(0, 0, 100, 100)
        skincen1.center = (960, 725)

        if self.num1 != 5:
            screen.blit(Animacije[self.skins[self.num1]][self.skins[self.num1]][0], skincen1)
            textskin1 = font2.render(self.skinname[self.num1], True, "black")
            Rect1 = textskin1.get_rect()
            Rect1.center = (960, 1000)
            screen.blit(textskin1, Rect1)
        elif self.user1 == "freaky":
            Rect1 = bob.get_rect()
            Rect1.center = (960, 725)
            screen.blit(bob, Rect1)
            textskin1 = font2.render("pick up", True, "black")
            Rect1 = textskin1.get_rect()
            Rect1.center = (960, 1000)
            screen.blit(textskin1, Rect1)
        elif self.user1 == "help":
            pg.quit()
        else:
            pg.draw.rect(screen, "black", skincen1)
            textskin1 = font2.render("???", True, "black")
            Rect1 = textskin1.get_rect()
            Rect1.center = (960, 1000)
            screen.blit(textskin1, Rect1)

        if 50 <= mpos[0] <= 150 and 50 <= mpos[1] <= 150:
            pg.draw.rect(screen, "gray", (50, 50, 100, 100), 0, 25)
        else:
            pg.draw.rect(screen, "black", (50, 50, 100, 100), 0, 25)
        
        # Draw left arrow if count is greater than 0
        if left_arrow_display_count > 0:
            left_arrow_rect = arrow_left_da.get_rect(center=(610, 725))
            screen.blit(arrow_left_da, left_arrow_rect)
            left_arrow_display_count -= 1
        else:
            left_arrow_rect = arrow_left_ne.get_rect(center=(610, 725))
            screen.blit(arrow_left_ne, left_arrow_rect)
        # Draw right arrow if count is greater than 0
        if right_arrow_display_count > 0:
            right_arrow_rect = arrow_right_da.get_rect(center=(1310, 725))
            screen.blit(arrow_right_da, right_arrow_rect)
            right_arrow_display_count -= 1
        else:
            right_arrow_rect = arrow_right_ne.get_rect(center=(1310, 725))
            screen.blit(arrow_right_ne, right_arrow_rect)

    def DetectClick(self):
        mpos = pg.mouse.get_pos()
        if 600 <= mpos[0] <= 1320 and 50 <= mpos[1] <= 250:
            self.R = True
        if self.input_rect1.collidepoint(mpos):
            self.active1 = True
        else:
            self.active1 = False
        if 50 <= mpos[0] <= 150 and 50 <= mpos[1] <= 150:
            global mainmenu
            mainmenu = True
            global singlplayer
            singlplayer = False
            self.R = True
SkinSelectorSingle = SkinSelectorSingle("", False, False, 0, 4, ["goblin", "bird", "svemirac",  "flora"], ["goblin", "bird", "svemirac",  "flora"])
def skinselectorsingle():
    global running, map, left_arrow_display_count, right_arrow_display_count
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    SkinSelectorSingle.DetectClick()
                    if SkinSelectorSingle.R:
                        running = False
                        SkinSelector.R = False
                        SkinSelector.num1 = 0
                        SkinSelector.user1 = ""
                        SkinSelector.active1 = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if SkinSelectorSingle.active1:
                        SkinSelectorSingle.user1 = SkinSelectorSingle.user1[:-1]
                elif SkinSelectorSingle.active1:
                    SkinSelectorSingle.user1 += event.unicode
                elif event.key == pg.K_a:
                    if SkinSelectorSingle.num1 == 0:
                        SkinSelectorSingle.num1 = SkinSelectorSingle.skinnum
                    else:
                        SkinSelectorSingle.num1 -= 1
                    left_arrow_display_count = ARROW_DISPLAY_TIME
                elif event.key == pg.K_d:
                    if SkinSelectorSingle.num1 == SkinSelectorSingle.skinnum:
                        SkinSelectorSingle.num1 = 0
                    else:
                        SkinSelectorSingle.num1 += 1
                    right_arrow_display_count = ARROW_DISPLAY_TIME
                elif event.key == pg.K_1:
                    map = "white"
                elif event.key == pg.K_2:
                    map = "pink"
                elif event.key == pg.K_3:
                    map = "dark blue"
                elif event.key == pg.K_4:
                    map = "brown"
        screen.fill(map)
        SkinSelectorSingle.DrawSkinSelector()
        pg.display.update()
        clock.tick(60)




class levelSelector:
    def __init__(self, R, num1, levelnum, levels, levelname):
        self.R = R
        self.num1 = num1
        self.levelnum = levelnum
        self.levels = levels
        self.levelname = levelname

    def DrawlevelSelector(self):
        global left_arrow_display_count, right_arrow_display_count

        mpos = pg.mouse.get_pos()
        font = pg.font.Font("freesansbold.ttf", 100)
        font2 = pg.font.Font("freesansbold.ttf", 40)

        pg.draw.rect(screen, "black", (810, 500, 300, 450), 5)

        if 600 <= mpos[0] <= 1320 and 50 <= mpos[1] <= 250:
            pg.draw.rect(screen, "gray", (600, 50, 720, 200), 0, 25)
        else:
            pg.draw.rect(screen, "black", (600, 50, 720, 200), 0, 25)
        textP = font.render("Play", True, "white")
        RectP = textP.get_rect()
        RectP.center = (960, 150)
        screen.blit(textP, RectP)

        levelcen1 = pg.Rect(0, 0, 100, 100)
        levelcen1.center = (960, 725)

        if self.num1 != self.levelnum:
            screen.blit(Animacije[self.levels[self.num1]][self.levels[self.num1]][0], levelcen1)
            textlevel1 = font2.render(self.levelname[self.num1], True, "black")
            Rect1 = textlevel1.get_rect()
            Rect1.center = (960, 1000)
            screen.blit(textlevel1, Rect1)
        
        if 50 <= mpos[0] <= 150 and 50 <= mpos[1] <= 150:
            pg.draw.rect(screen, "gray", (50, 50, 100, 100), 0, 25)
        else:
            pg.draw.rect(screen, "black", (50, 50, 100, 100), 0, 25)

        # Draw left arrow if count is greater than 0
        if left_arrow_display_count > 0:
            left_arrow_rect = arrow_left_da.get_rect(center=(610, 725))
            screen.blit(arrow_left_da, left_arrow_rect)
            left_arrow_display_count -= 1
        else:
            left_arrow_rect = arrow_left_ne.get_rect(center=(610, 725))
            screen.blit(arrow_left_ne, left_arrow_rect)
        # Draw right arrow if count is greater than 0
        if right_arrow_display_count > 0:
            right_arrow_rect = arrow_right_da.get_rect(center=(1310, 725))
            screen.blit(arrow_right_da, right_arrow_rect)
            right_arrow_display_count -= 1
        else:
            right_arrow_rect = arrow_right_ne.get_rect(center=(1310, 725))
            screen.blit(arrow_right_ne, right_arrow_rect)

    def DetectClick(self):
        mpos = pg.mouse.get_pos()
        if 600 <= mpos[0] <= 1320 and 50 <= mpos[1] <= 250:
            self.R = True
        else:
            self.active1 = False
        if 50 <= mpos[0] <= 150 and 50 <= mpos[1] <= 150:
            global mainmenu
            mainmenu = True
            global singlplayer
            singlplayer = False
            self.R = True
levelSelector = levelSelector( False, 0, 3, ["bird", "bird", "bird"], ["Iva", "Vledi", "Nena"])
def levelselector():
    global running, map, left_arrow_display_count, right_arrow_display_count
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    levelSelector.DetectClick()
                    if levelSelector.R:
                        running = False
                        levelSelector.R = False
                    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if levelSelector.active1:
                        levelSelector.user1 = levelSelector.user1[:-1]
                elif event.key == pg.K_a:
                    if levelSelector.num1 == 0:
                        levelSelector.num1 = levelSelector.levelnum
                    else:
                        levelSelector.num1 -= 1
                    left_arrow_display_count = ARROW_DISPLAY_TIME
                elif event.key == pg.K_d:
                    if levelSelector.num1 == levelSelector.levelnum:
                        levelSelector.num1 = 0
                    else:
                        levelSelector.num1 += 1
                    right_arrow_display_count = ARROW_DISPLAY_TIME
        screen.fill(map)
        levelSelector.DrawlevelSelector()
        pg.display.update()
        clock.tick(60)





screen.fill((0, 0, 0))




running = True
screen.fill(map)




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
        self.kakvaje = "bad"
        self.prosla = False
        self.vertices = koordi(self.boja, self.x, self.y, self.m, self.teta)
        self.g = 0.5

    def update(self):
        nacrtajstrelicu(black, self.x, self.y, self.m, self.teta)
        self.y += self.speed

    def draw(self):
        nacrtajstrelicu(self.boja, self.x, self.y, self.m, self.teta)

strel = []
strel2 = []

perfektogr = 20
goodogr = 40

def generisistrelicu():
    koja = random.randint(0, 3)
    i = random.randint(0, len(sveboje) - 1)
    while ((sveboje[i] == green) or (sveboje[i] == black) or (sveboje[i] == white) or (sveboje[i] == yellow) or (sveboje[i] == red)):
        i = random.randint(0, len(sveboje) - 1)
    if koja == 0:
        strel.append(Strelica(sveboje[i], 400, 200, 15, 270))
    elif koja == 1:
        strel.append(Strelica(sveboje[i], 585, 245, 15, 180))
    elif koja == 2:
        strel.append(Strelica(sveboje[i], 725, 155, 15, 0))
    else:
        strel.append(Strelica(sveboje[i], 910, 200, 15, 90))

def generisistrelicu2():
    koja = random.randint(0, 3)
    i = random.randint(0, len(sveboje) - 1)
    while ((sveboje[i] == green) or (sveboje[i] == black) or (sveboje[i] == white) or (sveboje[i] == yellow) or (sveboje[i] == red)):
        i = random.randint(0, len(sveboje) - 1)
    if koja == 0:
        strel2.append(Strelica(sveboje[i], 1010, 200, 15, 270))
    elif koja == 1:
        strel2.append(Strelica(sveboje[i], 1195, 245, 15, 180))
    elif koja == 2:
        strel2.append(Strelica(sveboje[i], 1335, 155, 15, 0))
    else:
        strel2.append(Strelica(sveboje[i], 1520, 200, 15, 90))

def clearstarestrelice():
    for st in strel:
        if st.y > 1200:
            strel.remove(st)

def clearstarestrelice2():
    for st in strel2:
        if st.y > 1200:
            strel2.remove(st)

def glavnestrelice():
    debljina = 5
    nacrtajstrelicu2(white, 400, 900, 15, 270, debljina)
    nacrtajstrelicu2(white, 585, 945, 15, 180, debljina)
    nacrtajstrelicu2(white, 725, 855, 15, 0, debljina)
    nacrtajstrelicu2(white, 910, 900, 15, 90, debljina)

    nacrtajstrelicu2(white, 1010, 900, 15, 270, debljina)
    nacrtajstrelicu2(white, 1195, 945, 15, 180, debljina)
    nacrtajstrelicu2(white, 1335, 855, 15, 0, debljina)
    nacrtajstrelicu2(white, 1520, 900, 15, 90, debljina)

    # nacrtajstrelicu(black, 400, 900, 15, 270)
    # nacrtajstrelicu(black, 585, 945, 15, 180)
    # nacrtajstrelicu(black, 725, 855, 15, 0)
    # nacrtajstrelicu(black, 910, 900, 15, 90)
def perfect_score_animation1(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("PERFECT!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(100, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][lik.skin+"_perfect"][br]= pg.transform.scale(Animacije[lik.skin][lik.skin+"_perfect"][br],(200, 200))
    screen.blit(Animacije[lik.skin][lik.skin+"_perfect"][br], lik.poz)

def perfect_score_animation2(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("PERFECT!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1700, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][lik.skin+"_perfect"][br]= pg.transform.scale(Animacije[lik.skin][lik.skin+"_perfect"][br],(200, 200))
    screen.blit(Animacije[lik.skin][lik.skin+"_perfect"][br], lik.poz)

def good_score_animation1(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("GOOD!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][lik.skin][br] = pg.transform.scale(Animacije[lik.skin][lik.skin][br], (200, 200))
    screen.blit(Animacije[lik.skin][lik.skin][br], lik.poz)
    

def good_score_animation2(lik,br):
    font = pg.font.Font(None, 74)
    text = font.render("GOOD!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1700, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][lik.skin][br] = pg.transform.scale(Animacije[lik.skin][lik.skin][br], (200, 200))
    screen.blit(Animacije[lik.skin][lik.skin][br], lik.poz)
    
def bad_score_animation1(lik,br):
    font = pg.font.Font(None, 74)
    text = font.render("BAD", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][lik.skin+"_bad"][br]= pg.transform.scale(Animacije[lik.skin][lik.skin+"_bad"][br],(200, 200))
    screen.blit(Animacije[lik.skin][lik.skin+"_bad"][br], lik.poz)

def bad_score_animation2(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("BAD", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1700, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][lik.skin+"_bad"][br]= pg.transform.scale(Animacije[lik.skin][lik.skin+"_bad"][br],(200, 200))
    screen.blit(Animacije[lik.skin][lik.skin+"_bad"][br], lik.poz)

def idle_animation1(lik, br):
    Animacije[lik.skin][lik.skin][br] = pg.transform.scale(Animacije[lik.skin][lik.skin][br], (200, 200))
    screen.blit(Animacije[lik.skin][lik.skin][br], lik.poz)
def idle_animation2(lik,br):
    Animacije[lik.skin][lik.skin][br] = pg.transform.scale(Animacije[lik.skin][lik.skin][br], (200, 200))
    screen.blit(Animacije[lik.skin][lik.skin][br], lik.poz)

brojac = 0

perfekt1 = False
gud1 = False
bed1 = False
ajdl1 = True
perfekt2 = False
gud2 = False
bed2 = False
ajdl2 = True

def perfectakcija():

    pg.mixer.Sound.play(perfsound)
    global skor1, combo1, skor2, combo2
    skor1 += int(20 * max(1, 0.8 + combo1/10))
    combo1 += 1
    global perfekt1
    perfekt1 = True

def goodakcija():
    pg.mixer.Sound.play(goodsound)
    global skor1, combo1, skor2, combo2
    skor1 += int(10 * max(1, 0.8 + combo1/10))
    combo1 += 1
    global gud1
    gud1 = True

def badakcija():
    pg.mixer.Sound.play(badsound)
    global skor1, combo1, skor2, combo2
    combo1 = 0
    global bed1
    bed1 = True

def perfectakcija2():
    pg.mixer.Sound.play(perfsound)
    global skor1, combo1, skor2, combo2
    skor2 += int(20 * max(1, 0.8 + combo2/10))
    combo2 += 1
    global perfekt2
    perfekt2 = True

def goodakcija2():
    pg.mixer.Sound.play(goodsound)
    global skor1, combo1, skor2, combo2
    skor2 += int(10 * max(1, 0.8 + combo2/10))
    combo2 += 1
    global gud2
    gud2 = True

def badakcija2():
    pg.mixer.Sound.play(badsound)
    global skor1, combo1, skor2, combo2
    combo2 = 0
    global bed2
    bed2 = True

def proverizelenekoorde():
    v = True
    for strelica in strel:
        if strelica.x == 400:
            if(strelica.y > (900 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green
                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                    v = False
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija()

        elif strelica.x == 585:
            if(strelica.y > (945 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green
                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija()
        
        elif strelica.x == 725:
            if(strelica.y > (855 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green
                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija()
            
            if(strelica.y >= (900 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green
                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija()
            
                    # -z je gore, +z je dole, +y je levo, -y je desno

    if v == False:
        # apdejtajskor(0)
        pass

def proverizelenekoorde2():
    v = True
    for strelica in strel2:
        if strelica.x == 1010:
            if(strelica.y > (900 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green
                    
                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                    v = False
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija2()

            

        elif strelica.x == 1195:
            if(strelica.y > (945 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green

                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija2()
                
        elif strelica.x == 1335:
            if(strelica.y > (855 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green
                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija2()
                    v = False

            
        else:
            if(strelica.y >= (900 + goodogr)):
                if(strelica.kakvaje == "perfect"):
                    strelica.boja = green
                elif(strelica.kakvaje == "good"):
                    strelica.boja = yellow
                else:
                    strelica.boja = red
                if(strelica.prosla == False):
                    strelica.prosla = True
                    badakcija2()
                else:
                    v = False

    if v == False:
        # apdejtajskor(0)
        pass

def akcija(kontrole):
    if kontrole[3]:
        jeperfect = False
        jegood = False
        najblize = 10000
        for x in strel:
            if(x.x == 400 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 900))
        for x in strel:
            if(najblize == abs(x.y - 900)):
                if x.x == 400 and x.prosla == False:
                    #900
                    if (abs(x.y - 900) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            perfectakcija()
                            x.kakvaje = "perfect"
                            x.boja = green
                    elif(abs(x.y - 900) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            goodakcija()
                            x.kakvaje = "good"
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            badakcija()
                            x.kakvaje = "bad"
                            x.boja = red

    elif kontrole[1]:
        jeperfect = False
        jegood = False
        najblize = 10000
        for x in strel:
            if(x.x == 585 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 945))
        for x in strel:
            if(najblize == abs(x.y - 945)):
                if x.x == 585 and x.prosla == False:
                    #945
                    if (abs(x.y - 945) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "perfect"
                            perfectakcija()
                            x.boja = green
                    elif(abs(x.y - 945) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "good"
                            goodakcija()
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "bad"
                            badakcija()
                            x.boja = red

    elif kontrole[0]:
        jeperfect = False
        jegood = False
        najblize = 100000
        for x in strel:
            if(x.x == 725 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 855))
        for x in strel:
            if(najblize == abs(x.y - 855)):
                if x.x == 725 and x.prosla == False:
                    #855
                    if (abs(x.y - 855) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "perfect"
                            perfectakcija()
                            x.boja = green
                    elif(abs(x.y - 855) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "good"
                            goodakcija()
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            badakcija() 
                            x.kakvaje = "bad"
                            x.boja = red

    elif kontrole[2]:
        jeperfect = False
        jegood = False
        najblize = 1000000
        for x in strel:
            if(x.x == 910 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 900))
        for x in strel:
            if(najblize == abs(x.y - 900)):
                if x.x == 910 and x.prosla == False:
                    #900
                    if (abs(x.y - 900) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "perfect"                        
                            perfectakcija()
                            x.boja = green
                    elif(abs(x.y - 900) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "good"
                            goodakcija()
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "bad"
                            badakcija()
                            x.boja = red

def akcija2(kontrole):
    if kontrole[3]:
        jeperfect = False
        jegood = False
        najblize = 10000
        for x in strel2:
            if(x.x == 1010 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 900))
        for x in strel2:
            if(najblize == abs(x.y - 900)):
                if x.x == 1010 and x.prosla == False:
                    #900
                    if (abs(x.y - 900) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            perfectakcija2()
                            x.kakvaje = "perfect"
                            x.boja = green
                    elif(abs(x.y - 900) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            goodakcija2()
                            x.kakvaje = "good"
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            badakcija2()
                            x.kakvaje = "bad"
                            x.boja = red

    elif kontrole[1]:
        jeperfect = False
        jegood = False
        najblize = 10000
        for x in strel2:
            if(x.x == 1195 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 945))
        for x in strel2:
            if(najblize == abs(x.y - 945)):
                if x.x ==1195 and x.prosla == False:
                    #945
                    if (abs(x.y - 945) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "perfect"
                            perfectakcija2()
                            x.boja = green
                    elif(abs(x.y - 945) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "good"
                            goodakcija2()
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "bad"
                            badakcija2()
                            x.boja = red

    elif kontrole[0]:
        jeperfect = False
        jegood = False
        najblize = 100000
        for x in strel2:
            if(x.x == 1335 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 855))
        for x in strel2:
            if(najblize == abs(x.y - 855)):
                if x.x == 1335 and x.prosla == False:
                    #855
                    if (abs(x.y - 855) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "perfect"
                            perfectakcija2()
                            x.boja = green
                    elif(abs(x.y - 855) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "good"
                            goodakcija2()
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            badakcija2() 
                            x.kakvaje = "bad"
                            x.boja = red

    elif kontrole[2]:
        jeperfect = False
        jegood = False
        najblize = 1000000
        for x in strel2:
            if(x.x == 1520 and x.prosla == False):
                najblize = min(najblize, abs(x.y - 900))
        for x in strel2:
            if(najblize == abs(x.y - 900)):
                if x.x == 1520 and x.prosla == False:
                    #900
                    if (abs(x.y - 900) <= perfektogr):
                        jeperfect = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "perfect"                        
                            perfectakcija2()
                            x.boja = green
                    elif(abs(x.y - 900) <= goodogr):
                        jegood = True
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "good"
                            goodakcija2()
                            x.boja = yellow
                    else:
                        if(x.prosla == False):
                            x.prosla = True
                            x.kakvaje = "bad"
                            badakcija2()
                            x.boja = red

def singlbot(perfectchance, goodchance):
    randbroj = random.randint(1, 100)
    if(randbroj <= perfectchance):
        for x in strel2:
            if(x.x == 1010):
                if((900 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = green
                        perfectakcija2()
            elif(x.x == 1195):
                if((945 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = green
                        perfectakcija2()
            elif(x.x == 1335):
                if((855 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = green
                        perfectakcija2()
            elif(x.x == 1520):
                if((900 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = green  
                        perfectakcija2()                            
    elif(randbroj <= goodchance):
        for x in strel2:
            if(x.x == 1010):
                if((900 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = yellow
                        goodakcija2()
            elif(x.x == 1195):
                if((945 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = yellow
                        goodakcija2()
            elif(x.x == 1335):
                if((855 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = yellow
                        goodakcija2()
            elif(x.x == 1520):
                if((900 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = yellow 
                        goodakcija2()
    else:
        for x in strel2:
            if(x.x == 1010):
                if((900 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = red
                        badakcija2()
            elif(x.x == 1195):
                if((945 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = red
                        badakcija2()
            elif(x.x == 1335):
                if((855 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = red
                        badakcija2()
            elif(x.x == 1520):
                if((900 + goodogr) < x.y):
                    if(x.prosla == False):
                        x.prosla = True
                        x.boja = red
                        badakcija2()


def drawgore():
    # POPRAVITI TEKSTOVE
    skorstr1 = "SCORE: " + str(skor1)
    skorstr2 = "SCORE: " + str(skor2)
    if combo1 > 2:
        combo1str= "X" + str(combo1)
    else:
        combo1str = ""
    if combo2 > 2:
        combo2str = "X" + str(combo2)
    else:
        combo2str = ""
    score1_text = font.render(skorstr1, True, white)
    score2_text = font.render(skorstr2, True, white)
    combo1_text = font.render(combo1str, True, white)
    combo2_text = font.render(combo2str, True, white)
    screen.blit(player1_name_text, (50 / 1920 * W, 20 / 800 * H))
    screen.blit(score1_text,  (50 / 1920 * W, 100 / 800 * H))
    screen.blit(combo1_text,  (50 / 1920 * W, 180 / 800 * H))
    player2_text_width = player2_name_text.get_width()
    skor2_text_width =  score2_text.get_width()
    screen.blit(player2_name_text,(W - 50 / 1920 * W - max(player2_text_width , skor2_text_width), 20 / 800 * H))
    screen.blit(score2_text ,(W - 50 / 1920 * W  - max(player2_text_width , skor2_text_width), 100 / 800 * H))
    screen.blit(combo2_text ,(W - 50 / 1920 * W  - max(player2_text_width , skor2_text_width), 180 / 800 * H))

def singlplejer():

    framecnt = 0
    running = True
    while running:
        kontrole = [False, False, False, False]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                elif(event.key == pg.K_w):
                    kontrole[0] = True
                elif(event.key == pg.K_s):
                    kontrole[1] = True
                elif(event.key == pg.K_d):
                    kontrole[2] = True
                elif(event.key == pg.K_a):
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
        singlbot(70, 85)


        # Draw players ZAMENITI SA ANIMACIJAMA KASNIJE
        pg.draw.rect(screen, player1.skin, (*PLAYER1_POS, PLAYER_WIDTH, PLAYER_HEIGHT))
        pg.draw.rect(screen, player2.skin, (*PLAYER2_POS, PLAYER_WIDTH, PLAYER_HEIGHT))

        glavnestrelice()
        clearstarestrelice()
        clearstarestrelice2()
        drawgore()

        proverizelenekoorde()

        if framecnt >= 60:
            generisistrelicu()
            generisistrelicu2()
            framecnt = 0

        for x in strel:
            x.update()
            x.draw()

        for x in strel2:
            x.update()
            x.draw()

        pg.display.flip()
        clock.tick(30)

        framecnt += 1
        screen.fill(map)
plsradi = 0
plsradi2 = 0
def multiplejer():
    pg.mixer.music.load('LevelUpBeat.mp3')
    pg.mixer.music.play(-1)

    ser = None
    # ARDUINO
    try:
        ser = serial.Serial("/dev/ttyACM0", 9600)  # Open serial port
        print("Serial port opened successfully")
    except serial.SerialException as e:
        print(f"Error: {e}")
    TRESH = 35
    # MAIN GAME

    framecnt = 0
    
    running = True
    while running:
        kontrole = [False, False, False, False]
        kontrole2 = [False, False, False, False]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                elif(event.key == pg.K_w):
                        kontrole[0] = True
                elif(event.key == pg.K_s):
                    kontrole[1] = True
                elif(event.key == pg.K_d):
                    kontrole[2] = True
                elif(event.key == pg.K_a):
                    kontrole[3] = True
                elif(event.key == pg.K_UP):
                        kontrole2[0] = True
                elif(event.key == pg.K_DOWN):
                    kontrole2[1] = True
                elif(event.key == pg.K_RIGHT):
                    kontrole2[2] = True
                elif(event.key == pg.K_LEFT):
                    kontrole2[3] = True
                
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
        akcija2(kontrole2)

        global brojac,perfekt1, perfekt2, gud1, gud2, bed1, bed2 , plsradi
        if perfekt1:
            perfect_score_animation1(player1, 1)
            print("perfect")
            plsradi += 1
        elif gud1:
            good_score_animation1(player1, brojac)
            print("gud")
            plsradi += 1
        elif bed1:
            bad_score_animation1(player1, 1)
            print("bad")
            plsradi += 1
        else:
            idle_animation1(player1, brojac)
            print("idle")
            plsradi = 1
        if perfekt2:
            perfect_score_animation2(player2, 1)
            plsradi2 += 1
        elif gud2:
            good_score_animation2(player2, brojac)
            plsradi2 += 1
        elif bed2:
            bad_score_animation2(player2, 1)
            plsradi2 += 1
        else:
            idle_animation2(player2, brojac)
            plsradi2 = 1
        if(plsradi % 20 == 0):
            perfekt1,  gud1, bed1, = False, False, False
        if(plsradi2 % 20 == 0):
            perfekt2,  gud2, bed2, = False, False, False
        if(framecnt % 20 == 0):
            brojac+=1
        if(brojac >= 2):
            brojac=  0
        glavnestrelice()
        clearstarestrelice()
        clearstarestrelice2()
        drawgore()

        proverizelenekoorde()
        proverizelenekoorde2()

        if framecnt >= 60:
            generisistrelicu()
            generisistrelicu2()
            framecnt = 0

        for x in strel:
            x.update()
            x.draw()

        for x in strel2:
            x.update()
            x.draw()

        pg.display.flip()
        clock.tick(30)
        framecnt += 1
        screen.fill(map)


strel.clear()
strel2.clear()
running = True
print(singlplayer, multiplayer, credits, quituj)
    
while True:
    if singlplayer == False and multiplayer == False and mainmenu == False:
        break
    if mainmenu:
        Mainmenu()
    
    if multiplayer:
        skinselectormulti()
        if mainmenu:
            Mainmenu()
        else:
            skin1 = SkinSelector.skins[SkinSelector.num1]
            skin2 = SkinSelector.skins[SkinSelector.num2]
            ime1 = SkinSelector.user1
            ime2 = SkinSelector.user2
            player1.skin = skin1
            player2.skin = skin2
            player1.name = ime1
            player2.name = ime2
            player1_name_text = font.render(player1.name, True, white)
            player2_name_text = font.render(player2.name, True, white)
            multiplejer()
    
    
    print("single is ", singlplayer)
    if singlplayer:
        print(1)
        skinselectorsingle()
        skinplejera= SkinSelectorSingle.skins[SkinSelectorSingle.num1]
        imeplejera = SkinSelectorSingle.user1
        print(mainmenu)
        if mainmenu:
            Mainmenu()
        else:
            levelselector()
            if mainmenu:
                Mainmenu()
            else:
                skinbosa = levelSelector.levels[levelSelector.num1]
                imebosa = levelSelector.levelname[levelSelector.num1]
                player1.skin = skinplejera
                player1.name = imeplejera
                player2.skin = skinbosa
                player2.name = imebosa
                player1_name_text = font.render(player1.name, True, white)
                player2_name_text = font.render(player2.name, True, white)
                singlplejer()
    running = True
    

if ser is not None:
    ser.close()
pg.quit()
