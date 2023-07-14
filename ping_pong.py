from random import randint
from pygame import *
init()

class SpriteGame():
    def __init__(self, x, y, width, height, speed, image_name):
        self.rect = rect.Rect(x, y, width, height)
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.sprite = transform.scale(image.load(image_name), (width, height))

class Playerl(SpriteGame):
    def update(self):
        w.blit(self.sprite, (self.rect.x, self.rect.y))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed

class Playerr(SpriteGame):
    def update(self):
        w.blit(self.sprite, (self.rect.x, self.rect.y))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 550:
            self.rect.y += self.speed

class Ball():
    def __init__(self, x, y, width, height, image_name):
        self.rect = rect.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.sprite = transform.scale(image.load(image_name), (width, height))
    def update(self):
        global addxball
        global addyball
        global player1win
        global close
        w.blit(self.sprite, (self.rect.x, self.rect.y))
        if self.rect.colliderect(player1.rect):
            addxball = -(randint(5, 10))
        if self.rect.colliderect(player2.rect):
            addxball = randint(5, 10)
        if self.rect.y <= 0:
            addyball = randint(5, 10)
        if self.rect.y >= 700:
            addyball = -(randint(5, 10))
        self.rect.x += addxball
        self.rect.y += addyball
        if self.rect.x <= 0:
            player1win = False
            close = True
        if self.rect.x >= 1450:
            player1win = True
            close = True

closeall = False
while closeall != True:
    w = display.set_mode((1500, 750))
    display.set_caption('ping pong')
    font1 = font.SysFont('Arial', 70)
    win1 = font1.render('player 1 wins (1-try again)', True, (255, 0, 0))
    win2 = font1.render('player 2 wins (1-try again)', True, (255, 0, 0))
    clock = time.Clock()
    player1 = Playerl(1350, 200, 50, 200, 5, 'Image20230711154148.png')
    player2 = Playerr(100, 200, 50, 200, 5, 'Image20230711154148.png')
    ball = Ball(500, 300, 50, 50, 'Image20230711154203.png')
    close = False
    player1win = False
    addxball = randint(5, 10)
    addyball = randint(5, 10)
    while close != True:
        w.fill((255, 255, 255))
        player1.update()
        player2.update()
        ball.update()
        for i in event.get():
            if i.type == QUIT:
                close = True
                closeall = True
        display.update()
        clock.tick(60)
    close = False
    while close == False:
        w.fill((255, 255, 255))
        if player1win:
            w.blit(win1, (200, 200))
        else:
            w.blit(win2, (200, 200))           
        for i in event.get():
            if i.type == KEYDOWN:
                if i.key == K_1:
                    close = True
            if i.type == QUIT:
                close = True
                closeall = True
        if closeall:
            close = True
        display.update()
        clock.tick(60)
