import pygame;

class Settings():
	def __init__(self):
		display_info = pygame.display.Info();
		self.screen_size = (display_info.current_w, display_info.current_h)
		self.bg_color = (255,255,255);
		self.zombie_speed = 5;
		self.zombie_health = 5;
		self.game_active = True;
		# square stuff 
		self.squares = {
			"start_left": 367,
			"start_top": 246,
			"square_width": 115,
			"square_height": 104,
			"rows": [
				245,
				350,
				455,
				560,
				665
			]
		};
		self.highlighted_square = 0;
		self.zombie_in_row = [
			0,
			0,
			0,
			0,
			0
		]