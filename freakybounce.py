import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
running = True

bob = pg.image.load('freakysmall.jpg')
boblimit = 100
bobstart = 1
bobs = []

class BoB:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

for i in range(bobstart):
    bobs.append(BoB(random.randint(10, 690), random.randint(10, 690), random.randint(1, 10), random.randint(1, 10)))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")

    for i in bobs:
        i.x += i.vx
        i.y += i.vy
        
        if (i.x >= 700):
            i.x = 699
            i.vx = -i.vx
            if (len(bobs) < boblimit):
                bobs.append(BoB(10, random.randint(10, 690), random.randint(1, 10), random.randint(1, 10)))
        if (i.y >= 700):
            i.y = 699
            i.vy = -i.vy
            if (len(bobs) < boblimit):
                bobs.append(BoB(10, random.randint(10, 690), random.randint(1, 10), random.randint(1, 10)))
        if (i.x <= 0):
            i.x = 1
            i.vx = -i.vx
            if (len(bobs) < boblimit):
                bobs.append(BoB(10, random.randint(10, 690), random.randint(1, 10), random.randint(1, 10)))
        if (i.y <= 0):
            i.y = 1
            i.vy = -i.vy
            if (len(bobs) < boblimit):
                bobs.append(BoB(10, random.randint(10, 690), random.randint(1, 10), random.randint(1, 10)))
        screen.blit(bob, (i.x, i.y))
        print(len(bobs))
            
    pg.display.update()

    clock.tick(60)

pg.quit()
