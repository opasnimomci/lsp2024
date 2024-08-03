import pygame as pg
import sys

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Character:
    def __init__(self, HP, skin, name, poz):
        self.HP = HP
        self.skin = skin
        self.name = name
        self.poz = poz

idle_goblin = pg.image.load("goblin.png")
idle_goblin2 = pg.image.load("goblin_2.png")

idle_bird1 = pg.image.load("bird_1.png")
idle_bird2 = pg.image.load("bird_2.png")
bird_perfect = pg.image.load("bird_perfect.png")
bird_bad = pg.image.load("bird_bad.png")

idle_yellow_bird1 = pg.image.load("yellow_bird_1.png")
idle_yellow_bird2 = pg.image.load("yellow_bird_2.png")

idle_svemirac1 = pg.image.load("svemirac_1.png")
idle_svemirac2 = pg.image.load("svemirac_2.png")

idle_demoncina1 = pg.image.load("demoncina_1.png")
idle_demoncina2 = pg.image.load("demoncina_2.png")

idle_vojnik1 = pg.image.load("vojnik_1.png")
idle_vojnik2 = pg.image.load("vojnik_2.png")

Animacije = {
    
    "goblin": [idle_goblin, idle_goblin2],
    #"goblin_perfect" : [idle_goblin, goblin_perfect],
    #"goblin_bad" : [idle_goblin, goblin_bad],
    
    "bird": [idle_bird1, idle_bird2],
    "bird_perfect": [idle_bird1, bird_perfect],
    "bird_bad": [idle_bird2, bird_bad],
    
    "yellow bird": [idle_yellow_bird1, idle_yellow_bird2],
    #"yellow bird_perfect": [idle_yellow_bird1, yellow_bird_perfect],
    #"yellow bird_bad": [idle_yellow_bird1, yellow_bird_bad],
    
    "svemirac": [idle_svemirac1, idle_svemirac2],
    #"svemirac_bad" : [idle_svemirac1, svemirac_bad],
    #"svemrac_perfect": [idle_svemirac1, svemirac_perfect],
    
    "demon": [idle_demoncina1, idle_demoncina2],
    #"demon_bad": [idle_demoncina1, demon_bad],
    #"demon_perfect": [idle_demoncina1, demon_perfect],
    
    "vojnik": [idle_vojnik1, idle_vojnik2],
    #"vojnik_bad": [idle_vojnik1, vojnik_bad],
    #"vojnik_perfect": [idle_vojnik1, vojnik_perfect]
    
}

def perfect_score_animation1(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("PERFECT!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pg.transform.scale(Animacije[lik.skin][br],(100, 200))
    screen.blit(Animacije[lik.skin][br], lik.poz)

def perfect_score_animation2(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("PERFECT!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1050, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pg.transform.scale(Animacije[lik.skin][br],(100, 200))
    screen.blit(Animacije[lik.skin][br], lik.poz)

def great_score_animation1(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("GOOD!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][br] = pg.transform.scale(Animacije[lik.skin][br], (100, 200))
    screen.blit(Animacije[lik.skin][br], lik.poz)
    

def great_score_animation2(lik,br):
    font = pg.font.Font(None, 74)
    text = font.render("GOOD!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1050, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][br] = pg.transform.scale(Animacije[lik.skin][br], (100, 200))
    screen.blit(Animacije[lik.skin][br], lik.poz)
    
def bad_score_animation1(lik,br):
    font = pg.font.Font(None, 74)
    text = font.render("BAD", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pg.transform.scale(Animacije[lik.skin][br],(100, 200))
    screen.blit(Animacije[lik.skin][br], lik.poz)

def bad_score_animation2(lik, br):
    font = pg.font.Font(None, 74)
    text = font.render("BAD", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1050, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pg.transform.scale(Animacije[lik.skin][br],(100, 200))
    screen.blit(Animacije[lik.skin][br], lik.poz)




    

clock = pg.time.Clock()
br = 0
frame_count = 0
lik1 = Character(50, "bird", "rump", (100, 575))
lik2 = Character(50, "vojnik", "baldy", (1000, 575))
lik3 = Character(50, "bird_perfect", "rump", (100, 575))
lik4 = Character(50, "vojnik", "baldy", (1000, 575))
lik5 = Character(50, "bird_bad", "rump", (100, 575))
lik6 = Character(50, "vojnik", "baldy", (1000, 575))

running = True
perfect_score_hit1 = False
perfect_score_hit2 = False
great_score_hit1 = False
great_score_hit2 = False
bad_score_hit1  = False
bad_score_hit2 = False

while running:
    screen.fill("white")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if (frame_count == 120):  
        perfect_score_hit1 = True
        perfect_score_hit2 = False
        great_score_hit1 = False
        great_score_hit2 = False
        bad_score_hit1  = False
        bad_score_hit2 = False
    if frame_count == 180:
        perfect_score_hit2 = True  
        great_score_hit1 = False
        perfect_score_hit1 = False
        great_score_hit2 = False
        bad_score_hit1  = False
        bad_score_hit2 = False

    if frame_count == 60:
        perfect_score_hit2 = False 
        great_score_hit1 = True
        perfect_score_hit1 = False
        great_score_hit2 = False
        bad_score_hit1  = False
        bad_score_hit2 = False
    if frame_count == 240:
        perfect_score_hit2 = False 
        great_score_hit1 = False
        perfect_score_hit1 = False
        great_score_hit2 = True
        bad_score_hit1  = False
        bad_score_hit2 = False
    if frame_count == 300:
        perfect_score_hit2 = False 
        great_score_hit1 = False
        perfect_score_hit1 = False
        great_score_hit2 = False
        bad_score_hit1  = True
        bad_score_hit2 = False
    if frame_count == 240:
        perfect_score_hit2 = False 
        great_score_hit1 = False
        perfect_score_hit1 = False
        great_score_hit2 = False
        bad_score_hit1  = False
        bad_score_hit2 = True



    

    frame_count += 1
    if frame_count % 30 == 0:  
        br = 1 - br



    if perfect_score_hit1:
        perfect_score_animation1(lik3, br)

    if perfect_score_hit2:
        perfect_score_animation2(lik4, br)
    if great_score_hit1:
        great_score_animation1(lik1, br)
    

    if great_score_hit2:    
        great_score_animation2(lik2, br)

    if bad_score_hit1:
        bad_score_animation1(lik5, br)
    if bad_score_hit2:
        bad_score_animation2(lik6,br)

    pg.display.update()
    clock.tick(60)  

pg.quit()
sys.exit()

