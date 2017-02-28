import sys;
import pygame;
from peashooter import Peashooter;
from bullet import Bullet;

def check_events(screen, game_settings, squares,plants,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos();
			# print mouse_x;
			# print mouse_y;
			for square in squares:
				if square.rect.collidepoint(mouse_x, mouse_y):
					plants.add(Peashooter(screen));
def update_screen(screen, game_settings, background, zombies,squares,plants,bullets,tick):
	screen.blit(background.image, background.rect)
	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();

		for plant in plants:
			plant.draw_me();
			if tick % 60 == 0:
				bullets.add(Bullet(screen, plant))

		for bullet in bullets.sprites():
			bullet.update_me();
			bullet.draw_me();