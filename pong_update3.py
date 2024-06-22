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

	def __init__ (self, x, y, width, height, speed, auto_up, auto_left):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
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

def move_ball(ball):
	move_ball_vertical(ball)
	move_ball_horizontal(ball)

def move_ball_vertical(ball):
	if ball.up:
		ball.move_ip(0, -1)
		ball.y -= 1
		if ball.y <= 0:
			ball.up = False
	elif not ball.up:
		ball.move_ip(0, 1)
		ball.y += 1
		if ball.y >= (height - ball_width):
			ball.up = True

def move_ball_horizontal(ball):
	if ball.left:
		ball.move_ip(-1, 0)
		ball.x -= ball.speed
	elif not ball.left:
		ball.move_ip(1, 0)
		ball.x += ball.speed

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
ball = Ball(x, y, ball_width, ball_width, 0.2, False, True)
score = Scoreboard(0, 0)

# Game Loop Variable
run = True

# Game Loop
while run:

	pygame.time.delay(10)

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
	move_ball(ball)
	collision()

	# Ball Out-of-Bounds Check
	if (ball.x <= 0):
		reset_screen()
		score.computerPoint()
	elif (ball.x >= (width - ball_width)):
		reset_screen()
		score.playerPoint()

	# Game Completion Message
	if (score.playerPoint() == 7):
		victory_text = victory_font-render("Player 1 Wins!", False, white)
		screen.blit(victory_text, (367, 200))
		pygame.time.delay(5000)
		run = False
	elif (score.computerPoint() == 7):
		victory_text = victory_font-render("Player 2 Wins!", False, white)
		screen.blit(victory_text, (367, 200))
		pygame.time.delay(5000)
		run = False
		
	# Exit Game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()
