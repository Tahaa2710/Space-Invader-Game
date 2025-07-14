import pygame
import random
import math
from pygame import mixer



pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

pygame.display.set_caption("  SPACE  ")
icon = pygame.image.load('ufo (4).png')
pygame.display.set_icon(icon)
player_image = pygame.image.load('space-invaders (1).png')
player_X = 400
player_Y = 500
new_player_X = 0



monster_image = pygame.image.load('monster.png')
monster_image_X = random.randint(0, 800)
monster_image_Y = random.randint(50, 200)
new_monster_image_X = 6
new_monster_image_Y = 40

background = pygame.image.load('background.png')

bullet = pygame.image.load('bullet (1).png')
bullet_x = 0
bullet_Y = 480
bullet_change_x = 0
bullet_change_y = 15
bullet_state = "rest"

count = 0
font = pygame.font.Font("freesansbold.ttf",26)

text_X = 10
text_Y = 10

over_X = 390
over_Y = 300

def player(x, y):
    screen.blit(player_image, (x, y))


def monster(x, y):
    screen.blit(monster_image, (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x, y))


def collision_occur(bullet_x, bullet_Y, monster_image_Y, monster_image_X):
    distance = math.sqrt(math.pow(monster_image_X - bullet_x, 2) + (math.pow(monster_image_Y - bullet_Y, 2)))
    if distance < 27:
        return True
    else:
        return False

def score_display(x,y):
    score = font.render("SCORE : " + str(count) , True , (255,255,255))
    screen.blit(score,(x,y))

def game_over(x,y):
    game_is_over = font.render("GAME OVER ", True , (0,255,255))
    screen.blit(game_is_over,(x,y))
    score_total = font.render("your score is " + str(count), True, (0, 255, 255))
    screen.blit(score_total,(x,y+30))

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            count = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_player_X = -10
            if event.key == pygame.K_RIGHT:
                new_player_X = 10
            if event.key == pygame.K_SPACE:
                if bullet_state == "rest":
                    bullet_x = player_X
                    bullet_fire(bullet_x, bullet_Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                new_player_X = 0

    player_X = player_X + new_player_X
    monster_image_X = monster_image_X + new_monster_image_X

    if player_X >= 736:
        player_X = 736
    elif player_X <= 0:
        player_X = 0

    if monster_image_X <= 0:
        new_monster_image_X = abs(new_monster_image_X)
        monster_image_X = 0
    elif monster_image_X >= 736:
        new_monster_image_X = -abs(new_monster_image_X)
        monster_image_X = 736

    if monster_image_X <= 0:
        monster_image_Y += new_monster_image_Y
    elif monster_image_X >= 736:
        monster_image_Y += new_monster_image_Y

    if bullet_state == "fire":
        bullet_fire(bullet_x, bullet_Y)
        bullet_Y = bullet_Y - bullet_change_y


    if bullet_Y <= 0:
        bullet_Y = 480
        bullet_state = "rest"
        


    collision = collision_occur(bullet_x, bullet_Y, monster_image_Y, monster_image_X)
    if collision:
       
        bullet_Y = 480
        bullet_state = "rest"
        monster_image_X = random.randint(0, 800)
        monster_image_Y = random.randint(50, 200)
        count = count + 1

        new_monster_image_X = 6 + (count // 3)
        if new_monster_image_X > 20:
            new_monster_image_X = 22

        print(count)



    score_display(text_X,text_Y)
    player(player_X, player_Y)

    if monster_image_Y >= 400:
        game_over(over_X,over_Y)
        monster_image_Y = 20000
    monster(monster_image_X, monster_image_Y)

    pygame.display.update()



