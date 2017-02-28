import pygame;
from settings import Settings;
import game_functions as gf;
from background import Background;
from pygame.sprite import Group, groupcollide;
from zombie import Zombie;
from square import Square;
from bullet import Bullet;




pygame.init();
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("DC PVZ clone");
background = Background(game_settings);

# all of our groups
zombies = Group();
plants = Group();
squares = Group();
bullets = Group();



# load up the squares 
for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen, game_settings,i,j));

def run_game():
	tick = 0;
	while 1:
		gf.check_events(screen,game_settings,squares,plants,bullets);
		gf.update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick)
		tick += 1;
		if tick  % 60 == 0:
			zombies.add(Zombie(screen,game_settings.zombie_speed, game_settings.zombie_health));
		
		pygame.display.flip();


run_game();