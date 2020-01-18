import pygame
pygame.init()
pygame.font.init()

pygame.display.set_caption("Bird Clicker")

win = pygame.display.set_mode((500, 500))

f1 = pygame.image.load('./assets/f1.png')
f2 = pygame.image.load('./assets/f2.png')
icon = pygame.image.load('./assets/Icon.png')
icons = pygame.transform.scale(icon, (250,250))
breeder = pygame.image.load('./assets/breeder.png')
breeders = pygame.transform.scale(breeder, (250,250))
aicon = pygame.image.load('./assets/AVI2.png')
aicons = pygame.transform.scale(aicon, (125,125))

avery_points = 0
avery_cost = 100
a_increment = 1

breeder_points = 0
breeder_cost = 10
increment = 1


points = 0

background = f1

white = (255, 255, 255)
black = (0, 0, 0)

def print_points():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw = font.render(f"{int(points)}", True, white, (0, 183, 255))
    WintextRect = WinDraw.get_rect()
    WintextRect.center = (100, 250)
    win.blit(WinDraw, WintextRect)

def print_bpoints():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw2 = font.render(f"{breeder_points}", True, white, (0, 183, 255))
    WintextRect2 = WinDraw2.get_rect()
    WintextRect2.center = (350, 365)
    win.blit(WinDraw2, WintextRect2)

def print_apoints():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"{avery_points}", True, white, (0, 183, 255))
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (320, 435)
    win.blit(WinDraw3, WintextRect3)


pos = 0

timer = 0

timer2 = 0

height = 150

while True:
    pygame.time.delay(30)

    win.blit(background,(0,0))
    win.blit(icons,(125,height))
    win.blit(breeders, (135,250))
    win.blit(aicons, (190,375))

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if points >= breeder_cost:
                            breeder_points += 1
                            points -= breeder_cost
                        print(breeder_cost)
                    if event.key == pygame.K_RSHIFT:
                        if points >= avery_cost:
                            avery_points += 1
                            points -= avery_cost
                if pygame.mouse.get_pressed()[0]:
                    points += 1
                    height = 125
                else:
                    height = 150

    if breeder_points == 0:
        breeder_cost = 10

    if timer >= 10:
        pos += 1
        timer = 0

    if timer2 >= 15:
        points += 1 * breeder_points
        points += 10 * avery_points
        timer2 = 0

    if breeder_points > 0:
        increment = breeder_points * 1.5

    breeder_cost = 10 * round(increment)

    if avery_points > 0:
        a_increment = avery_points * 1.5

    avery_cost = 100 * round(a_increment)

    timer += 1

    timer2 += 1

    if pos == 0:
        background = f1

    if pos == 1:
        background = f2

    if pos == 3:
        pos = 0
        timer = 0

    print_points()
    print_bpoints()
    print_apoints()

    pygame.display.update()