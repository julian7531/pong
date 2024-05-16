#pong by julian7531

import pygame
pygame.init()

window_width , window_height = 750,500
win = pygame.display.set_mode((window_width , window_height))

class Ball:
    def __init__(self, speed , player_1_score , player_2_score):
        self.balld = pygame.draw.circle(win, (255, 255, 255),  [100,100], radius=10)
        self.speed = speed
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score
     
    def drawball(self):
        pygame.draw.circle(win, (255, 255, 255), center=self.balld.center, radius=10)

    def move(self):
        self.balld.move_ip(self.speed)
        if self.balld.left <= 0 or self.balld.right >= window_width:
            self.speed[0] = -self.speed[0]
        if self.balld.top <= 0 or self.balld.bottom >= window_height:
            self.speed[1] = -self.speed[1]
    
    def ball_hit_boundary(self , player_1_score, player_2_score):
        if ball.balld.left == 0:
            ball.balld.center = window_height // 2 , window_width // 2
            pygame.time.delay(200)
            self.player_2_score += 1
            self.player_2_score
        if ball.balld.right == window_width:
            ball.balld.center = window_width // 2 , window_height // 2
            pygame.time.delay(200)
            self.player_1_score += 1  
            self.player_1_score

    def ball_hit_slider(self):
        if ball.balld.left - (slider_1.x + slider_1.width) == 0 and (slider_1.y-20) < ball.balld.center[1] < (slider_1.y+slider_1.height+20) :
            ball.speed[0] = -ball.speed[0]

        if ball.balld.right - (slider_2.x) == 0 and (slider_2.y-20) < ball.balld.center[1] < (slider_2.y+slider_2.height+20) :
            ball.speed[0] = -ball.speed[0]
    
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
        pygame.draw.rect(win, (0,255,255) , (slider_1.x, slider_1.y, slider_1.width, slider_1.height) )
        
    def draw_slider_2(self):
        pygame.draw.rect(win, (255,0,0) , (slider_2.x, slider_2.y, slider_2.width, slider_2.height) )

slider_1 = Slider(25, 50, 5, 100, 1.4)
slider_2 = Slider(710, 50, 5, 100, 1.4)

speed = [1,1]

ball = Ball(speed , 0 ,0 )

run = True
while run:
    pygame.time.delay(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    win.fill((0,0,0))

    slider_1.move_slider_1(keys)
    slider_1.draw_slider_1()
    slider_2.move_slider_2(keys)
    slider_2.draw_slider_2()
    
    ball.move()
    ball.drawball()  

    ball.ball_hit_boundary(ball.player_1_score, ball.player_2_score)
    ball.ball_hit_slider()

    pygame.display.set_caption(f"Score: {ball.player_1_score} - {ball.player_2_score}")

    pygame.display.flip()

pygame.quit()

