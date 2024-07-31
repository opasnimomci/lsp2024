import pygame as pg

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
clock = pg.time.Clock()
running = True

class SkinSelector:
    def DrawSkinSelector(self):
        pg.draw.rect(screen, "black", (100, 100, 100, 100))

SkinSelector = SkinSelector()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    SkinSelector.DrawSkinSelector()

    pg.display.update()

    clock.tick(60)

pg.quit()
