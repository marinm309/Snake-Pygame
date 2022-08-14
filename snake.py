import pygame
import random
import os
import time

pygame.font.init()
icon = pygame.image.load('snake.png')
time1 = time.time()
rec_x = 380
rec_y = 210
move_x = 5
move_y = 5
vel_x = 0
vel_y = 0
food_x = 0
food_y = 0
score = 0
score_add = 0
x_change = True
y_change = True
move = False
new_food = True
game_over = False
check = os.path.isfile('SCORES.txt')
if not check:
    f = open('SCORES.txt', 'w')
    f.close()


def snake(x, y):
    pygame.draw.rect(screen, (100, 255, 100), (x + 5, y + 5, 50, 50))


def food(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 60, 60))


def show_score(x, y):
    display_score = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(display_score, (x, y))


at = []
lst = [[(0, 0), (60, 0), (120, 0), (180, 0), (240, 0), (300, 0), (360, 0), (420, 0), (480, 0), (540, 0)],
       [(0, 60), (60, 60), (120, 60), (180, 60), (240, 60), (300, 60), (360, 60), (420, 60), (480, 60), (540, 60)],
       [(0, 120), (60, 120), (120, 120), (180, 120), (240, 120), (300, 120), (360, 120), (420, 120), (480, 120),
        (540, 120)],
       [(0, 180), (60, 180), (120, 180), (180, 180), (240, 180), (300, 180), (360, 180), (420, 180), (480, 180),
        (540, 180)],
       [(0, 240), (60, 240), (120, 240), (180, 240), (240, 240), (300, 240), (360, 240), (420, 240), (480, 240),
        (540, 240)],
       [(0, 300), (60, 300), (120, 300), (180, 300), (240, 300), (300, 300), (360, 300), (420, 300), (480, 300),
        (540, 300)],
       [(0, 360), (60, 360), (120, 360), (180, 360), (240, 360), (300, 360), (360, 360), (420, 360), (480, 360),
        (540, 360)],
       [(0, 420), (60, 420), (120, 420), (180, 420), (240, 420), (300, 420), (360, 420), (420, 420), (480, 420),
        (540, 420)],
       [(0, 480), (60, 480), (120, 480), (180, 480), (240, 480), (300, 480), (360, 480), (420, 480), (480, 480),
        (540, 480)],
       [(0, 540), (60, 540), (120, 540), (180, 540), (240, 540), (300, 540), (360, 540), (420, 540), (480, 540),
        (540, 540)]]

pygame.init()
pygame.font.init()
pygame.display.set_caption('Snake')
pygame.display.set_icon(icon)
font = pygame.font.Font("freesansbold.ttf", 32)
font1 = pygame.font.Font("freesansbold.ttf", 16)
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
while True:
    time2 = time.time()
    a = pygame.time.wait(200)
    b = pygame.time.get_ticks()
    c = b // 300
    d = 0
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and c != d:
            if event.key == pygame.K_SPACE and game_over:
                rec_x = 380
                rec_y = 210
                move_x = 5
                move_y = 5
                vel_x = 0
                vel_y = 0
                food_x = 0
                food_y = 0
                score = 0
                score_add = 0
                x_change = True
                y_change = True
                move = False
                new_food = True
                game_over = False
                timer = 0
                time1 = time2
            if event.key == pygame.K_LEFT and vel_x == 0 and not game_over:
                vel_x = -1
                vel_y = 0
                d = c
            if event.key == pygame.K_RIGHT and vel_x == 0 and not game_over:
                vel_x = 1
                vel_y = 0
                d = c
            if event.key == pygame.K_UP and vel_y == 0 and not game_over:
                vel_y = -1
                vel_x = 0
                d = c
            if event.key == pygame.K_DOWN and vel_y == 0 and not game_over:
                vel_y = 1
                vel_x = 0
                d = c
    if new_food:
        food_x = random.choice(lst)
        food_y = random.choice(lst)
        food_x = random.choice(food_x)[0]
        food_y = random.choice(food_y)[1]
        new_food = False
    move_x += vel_x
    move_y += vel_y
    if move_x == -1:
        move_x = 9
    if move_y == -1:
        move_y = 9
    if move_x == 10:
        move_x = 0
    if move_y == 10:
        move_y = 0
    rec_x = lst[move_y][move_x][0]
    rec_y = lst[move_y][move_x][1]
    at.append((rec_x, rec_y))
    if rec_x == food_x and rec_y == food_y:
        new_food = True
        score += 1
    if score >= 1:
        for i in range(2, score + 2):
            a = (at[-i][0], at[-i][1])
            b = (rec_x, rec_y)
            snake(at[-i][0], at[-i][1])
            if (rec_x, rec_y) == (at[-i][0], at[-i][1]) or (rec_x, rec_y) == (at[-i - 1][0], at[-i - 1][1]):
                game_over = True
                pygame.draw.rect(screen, (255, 50, 50), (rec_x, rec_y, 60, 60))
                vel_x = 0
                vel_y = 0
                score_add += 1
                if score_add == 1:
                    with open('SCORES.txt', 'a') as add_score:
                        add_score.write(f'Score: {score} --- Time: {timer:.1f}\n')
                screen.blit(font.render(f'GAME OVER', True, (255, 255, 255)), (200, 268))
                screen.blit(font1.render(f'PRESS SPACE TO RESTART', True, (255, 255, 255)), (190, 297))
    food(food_x, food_y)
    if not game_over:
        timer = time2 - time1
        pygame.draw.rect(screen, (0, 255, 0), (rec_x, rec_y, 60, 60))
        screen.blit(font.render(f'Time: {timer:.1f}', True, (255, 255, 255)), (420, 10))
    if game_over:
        screen.blit(font.render(f'Time: {timer:.1f}', True, (255, 255, 255)), (420, 10))
    show_score(10, 10)
    pygame.display.flip()
    clock.tick(60)
