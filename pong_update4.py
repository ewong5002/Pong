import pygame

pygame.init()

height = 600
width = 800

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong")

paddle_height = 60
y = height/2
y2 = height/2

x = width/2
y3 = height/2

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

game_font = pygame.font.Font("freesansbold.ttf", 32)
victory_font = pygame.font.Font("freesansbold.ttf", 50)

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

clock = pygame.time.Clock()

run = True
while run:

	pygame.time.delay(7)

	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, (255, 255, 255), player1)
	pygame.draw.rect(screen, (255, 255, 255), player2)
	pygame.draw.rect(screen, (255, 255, 255), ball)

	score_text = game_font.render(f"{score}", False, (255, 255, 255))
	screen.blit(score_text, (367, 50))

	key = pygame.key.get_pressed()
	restart = False

	movement()
    
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
			run = False
			
	pygame.display.update()

pygame.quit()
