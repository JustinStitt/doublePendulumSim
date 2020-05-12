import pygame
import sys
import math
pygame.init()

size = (750,750)
background_color = (240,240,213)
black = (0,0,0)
window = pygame.display.set_mode(size)

center = (size[0]/2,50 )
clock = pygame.time.Clock()

#vars
r1 = 100.#length of rope 1
r2 = 375.
m1 = 50.
m2 = 10.
a1 = 45.
a2 = 0.
a1_v = 0.
a2_v = 0.
#a1_a = 0.
#a2_a = 0.
ball_size = 60
g = 5#gravity constant
#end vars


def update():
    global a1,a2,a1_v,a2_v,g
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -2 * g * math.sin(a1-2*a2)
    num3 = -2*math.sin(a1-a2) * m2
    num4 = a2_v*a2_v*r2+a1_v*a1_v*r1*math.cos(a1-a2)
    den = r1 * (2*m1+m2-m2*math.cos(2*a1-2*a2))

    a1_a = (num1 + num2 +num3*num4) / den

    num1 = 2 * math.sin(a1-a2)
    num2 = (a1_v*a1_v*r1*(m1+m2))
    num3 = g * (m1 + m2) * math.cos(a1)
    num4 = a2_v*a2_v*r2*m2*math.cos(a1-a2)
    den = r2 * (2*m1+m2-m2*math.cos(2*a1-2*a2))

    a2_a = (num1*(num2+num3+num4)) / den




    x1 = (r1 * math.sin(a1)) + center[0]
    y1 = (r1 * math.cos(a1)) + center[1]
    x2 = x1 + (r2 * math.sin(a2))
    y2 = y1 + (r2 * math.cos(a2))

    pygame.draw.line(window, black, center, (x1,y1), 4 )
    pygame.draw.ellipse(window, black, pygame.Rect(x1 - ball_size / 2,y1 - ball_size / 2,ball_size,ball_size)  )
    pygame.draw.line(window, black, (x1,y1), (x2,y2), 4 )
    pygame.draw.ellipse(window, black, pygame.Rect(x2 - ball_size / 2,y2 - ball_size / 2,ball_size,ball_size)  )

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 +=a2_v



    a2_a = 0

def render():
    pass

while True:
    window.fill(background_color)
    update()
    render()
    pygame.display.flip()
    clock.tick(30)
