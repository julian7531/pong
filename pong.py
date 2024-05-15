#pong by julian

import pygame
pygame.init()

window_width , window_height = 750,500
win = pygame.display.set_mode((window_width , window_height))

class Ball:
    def __init__(self, speed):
        self.balld = pygame.draw.circle(win, (255, 255, 255),  [100,100], radius=10)
        self.speed = speed

    def drawball(self):
        pygame.draw.circle(win, (255, 255, 255), center=self.balld.center, radius=10)

    def move(self):
        self.balld.move_ip(self.speed)
        if self.balld.left <= 0 or self.balld.right >= window_width:
            self.speed[0] = -self.speed[0]
        if self.balld.top <= 0 or self.balld.bottom >= window_height:
            self.speed[1] = -self.speed[1]
     
class Slider:
    def __init__(self, x ,y ,width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def move_slider_1(self , keys):
        if keys[pygame.K_w] and self.y > 0:
            self.y -= (self.vel)

        if keys[pygame.K_s] and self.y < (500-self.height):
            self.y += self.vel

    def move_slider_2(self , keys):
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= (self.vel)

        if keys[pygame.K_DOWN] and self.y < (500-self.height):
            self.y += self.vel

    def draw_slider_1(self):
        pygame.draw.rect(win, (0,255,255) , (s1.x, s1.y, s1.width, s1.height) )
        
    def draw_slider_2(self):
        pygame.draw.rect(win, (255,0,0) , (s2.x, s2.y, s2.width, s2.height) )

s1 = Slider(25, 50, 5, 100, 2)
s2 = Slider(710, 50, 5, 100, 2)

speed = [1,1]

ball = Ball(speed)

player_1_score = 0 
player_2_score = 0

run = True
game_close = False
while run:
    pygame.time.delay(2)

    pygame.display.set_caption(f"Score: {player_1_score} - {player_2_score}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    win.fill((0,0,0))

    s1.move_slider_1(keys)
    s1.draw_slider_1()
    
    s2.move_slider_2(keys)
    s2.draw_slider_2()
    
    ball.move()
    ball.drawball()  

    if ball.balld.left - (s1.x + s1.width) == 0 and (s1.y-20) < ball.balld.center[1] < (s1.y+s1.height+20) :
        ball.speed[0] = -ball.speed[0]

    if ball.balld.right - (s2.x) == 0 and (s2.y-20) < ball.balld.center[1] < (s2.y+s2.height+20) :
        ball.speed[0] = -ball.speed[0]

    if ball.balld.left == 0:
        player_2_score += 1
        ball.balld.center = window_height / 2 , window_width / 2

    if ball.balld.right == window_width:
        player_1_score += 1
        ball.balld.center = window_width // 2 , window_height // 2

    pygame.display.flip()

pygame.quit()

