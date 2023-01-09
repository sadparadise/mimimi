import pygame, sys, random

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("mimimi")

clock = pygame.time.Clock()

bg_color = [0, 0, 0]

sqr_size = int(width/20)

head_pos = [int(width/2), int(height/2)]
body = [[[int(width/2), int(height/2)], 0]]         # each element of the list is an array keeping the position of one of the body parts and a
head_color = [255, 0, 255]                          # number telling which direction the part must follow in the iteration:
body_color = [0, 0, 255]                            # 0 - right, 1 - up, 2 - left, 3 - down

speed = sqr_size
direction = 0

fruit_pos = [random.randint(0,19) * 25, random.randint(0,19) * 25]
fruit_color = [255, 0, 0]

while True:
    dt = clock.tick(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_UP:
                direction = 1
            if event.key == pygame.K_LEFT:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3

    for i in range(len(body)-1, 0, -1):               # sets the direction followed by part to the one followed by the part before it in the
        body[i][1] = body[i-1][1]                     # previous iteration (frame, tick, anything...)
    body[0][1] = direction
    
    for part in body:
        if part[1] == 0:
            part[0][0] += speed
        if part[1] == 1:
            part[0][1] -= speed
        if part[1] == 2:
            part[0][0] -= speed
        if part[1] == 3:
            part[0][1] += speed

    if body[0][0][0] == fruit_pos[0] and body[0][0][1] == fruit_pos[1]:
        if body[-1][1] == 0:
            body.append([[body[-1][0][0] + sqr_size, body[-1][0][1]], 0])
        if body[-1][1] == 1:
            body.append([[body[-1][0][0], body[-1][0][1] + sqr_size], 1])
        if body[-1][1] == 2:
            body.append([[body[-1][0][0] - sqr_size, body[-1][0][1]], 2])
        if body[-1][1] == 3:
            body.append([[body[-1][0][0], body[-1][0][1] - sqr_size], 3])
        fruit_pos = [random.randint(0,20) * 25, random.randint(0,20) * 25]

    screen.fill(bg_color)
    for part in body[1:]:
        pygame.draw.rect(screen, body_color, part[0] + [sqr_size] * 2)
    pygame.draw.rect(screen, head_color, body[0][0] + [sqr_size] * 2)
    pygame.draw.rect(screen, fruit_color, fruit_pos + [sqr_size] * 2)
    pygame.display.update()
