import pygame as pg

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
clock = pg.time.Clock()
running = True

##mapa
map = "white"

bob = pg.image.load('freaky.jpg')

class SkinSelectorSingle:
    def __init__ (self, user1, active1, R, num1, skinnum, skins, skinname):
        self.user1 = user1
        self.active1 = active1
        self.R = R
        self.num1 = num1
        ##broj skinova i skinovi i imena skinova
        self.skinnum = skinnum
        self.skins = skins
        self.skinname = skinname

    def DrawSkinSelector(self):
        mpos = pg.mouse.get_pos()
        font = pg.font.Font("freesansbold.ttf", 100)
        font2 = pg.font.Font("freesansbold.ttf", 40)

        pg.draw.rect(screen, "black", (810, 500, 300, 450), 5)

        if (mpos[0] >= 600 and mpos[0] <= 1320 and mpos[1] <= 250 and mpos[1] >= 50):
            pg.draw.rect(screen, "gray", (600, 50, 720, 200), 0, 25)
        else:
            pg.draw.rect(screen, "black", (600, 50, 720, 200), 0, 25)
        textP = font.render("Play", True, "white")
        RectP = textP.get_rect()
        RectP.center = (960, 150)
        screen.blit(textP, RectP)

        self.input_rect1 = pg.Rect(760, 300, 400, 100)
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

        skincen1 = pg.Rect(0, 0, 100, 100)
        skincen1.center = (960, 725)
        ##crta skin levo
        if (self.num1 != 5):
            pg.draw.rect(screen, self.skins[self.num1], skincen1)
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
        

    def DetectClick(self):
        mpos = pg.mouse.get_pos()
        if (mpos[0] >= 600 and mpos[0] <= 1320 and mpos[1] <= 250 and mpos[1] >= 50):
            self.R = True
        if self.input_rect1.collidepoint(mpos):
            self.active1 = True
        else:
            self.active1 = False

SkinSelectorSingle = SkinSelectorSingle("", False, False, 0, 5, ["red", "blue", "yellow", "green", "purple"], ["red", "blue", "yellow", "green", "purple"])

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                SkinSelectorSingle.DetectClick()
                if (SkinSelectorSingle.R):
                    running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                if SkinSelectorSingle.active1:
                    SkinSelectorSingle.user1 = SkinSelectorSingle.user1[:-1]
            elif SkinSelectorSingle.active1:
                if SkinSelectorSingle.active1:
                    SkinSelectorSingle.user1 += event.unicode
            elif event.key == pg.K_a:
                if SkinSelectorSingle.num1 == 0:
                    SkinSelectorSingle.num1 = SkinSelectorSingle.skinnum
                else:
                    SkinSelectorSingle.num1 -= 1
            elif event.key == pg.K_d:
                if SkinSelectorSingle.num1 == SkinSelectorSingle.skinnum:
                    SkinSelectorSingle.num1 = 0
                else:
                    SkinSelectorSingle.num1 += 1
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

    SkinSelectorSingle.DrawSkinSelector()

    pg.display.update()

    clock.tick(60)

#username
print(SkinSelectorSingle.user1)

pg.quit()
