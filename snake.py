import pygame
import random
import time

pygame.init()

dis_width = 500
dis_height = 500

black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red2 = (250, 128, 114)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 50)

def Your_score(score):
    value = score_font.render("Your Score:" + str(score), True,yellow)
    dis.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        leght_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_DOWN:
                        x1_change = snake_block
                        y1_change = 0

            x1 += x1_change
            y1 += y1_change

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_over = True

            if not game_over:
                dis.fill(black)
                pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                snake_head = []
                snake_head.append(x1)
                snake_head.append(y1)
                snake_list.append(snake_head)
                if len(snake_list) > leght_of_snake:
                    del snake_list[0]

                for x in snake_list[:-1]:
                    if x == snake_head:
                        game_over = True

                our_snake(snake_block, snake_list)
                Your_score(leght_of_snake -1)

                pygame.display.update()

                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    lenght_of_snake += 1

                clock.tick(snake_speed)

    dis.fill(red2)
    message("YOU LOST! YOUR SCORE:" + str(lenght_of_snake - 1), black)
    pygame.display.update()
    time,sleep(2)

while True:
    try:
        gameLoop()
    except Exception as e:

        pygame.quit()
        break



        

                    














