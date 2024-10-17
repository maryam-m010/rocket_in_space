import pygame, sys, time

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("rocket in space")
screen.fill("white")

player_x = 200
player_y = 200

bg = pygame.image.load("space.png")
player = pygame.image.load("spaceship.png")

pygame.display.update()

keys = [False, False, False, False]

while player_y < 600:
    screen.blit(bg, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_DOWN:
                keys[1] = True
            if event.key == pygame.K_LEFT:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_DOWN:
                keys[1] = False
            if event.key == pygame.K_LEFT:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False
            
    if keys[0]:
        if player_y > 0:
            player_y -= 7

    if keys[1]:
        if player_y < 450:
            player_y += 7

    if keys[2]:
        if player_x > 0:
            player_x -= 7

    if keys[3]:
        if player_x < 450:
            player_x += 7

    player_y += 5
    time.sleep(0.05)

print("GAME OVER!!")