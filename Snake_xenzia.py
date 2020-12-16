import pygame
import pygame.freetype
import os
import time
import random

pygame.init()

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts", "game.ttf")
font_size = 15
pygame.freetype.init()
my_font = pygame.freetype.Font(font_path, font_size)

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 500
dis_height = 300

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
apple_rad = 3
move = 10


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def stats(your_score):
    my_font.render_to(dis, (4, 4), "Your score:" + str(your_score), black, None, size=64)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 15, dis_height / 10])


def score(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 15, dis_height / 10])

def gameLoop(move, snake_speed):
    boundary = 1
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1


    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10

    while not game_over:
        your_score = 0
        stats(your_score)


        while game_close == True:
            dis.fill(green)
            message("You Lost! Press C-Play Again or Q-Quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        snake_speed = 15
                        gameLoop(move, snake_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -move
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = move
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -move
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = move
                    x1_change = 0


        if boundary == 1:
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

        if len(snake_List) == 4:
            boundary = 0

        if boundary == 0:
            if x1 > dis_width:
                x1 = 0

            if x1 < 0:
                x1 = dis_width

            if y1 == dis_height:
                y1 = 0

            if y1 < 0:
                y1 = dis_height


        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.circle(dis, red, [foodx, foody], apple_rad)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            your_score += 1
            snake_speed += 1
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            Length_of_snake += 1
            message("You Lost! Press C-Play Again or Q-Quit", red)


        clock.tick(snake_speed)

       # pygame.quit()
        #quit()


gameLoop(move, snake_speed)