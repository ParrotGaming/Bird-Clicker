import pygame
pygame.init()
pygame.font.init()

pygame.display.set_caption("Bird Clicker")

win = pygame.display.set_mode((500, 500))

f1 = pygame.image.load('./assets/f1.png')
f2 = pygame.image.load('./assets/f2.png')
icon = pygame.image.load('./assets/Icon.png')
icons = pygame.transform.scale(icon, (250,250))

points = 0

background = f1

white = (255, 255, 255)
black = (0, 0, 0)

def print_points():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw = font.render(f"{points}", True, white, black)
    WintextRect = WinDraw.get_rect()
    WintextRect.center = (100, 250)
    win.blit(WinDraw, WintextRect)

pos = 0

timer = 0

height = 150

while True:
    pygame.time.delay(30)

    win.blit(background,(0,0))
    win.blit(icons,(125,height))

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        height = 125
                        points += 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        height = 150

    if timer >= 10:
        pos += 1
        timer = 0

    timer += 1

    if pos == 0:
        background = f1

    if pos == 1:
        background = f2

    if pos == 3:
        pos = 0
        timer = 0

    print_points()

    pygame.display.update()