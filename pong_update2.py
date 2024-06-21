import pygame, random

pygame.init()

pygame.display.set_caption("Pong") #Title of game

height = 600
width = 800

screen = pygame.display.set_mode((width, height))

run = True

class Paddle(pygame.Rect): #Creates paddle object

	start_y = height/2

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.reset()

	def reset(self):
		self.y = self.start_y

class Ball(pygame.Rect): #Creates ball object

	start_x = width/2
	start_y = height/2

	def __init__ (self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.reset()

	def reset(self):
		self.x = self.start_x
		self.y = self.start_y

white = (255, 255, 255) #Initializing RGB values for colours
black = (0, 0, 0)

paddle_width = 10 #Initializing paddle attributes
paddle_height = 60
y = y2 = ball_y = height/2

x = width/2 #Initializing ball attributes
ball_width = 10

player1 = Paddle(50, y, paddle_width, paddle_height)
player2 = Paddle(750, y2, paddle_width, paddle_height)
ball = Ball(x, ball_y, ball_width, ball_width)

go_down = False
ball_go_right = False
ball_go_up = True

while run:

	pygame.time.delay(5)

	screen.fill(black)

	pygame.draw.rect(screen, white, player1)

	pygame.draw.rect(screen, white, player2)

	pygame.draw.rect(screen, white, ball)

	key = pygame.key.get_pressed()

	if key[pygame.K_w] == True and player1.y > 0: #Controls for human player
		player1.move_ip(0, -1)
		y -= 1
	elif key[pygame.K_s] == True and player1.y < (height - paddle_height):
		player1.move_ip(0, 1)
		y += 1
    
	if not go_down: #Movement for computer player
		player2.move_ip(0, -1)
		y2 -= 1
		if player2.y == 0:
			go_down = True

	if go_down:
		player2.move_ip(0, 1)
		y2 += 1
		if player2.y == (height - paddle_height):
			go_down = False

	if not ball_go_right: #Movement for ball
		ball.move_ip(-1, 0)
		x -= 1
	elif ball_go_right:
		ball.move_ip(1, 0)
	
	if not ball_go_up:
		ball.move_ip(0, 1)
		ball_y += 1
		if ball.y == (height - 10):
			ball_go_up = True
	elif ball_go_up:
		ball.move_ip(0, -1)
		ball_y -= 1
		if ball.y == 0:
			ball_go_up = False

	if ball.colliderect(player1): #Collision physics
		if key[pygame.K_s] == True:
			ball_go_up = False
			ball_go_right = True
		elif key[pygame.K_w] == True:
			ball_go_up = True
			ball_go_right = True
	
	if ball.colliderect(player2):
		if go_down == True:
			ball_go_up = False
			ball_go_right = False
		elif go_down == False:
			ball_go_up = True
			ball_go_right = False

	if (ball.x <= 0 or ball.x >= (width - ball_width)): #Checks if the ball hits either end of the screen
		pygame.time.delay(500)
		player1.reset()
		player2.reset()
		ball.reset()
		
	for event in pygame.event.get(): #Allows player to exit the game
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()
