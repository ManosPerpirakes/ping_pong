from pygame import *
init()

w = display.set_mode((1500, 750))
clock = time.Clock()
close = False
while close != True:
    w.fill((255, 255, 255))
    for i in event.get():
        if i.type == QUIT:
            close = True
    display.update()
    clock.tick(60)