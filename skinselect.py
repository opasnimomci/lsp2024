import pygame as pg

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
clock = pg.time.Clock()
running = True

class SkinSelector:
    def DrawSkinSelector(self):
        mpos = pg.mouse.get_pos()
        font = pg.font.Font("freesansbold.ttf", 100)

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

        input_rect1 = pg.Rect(100, 250, 400, 100)
        color_active = pg.Color('gray')
        color_passive = pg.Color('white')
        active1 = False
        color = color_passive
        pg.draw.rect(screen, "black", (100, 250, 400, 100), 5)
        pg.draw.rect(screen, "black", (1420, 250, 400, 100), 5)

    def DetectClick(self):
        mpos = pg.mouse.get_pos()
        if (mpos[0] >= 600 and mpos[0] <= 1320 and mpos[1] <= 250 and mpos[1] >= 50):
            self.R = True

SkinSelector = SkinSelector()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                SkinSelector.DetectClicks()
                if (SkinSelector.R):
                    running = False

    screen.fill("white")
    SkinSelector.DrawSkinSelector()

    pg.display.update()

    clock.tick(60)

pg.quit()
