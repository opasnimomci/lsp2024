import pygame as pg

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
clock = pg.time.Clock()
running = True

##mapa
map = "white"

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

        """pg.draw.rect(screen, "black", (550, 625, 820, 50))
        pg.draw.rect(screen, "black", (550, 675, 820, 150), 5)
        pg.draw.line(screen, "black", (755, 675), (755, 824), 5)
        pg.draw.line(screen, "black", (960, 675), (960, 824), 5)
        pg.draw.line(screen, "black", (1165, 675), (1165, 824), 5)"""

        if (mpos[0] >= 600 and mpos[0] <= 1320 and mpos[1] <= 250 and mpos[1] >= 50):
            pg.draw.rect(screen, "gray", (600, 50, 720, 200), 0, 25)
        else:
            pg.draw.rect(screen, "black", (600, 50, 720, 200), 0, 25)
        textP = font.render("Play", True, "white")
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
        pg.draw.rect(screen, self.skins[self.num1], skincen1)
        textskin1 = font2.render(self.skinname[self.num1], True, "black")
        Rect1 = textskin1.get_rect()
        Rect1.center = (300, 1000)
        screen.blit(textskin1, Rect1)

        skincen2 = pg.Rect(0, 0, 100, 100)
        skincen2.center = (1620, 725)
        ##crta skin desno
        pg.draw.rect(screen, self.skins[self.num2], skincen2)
        textskin2 = font2.render(self.skinname[self.num2], True, "black")
        Rect2 = textskin2.get_rect()
        Rect2.center = (1620, 1000)
        screen.blit(textskin2, Rect2)
        

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

SkinSelector = SkinSelector("", "", False, False, False, 0, 0, 5, ["red", "blue", "yellow", "green", "purple"], ["red", "blue", "yellow", "green", "purple"])

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                SkinSelector.DetectClick()
                if (SkinSelector.R):
                    running = False
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
                    SkinSelector.num1 = SkinSelector.skinnum - 1
                else:
                    SkinSelector.num1 -= 1
            elif event.key == pg.K_d:
                if SkinSelector.num1 == SkinSelector.skinnum - 1:
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

    screen.fill(map)

    SkinSelector.DrawSkinSelector()

    pg.display.update()

    clock.tick(60)

#usernamovi
print(SkinSelector.user1, SkinSelector.user2)

pg.quit()
