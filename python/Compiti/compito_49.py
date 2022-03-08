import sys, pygame

pygame.init()

width, height = 640, 480
size=(width, height)
speed = [1, 1]
black = (0, 0, 0)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__["unicode"] == "w":
                if ballrect.top > 0:
                    ballrect = ballrect.move(0, -10)
            if event.__dict__["unicode"] == "a":
                if ballrect.left > 0:
                    ballrect = ballrect.move(-10, 0)
            if event.__dict__["unicode"] == "s":
                if ballrect.bottom < height:
                    ballrect = ballrect.move(0, 10)
            if event.__dict__["unicode"] == "d":
                if ballrect.right < width:
                    ballrect = ballrect.move(10, 0)
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()