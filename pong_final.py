import pygame

pygame.init()

# Screen variables
height = 600
width = 800

# Fonts
game_font = pygame.font.Font("freesansbold.ttf", 32)
victory_font = pygame.font.Font("freesansbold.ttf", 50)

# Colour variables
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))

# Title
pygame.display.set_caption("Pong")

# Object variables
paddle_height = 60
y = y2 = y3 = height/2

x = width/2

# Objects
player1 = pygame.Rect((50, y, 10, paddle_height))
player2 = pygame.Rect((750, y2, 10, paddle_height))
ball = pygame.Rect(x, y3, 10, 10)

class Scoreboard:

	def __init__(self, player_score, computer_score):
		self.player_score = player_score
		self.computer_score = computer_score

	def playerPoint(self):
		self.player_score += 1

	def computerPoint(self):
		self.computer_score += 1

	def __str__(self):
		return f"{self.player_score} - {self.computer_score}"

def movement():
	if key[pygame.K_w] == True and player1.y > 0:
		player1.move_ip(0, -1)
		player1.y -= 1
	elif key[pygame.K_s] == True and player1.y < (height - paddle_height):
		player1.move_ip(0, 1)
		player1.y += 1

score = Scoreboard(0, 0)

godown = False
ballgoright = False
ballgoup = True

while True:

	pygame.time.delay(7)

	screen.fill((0, 0, 0))

	# Display objects
	pygame.draw.rect(screen, white, player1)
	pygame.draw.rect(screen, white, player2)
	pygame.draw.rect(screen, white, ball)

	# Display score
	score_text = game_font.render(f"{score}", False, (255, 255, 255))
	screen.blit(score_text, (367, 50))

	key = pygame.key.get_pressed()

	# Human paddle controls
	movement()

	# Computer paddle controls
	if godown == False:
		player2.move_ip(0, -1)
		y2 -= 1
		if player2.y == 0:
			godown = True

	if godown == True:
		player2.move_ip(0, 1)
		y2 += 1
		if player2.y == height - paddle_height:
			godown = False

	# Ball movement
	if ballgoright == False:
		ball.move_ip(-1, 0)
	elif ballgoright:
		ball.move_ip(1, 0)
	
	if ballgoup == False:
		ball.move_ip(0, 1)
		y3 += 1
		if ball.y == height - 10:
			ballgoup = True
	elif ballgoup:
		ball.move_ip(0, -1)
		y3 -= 1
		if ball.y == 0:
			ballgoup = False

	# Collision physics
	if ball.colliderect(player1):
		if key[pygame.K_s] == True:
			ballgoup = False
			ballgoright = True
		elif key[pygame.K_w] == True:
			ballgoup = True
			ballgoright = True
		else:
			ballgoright = True
	
	if ball.colliderect(player2):
		if godown == True:
			ballgoup = False
			ballgoright = False
		elif godown == False:
			ballgoup = True
			ballgoright = False
		else:
			ballgoright = False

	# Out-of-bounds check
	if ball.x <= 0:
		ball.x = width/2
		ball.y = height/2
		ballgoright = False
		ballgoup = True
		score.computerPoint()
		pygame.display.update()

	elif ball.x >= 790:
		ball.x = width/2
		ball.y = height/2
		ballgoright = False
		ballgoup = True
		score.playerPoint()

	# Game completed messages
	if (int(f"{score}"[0]) == 7):
		victory_text = victory_font.render("Player 1 Wins!", False, (255, 255, 255))
		screen.blit(victory_text, (225, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		run = False
	elif (int(f"{score}"[4]) == 7):
		victory_text = victory_font.render("Player 2 Wins!", False, (255, 255, 255))
		screen.blit(victory_text, (225, 210))
		pygame.display.update()
		pygame.time.delay(3000)
		run = False
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			
	pygame.display.update()
