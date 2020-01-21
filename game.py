import pygame
pygame.init()
pygame.font.init()

pygame.display.set_caption("Bird Clicker")

win = pygame.display.set_mode((500, 500))

bw = 200
bh = 200
bx = 50
by = 50

aw = 90
ah = 90
ax = 300
ay = 95

f1 = pygame.image.load('./assets/f1.png')
f2 = pygame.image.load('./assets/f2.png')
icon = pygame.image.load('./assets/Icon.png')
icons = pygame.transform.scale(icon, (250,250))
moontro = pygame.image.load('./assets/moon_trophy.png')
breeder = pygame.image.load('./assets/breeder.png')
breeders = pygame.transform.scale(breeder, (bw,bh))
aicon = pygame.image.load('./assets/AVI2.png')
aicons = pygame.transform.scale(aicon, (aw,ah))

avery_points = 0
avery_cost = 100
a_increment = 1

px = 1

moon = False

breeder_points = 0
breeder_cost = 10
increment = 1

start = True

trophy = False

store = False

selection1 = "start"
selection2 = "quit"
ss1 = False
ss2 = False

points = 0

background = f1

txtbr = (0, 183, 255)

white = (255, 255, 255)

def print_points():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw = font.render(f"{int(points)}", True, white, txtbr)
    WintextRect = WinDraw.get_rect()
    WintextRect.center = (100, 250)
    win.blit(WinDraw, WintextRect)

def print_bpoints():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw2 = font.render(f"{breeder_points}", True, white, txtbr)
    WintextRect2 = WinDraw2.get_rect()
    WintextRect2.center = (225, 145)
    win.blit(WinDraw2, WintextRect2)

def print_apoints():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"{avery_points}", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (400, 145)
    win.blit(WinDraw3, WintextRect3)

def print_start():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"{selection1}", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (250, 225)
    win.blit(WinDraw3, WintextRect3)

def print_quit():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"{selection2}", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (250, 300)
    win.blit(WinDraw3, WintextRect3)


pos = 0

timer = 0

timer2 = 0

timer3 = 0

height = 150

while True:
    pygame.time.delay(30)

    win.blit(background,(0,0))

    breeders = pygame.transform.scale(breeder, (bw,bh))

    if start == False and store == False and trophy == False:
        win.blit(icons,(125,height))

    press = False

    motion = False

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    motion = True
                    if event.key == pygame.K_RETURN:
                        if start == False and store == True:
                            if px == 1:
                                if points >= breeder_cost:
                                    breeder_points += 1
                                    points -= breeder_cost
                                print(breeder_cost)
                            if px == 2:
                                if points >= avery_cost:
                                    avery_points += 1
                                    points -= avery_cost
                        if start:
                            if ss1:
                                start = False
                            if ss2:
                                pygame.display.quit()
                    if event.key == pygame.K_ESCAPE:
                        if store == False and trophy == False:
                            start = True
                            selection1 = "start"
                            selection2 = "quit"
                            ss1 = False
                            ss2 = False
                        if store == True and trophy == False:
                            store = False
                        if trophy == True and store == False:
                            trophy = False
                    if event.key == pygame.K_UP:
                        if start == True:
                            ss1 = True
                            selection1 = "START"
                            ss2 = False
                            selection2 = "quit"
                    if event.key == pygame.K_DOWN:
                        if start == True:
                            ss1 = False
                            selection1 = "start"
                            ss2 = True
                            selection2 = "QUIT"
                    if event.key == pygame.K_RIGHT:
                        if px <= 2:
                            px += 1
                    if event.key == pygame.K_LEFT:
                        if px >= 1:
                            px -= 1
                    if event.key == pygame.K_s:
                        if start == False and trophy == False:
                            store = True
                    if event.key == pygame.K_t:
                        if start == False and store == False:
                            trophy = True
                if event.type == pygame.KEYUP:
                    motion = True
                if pygame.mouse.get_pressed()[0] and press == False and start == False and store == False:
                    press = True

                else:
                    height = 150
                
                if event.type == pygame.MOUSEMOTION:
                    motion = True

                if motion == False and press:
                    points += 1
                    height = 125
                    press = False

    print(px)
    print(bw)
    print(bh)

    if px == 1:
        bw = 225
        bh = 225
        bx = 35
        by = 35
        aw = 90
        ah = 90
        ax = 300
        ay = 95

    elif px == 2:
        aw = 120
        ah = 120
        ax = 290
        ay = 85
        bw = 200
        bh = 200
        bx = 50
        by = 50
    else:
        bw = 200
        bh = 200
        bx = 50
        by = 50
        aw = 90
        ah = 90
        ax = 300
        ay = 95

    if store == True and trophy == False:
        win.blit(breeders, (bx,by))
        win.blit(aicons, (ax,ay))
        print_bpoints()
        print_apoints()

    if breeder_points == 0:
        breeder_cost = 10

    if timer >= 10:
        pos += 1
        timer = 0

    if timer2 >= 30:
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

    if start:
        print_start()
        print_quit()

    if points >= 100:
        moon = True

    if start == False and store == False and trophy == False:
        print_points()

    if trophy == True and store == False:
        if moon:
            win.blit(moontro, (150,200))

    pygame.display.update()