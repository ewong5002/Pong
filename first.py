import pygame

pygame.init()

height = 600

screen = pygame.display.set_mode((800, height))

pygame.display.set_caption("Pong")

run = True

paddle_height = 60
y = height/2

player1 = pygame.Rect((50, y, 10, paddle_height))
player2 = pygame.Rect((450, y, 10, paddle_height))

while run:

	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, (255, 255, 255), player1)

	pygame.draw.rect(screen, (255, 255, 255), player2)

	key = pygame.key.get_pressed()

	if key[pygame.K_w] == True and player1.y > 0:
		player1.move_ip(0, -1)
		y -= 1
	elif key[pygame.K_s] == True and player1.y < (height - paddle_height):
		player1.move_ip(0, 1)
		y += 1
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()