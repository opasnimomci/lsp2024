import pygame as pg
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Character:
    def __init__(self, HP, skin, name, poz):
        self.HP = HP
        self.skin = skin
        self.name = name
        self.poz = poz

idle_goblin = pygame.image.load("goblin.png")
idle_goblin2 = pygame.image.load("goblin_2.png")

idle_bird1 = pygame.image.load("bird_1.png")
idle_bird2 = pygame.image.load("bird_2.png")
bird_perfect = pygame.image.load("bird_perfect.png")
bird_bad = pygame.image.load("bird_bad.png")

idle_yellow_bird1 = pygame.image.load("yellow_bird_1.png")
idle_yellow_bird2 = pygame.image.load("yellow_bird_2.png")

idle_svemirac1 = pygame.image.load("svemirac_1.png")
idle_svemirac2 = pygame.image.load("svemirac_2.png")

idle_demoncina1 = pygame.image.load("demoncina_1.png")
idle_demoncina2 = pygame.image.load("demoncina_2.png")

idle_vojnik1 = pygame.image.load("vojnik_1.png")
idle_vojnik2 = pygame.image.load("vojnik_2.png")

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

def idle_animacija(lik, br):
    Animacije[lik.skin][br] = pygame.transform.scale(Animacije[lik.skin][br], (100, 200))
    screen.blit(Animacije[lik.skin][br], lik.poz)

def perfect_score_animation1(lik, br):
    font = pygame.font.Font(None, 74)
    text = font.render("PERFECT!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pygame.transform.scale(Animacije[lik.skin][br],(100, 200))

def perfect_score_animation2(lik, br):
    font = pygame.font.Font(None, 74)
    text = font.render("PERFECT!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1050, 550))
    screen.blit(text, text_rect)
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pygame.transform.scale(Animacije[lik.skin][br],(100, 200))

def great_score_animation1():
    font = pygame.font.Font(None, 74)
    text = font.render("GOOD!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)

def great_score_animation2():
    font = pygame.font.Font(None, 74)
    text = font.render("GOOD!", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1050, 550))
    screen.blit(text, text_rect)
    
def bad_score_animation1(lik,br):
    font = pygame.font.Font(None, 74)
    text = font.render("BAD", True, (200, 255, 255))
    text_rect = text.get_rect(center=(150, 550))
    screen.blit(text, text_rect)
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pygame.transform.scale(Animacije[lik.skin][br],(100, 200))

def bad_score_animation2(lik, br):
    font = pygame.font.Font(None, 74)
    text = font.render("BAD", True, (200, 255, 255))
    text_rect = text.get_rect(center=(1050, 550))
    screen.blit(text, text_rect)
    Animacije[lik.skin][br]= pygame.transform.scale(Animacije[lik.skin][br],(100, 200))




    

clock = pygame.time.Clock()
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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



    idle_animacija(lik1, br)
    idle_animacija(lik2, br)

    frame_count += 1
    if frame_count % 30 == 0:  
        br = 1 - br


    if perfect_score_hit1:
        perfect_score_animation1(lik3, br)

    if perfect_score_hit2:
        perfect_score_animation2(lik4, br)

    if great_score_hit1:
        great_score_animation1()

    if great_score_hit2:    
        great_score_animation2()

    if bad_score_hit1:
        bad_score_animation1(lik5, br)
    if bad_score_hit2:
        bad_score_animation2(lik6,br)

    pygame.display.update()
    clock.tick(60)  

pygame.quit()
sys.exit()
