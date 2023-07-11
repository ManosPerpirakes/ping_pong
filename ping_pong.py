from pygame import *
init()

class SpriteGame(sprite.Sprite):
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

w = display.set_mode((1500, 750))
clock = time.Clock()
player1 = Playerl(1350, 200, 50, 200, 5, 'Image20230711154148.png')
player2 = Playerr(100, 200, 50, 200, 5, 'Image20230711154148.png')
close = False
while close != True:
    w.fill((255, 255, 255))
    player1.update()
    player2.update()
    for i in event.get():
        if i.type == QUIT:
            close = True
    display.update()
    clock.tick(60)
