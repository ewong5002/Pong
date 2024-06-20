import pygame

pygame.init()

height = 600
width = 800

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong")

run = True

paddle_height = 60
y = height/2
y2 = height/2

x = width/2
y3 = height/2

player1 = pygame.Rect((50, y, 10, paddle_height))
player2 = pygame.Rect((750, y2, 10, paddle_height))
ball = pygame.Rect(x, y3, 10, 10)

godown = False
ballgoright = False
ballgoup = True

while run:

	pygame.time.delay(5)

	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, (255, 255, 255), player1)

	pygame.draw.rect(screen, (255, 255, 255), player2)

	pygame.draw.rect(screen, (255, 255, 255), ball)

	key = pygame.key.get_pressed()

	if key[pygame.K_w] == True and player1.y > 0:
		player1.move_ip(0, -1)
		y -= 1
	elif key[pygame.K_s] == True and player1.y < (height - paddle_height):
		player1.move_ip(0, 1)
		y += 1
    
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
		x -= 1
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
	
	if ball.colliderect(player2):
		if godown == True:
			ballgoup = False
			ballgoright = False
		elif godown == False:
			ballgoup = True
			ballgoright = False

	if ball.x <= 0:
		x = width/2
		y3 = height/2
		print("hi")
	elif ball.x >= 800:
		x = width/2
		y3 = height/2
		print("hi")
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:

			run = False
	
	pygame.display.update()

pygame.quit()
