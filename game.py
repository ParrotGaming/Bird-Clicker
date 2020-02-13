import json
import pygame
pygame.init()
pygame.font.init()

pygame.display.set_caption("Bird Clicker")

win = pygame.display.set_mode((500, 500))

bw = 120
bh = 40
bx = 80
by = 120

aw = 60
ah = 60
ax = 320
ay = 105

f1 = pygame.image.load('./assets/f1.png')
f2 = pygame.image.load('./assets/f2.png')
lck = pygame.image.load('./assets/locked.png')
lcks = pygame.transform.scale(lck, (100,100))
moontro = pygame.image.load('./assets/moon_trophy.png')
moontros = pygame.transform.scale(moontro, (100,100))
marstro = pygame.image.load('./assets/mars.png')
marstros = pygame.transform.scale(marstro, (100,100))

px = 1

breeder_cost = 10
increment = 1

start = True

trophy = False

store = False

selection1 = "start"
selection2 = "quit"
ss1 = False
ss2 = False

height = 150

background = f1

txtbr = (0, 183, 255)

white = (255, 255, 255)

button_main = pygame.Rect(125,height,100,100)
button_main_asset = pygame.image.load('./assets/Icon.png')
button_main_assetScaled = pygame.transform.scale(button_main_asset, (250,250))

button_store = pygame.Rect(10,10,35,40)
button_store_asset = pygame.image.load('./assets/shop.png')
button_store_assetScaled = pygame.transform.scale(button_store_asset, (35,40))
button_exit = pygame.Rect(10,10,30,30)
button_exit_asset = pygame.image.load('./assets/exit.png')
button_exit_assetScaled = pygame.transform.scale(button_exit_asset, (30,30))

button_breeder = pygame.Rect(bx,by,bw,bh)
button_breeder_asset = pygame.image.load('./assets/breeder.png')
button_breeder_assetScaled = pygame.transform.scale(button_breeder_asset, (bw,bh))

button_breederC = pygame.Rect(80,120,bw,bh)

button_aviary = pygame.Rect(ax,ay,aw,ah)
button_aviary_asset = pygame.image.load('./assets/AVI2.png')
button_aviary_assetScaled = pygame.transform.scale(button_aviary_asset, (aw,ah))

button_aviaryC = pygame.Rect(320,105,bw,bh)

class State:
    def __init__(self):
        self.points = 0
        self.breeder_points = 0
        self.avery_points = 0
        self.moon = False
        self.mars = False

    def decode(self):
        f = open("./saves/save.json","r")
        d = json.load(f)
        self.points = d.get("points",0)
        self.breeder_points = d.get("breeder_points",0)
        self.avery_points = d.get("avery_points",0)
        self.moon = d.get("moon",0)
        self.mars = d.get("mars",0)

    def encode(self):
        f = open("./saves/save.json","w")
        d = {
            "points": self.points,
            "breeder_points": self.breeder_points,
            "avery_points": self.avery_points,
            "moon": self.moon,
            "mars": self.mars
        }
        json.dump(d,f)

state = State()

try:
    state.decode()
except:
    pass

display_points = 0
display_pointsV = ""

def display_number(n):
    t = 1000
    m = 1000000
    b = 1000000000
    tr = 1000000000000
    l = ""
    if n >= tr:
        n = float(n) / tr
        l = "TR"
    elif n >= b:
        n = float(n) / b
        l = "B"
    elif n >= m:
        n = float(n) / m
        l = "M"
    elif n >= t:
        n = float(n) / t
        l = "K"
    s = str(n)
    i = s.find(".")
    if i > -1:
        s = s[:i+2]
    return s + l

def print_points():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw = font.render(f"{int(display_points)}{display_pointsV}", True, white, txtbr)
    WintextRect = WinDraw.get_rect()
    WintextRect.center = (100, 250)
    win.blit(WinDraw, WintextRect)

def print_pointsF():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw = font.render(f"{display_number(state.points)}", True, white, txtbr)
    WintextRect = WinDraw.get_rect()
    WintextRect.center = (100, 250)
    win.blit(WinDraw, WintextRect)

def print_bpoints():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw2 = font.render(f"{state.breeder_points}", True, white, txtbr)
    WintextRect2 = WinDraw2.get_rect()
    WintextRect2.center = (225, 145)
    win.blit(WinDraw2, WintextRect2)

def print_bcost():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw2 = font.render(f"{display_number(breeder_cost)}", True, white, txtbr)
    WintextRect2 = WinDraw2.get_rect()
    WintextRect2.center = (145, 190)
    win.blit(WinDraw2, WintextRect2)

def print_apoints():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"{state.avery_points}", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (400, 145)
    win.blit(WinDraw3, WintextRect3)

def print_acost():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw2 = font.render(f"{display_number(avery_cost)}", True, white, txtbr)
    WintextRect2 = WinDraw2.get_rect()
    WintextRect2.center = (350, 190)
    win.blit(WinDraw2, WintextRect2)

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

