import pygame as pg
import random

pg.init()
W, H = 1280, 720
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
running = True
w, h = 100, 100
r, t = 20, 50
c = 0
vy = 5
L1 = []
L2 = []
L3 = []
L4 = []

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    """if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                
            if event.key == pg.K_d:"""

    c += 1
    if c == 50:  
        n = random.randint(1, 4)
        print(n)
        c = 0
        if (n == 1):
            L1.append(H - h)
        if (n == 2):
            L2.append(H - h)
        if (n == 3):
            L3.append(H - h)
        if (n == 4):
            L4.append(H - h)

    screen.fill("black")
    pg.draw.rect(screen, "gray", (W / 2 - 1.5 * r - 2 * w, t, w, h))
    pg.draw.rect(screen, "gray", (W / 2 - 0.5 * r - w, t, w, h))
    pg.draw.rect(screen, "gray", (W / 2 + 0.5 * r, t, w, h))
    pg.draw.rect(screen, "gray", (W / 2 + 1.5 * r + w, t, w, h))

    s = 0
    for i in range(len(L1)):
        L1[i - s] -= vy
        pg.draw.rect(screen, "purple", (W / 2 - 1.5 * r - 2 * w, L1[i - s], w, h))
        if L1[i - s] < -110:
            L1.pop(i - s)
            s += 1
    s = 0
    for i in range(len(L2)):
        L2[i - s] -= vy
        pg.draw.rect(screen, "blue", (W / 2 - 0.5 * r - w, L2[i - s], w, h))
        if L2[i - s] < -110:
            L2.pop(i - s)
            s += 1
    s = 0
    for i in range(len(L3)):
        L3[i - s] -= vy
        pg.draw.rect(screen, "green", (W / 2 + 0.5 * r, L3[i - s], w, h))
        if L3[i - s] < -110:
            L3.pop(i - s)
            s += 1
    s = 0
    for i in range(len(L4)):
        L4[i - s] -= vy
        pg.draw.rect(screen, "red", (W / 2 + 1.5 * r + w, L4[i - s], w, h))
        if L4[i - s] < -110:
            L4.pop(i - s)
            s += 1
    

    pg.display.flip()

    clock.tick(60)

pg.quit()