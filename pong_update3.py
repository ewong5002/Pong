import pygame

pygame.init()

# Game Title
pygame.display.set_caption("Pong")

# Screen Variables
height = 600
width = 800

screen = pygame.display.set_mode((width, height))

# Colour Variables
white = (255, 255, 255)
black = (0, 0, 0)

# Font Variables
game_font = pygame.font.Font("freesansbold.ttf", 32)
victory_font = pygame.font.Font("freesansbold.ttf", 50)

# Game Objects
class Paddle(pygame.Rect):

	start_y = height/2

	def __init__(self, x, y, width, height, auto):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.auto = auto

	def reset(self):
		self.y = self.start_y

class Ball(pygame.Rect):

	start_x = width/2
	start_y = height/2
	start_speed = 0.2

	def __init__ (self, x, y, width, speed, auto_up, auto_left):
		self.x = x
		self.y = y
		self.width = self.height = width
		self.speed = speed
		self.up = auto_up
		self.left = auto_left

	def reset(self):
		self.x = self.start_x
		self.y = self.start_y
		self.speed = self.start_speed

class Scoreboard:

	def __init__(self, player_score, computer_score):
		self.player_score = player_score
		self.computer_score = computer_score

	def playerPoint(self):
		self.player_score += 1

	def computerPoint(self):
		self.computer_score += 1

	def __str__(self):
		return f"{self.player_score} : {self.computer_score}"
	
# Game Functions
def movement(player):
	if key[pygame.K_w] == True and player.y > 0:
		player.move_ip(0, -1)
		player.y -= 1
	elif key[pygame.K_s] == True and player.y < (height - paddle_height):
		player.move_ip(0, 1)
		player.y += 1

def computer_movement(player):
	if player.auto:
		player.move_ip(0, -1)
		player.y -= 1
		if player.y == 0:
			player.auto = False
	elif not player.auto:
		player.move_ip(0, 1)
		player.y += 1
		if player.y == (height - paddle_height):
			player.auto = True

def move_ball():
	move_ball_vertical()
	move_ball_horizontal()

def move_ball_vertical():
	if ball.up:
		ball.move_ip(0, -1)
		ball.y -= 1
		if ball.y <= 0:
			ball.up = False
	elif not ball.up:
		ball.move_ip(0, 1)
		ball.y += 1
		if ball.y >= (height - ball.width):
			ball.up = True

def move_ball_horizontal():
	if ball.left:
		ball.move_ip(-1, 0)
	elif not ball.left:
		ball.move_ip(1, 0)

def collision():
	if ball.colliderect(player1):
		if key[pygame.K_s] == True:
			ball.up = True
		elif key[pygame.K_w] == True:
			ball.up = False
		ball.left = False

	if ball.colliderect(player2):
		if player2.auto:
			ball.up = True
		elif not player2.auto:
			ball.up = False
		ball.left = True

def reset_screen():
	pygame.time.delay(500)
	player1.reset()
	player2.reset()
	ball.reset()

# Paddle Variables
paddle_width = 10
paddle_height = 60
y = height/2

# Ball Variables
x = width/2
ball_width = 10

# Creating Objects
player1 = Paddle(50, y, paddle_width, paddle_height, True)
player2 = Paddle(750, y, paddle_width, paddle_height, True)
ball = Ball(x, y, ball_width, 0.2, True, True)
score = Scoreboard(0, 0)

# Game Loop Variable
run = True

# Game Loop
while run:

	pygame.time.delay(7)
	pygame.display.update()

	# Visuals
	screen.fill(black)
	pygame.draw.rect(screen, white, player1)
	pygame.draw.rect(screen, white, player2)
	pygame.draw.rect(screen, white, ball)

	score_text = game_font.render(f"{score}", False, white)
	screen.blit(score_text, (367, 50))

	key = pygame.key.get_pressed()

	# Game Logic
	movement(player1)
	computer_movement(player2)
	move_ball()
	#collision() 

	if ball.colliderect(player1):
		if key[pygame.K_s] == True:
			ball.up = False
			ball.left = False
		elif key[pygame.K_w] == True:
			ball.up = True
			ball.left = False
		else:
			ball.left = False

	# Ball Out-of-Bounds Check
	if (ball.x <= 0):
		reset_screen()
		score.computerPoint()
	elif (ball.x >= (width - ball.width)):
		reset_screen()
		score.playerPoint()

	# Game Completion Message
	if (int(f"{score}"[0]) == 7):
		victory_text = victory_font.render("Player 1 Wins!", False, white)
		screen.blit(victory_text, (225, 210))
		pygame.display.update()
		pygame.time.delay(3000)
		run = False
	elif (int(f"{score}"[4]) == 7):
		victory_text = victory_font.render("Player 2 Wins!", False, white)
		screen.blit(victory_text, (225, 210))
		pygame.display.update()
		pygame.time.delay(3000)
		run = False
		
	# Exit Game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