def print_moon():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"Moon", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (140, 170)
    win.blit(WinDraw3, WintextRect3)

def print_moon_points():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"100 pts", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (140, 330)
    win.blit(WinDraw3, WintextRect3)

def print_mars():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"Mars", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (370, 170)
    win.blit(WinDraw3, WintextRect3)

def print_mars_points():
    font = pygame.font.Font('./assets/LCD_Solid.ttf', 32)
    WinDraw3 = font.render(f"1000 pts", True, white, txtbr)
    WintextRect3 = WinDraw3.get_rect()
    WintextRect3.center = (365, 330)
    win.blit(WinDraw3, WintextRect3)

pos = 0

timer = 0

timer2 = 0

timer3 = 0

t1 = moontros

t2 = lcks

while True:
    pygame.time.delay(30)

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    win.blit(background,(0,0))

    if start == False and store == False and trophy == False:
        win.blit(button_main_assetScaled,(button_main.x,height))

    press = False

    motion = False

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state.encode()
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    motion = True
                    if event.key == pygame.K_RETURN:
                        if start:
                            if ss1:
                                start = False
                            if ss2:
                                state.encode()
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
                    if event.key == pygame.K_s:
                        if start == False and trophy == False:
                            store = True
                    if event.key == pygame.K_t:
                        if start == False and store == False:
                            trophy = True
                if event.type == pygame.KEYUP:
                    motion = True
                if pygame.mouse.get_pressed()[0]:
                    press = True

                else:
                    height = 150
                
                if event.type == pygame.MOUSEMOTION:
                    motion = True

                if motion == False and press:
                    if button_store.collidepoint(mouseX,mouseY) and store == False:
                        store = True
                    elif button_exit.collidepoint(mouseX,mouseY) and store:
                        store = False
                    elif button_breederC.collidepoint(mouseX,mouseY) and store:
                        if state.points >= breeder_cost:
                            state.breeder_points += 1
                            state.points -= breeder_cost
                            print(breeder_cost)
                    elif button_aviaryC.collidepoint(mouseX,mouseY) and store:
                        if state.points >= avery_cost:
                            if state.points >= avery_cost:
                                state.avery_points += 1
                                state.points -= avery_cost
                    elif store == False and trophy == False and start == False:
                        state.points += 1
                        height = 125
                    press = False
    
    if button_breederC.collidepoint(mouseX,mouseY) and store:
        px = 1
    elif button_aviaryC.collidepoint(mouseX,mouseY) and store:
        px = 2
    else:
        px = 0


    if px == 1:
        button_breeder.x = 80
        button_breeder.y = 110
        aw = 90
        ah = 90
        button_aviary.x = 320
        button_aviary.y = 105

    elif px == 2:
        aw = 90
        ah = 90
        button_aviary.x = 320
        button_aviary.y = 95
        bw = 200
        bh = 200
        button_breeder.x = 80
        button_breeder.y = 120
    else:
        bw = 200
        bh = 200
        button_breeder.x = 80
        button_breeder.y = 120
        aw = 90
        ah = 90
        button_aviary.x = 320
        button_aviary.y = 105

    if store == True and trophy == False:
        # win.blit(breeders, (bx,by))
        win.blit(button_breeder_assetScaled,(button_breeder.x,button_breeder.y))
        win.blit(button_aviary_assetScaled, (button_aviary.x,button_aviary.y))
        print_bpoints()
        print_apoints()
        print_acost()
        print_bcost()
        win.blit(button_exit_assetScaled,(button_exit.x,button_exit.y))

    if state.breeder_points == 0:
        breeder_cost = 10

    if timer >= 10:
        pos += 1
        timer = 0

    if timer2 >= 30:
        state.points += 1 * state.breeder_points
        state.points += 10 * state.avery_points
        timer2 = 0

    if state.breeder_points > 0:
        increment = state.breeder_points * 1.5

    breeder_cost = 10 * round(increment)


    avery_cost = int(100 * (state.avery_points + 1) * 1.5)

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

    if state.points >= 100:
        state.moon = True

    if state.points >= 1000:
        state.mars = True
    
    if state.moon:
        t1 = moontros
    if state.moon == False:
        t1 = lcks
    if state.mars:
        t2 = marstros
    if state.mars == False:
        t2 = lcks

    if start == False and store == False and trophy == False:
        if state.points < 1000:
            print_points()
        if state.points >= 1000:
            print_pointsF()
        win.blit(button_store_assetScaled,(button_store.x,button_store.y))

    if trophy == True and store == False:
        win.blit(t1, (90,200))
        win.blit(t2, (320,200))
        print_moon()
        print_moon_points()
        print_mars()
        print_mars_points()

    if state.points < 1000:
        display_points = state.points
        display_pointsV = ""

    pygame.display.update()