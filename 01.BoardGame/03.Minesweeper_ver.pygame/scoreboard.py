import pygame.font


class Scoreboard():
	""" 显示得分信息的类 """
	
	def __init__(self, setting, screen, stats):
		""" 初始化显示得分涉及的属性 """
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.setting = setting
		self.stats = stats
	
		#显示得分的字体设置
		self.width, self.height = 80, 48
		self.text_color = (204, 51, 0)
		self.bg_color = (0, 0, 0)
		self.font = pygame.font.Font(setting.font, 40)
		
		#创建rect对象
		self.rect_l = pygame.Rect(0, 0, self.width, self.height)
		self.rect_l.x = self.screen_rect.left + 5
		self.rect_l.y = 10
		self.rect_r = pygame.Rect(0, 0, self.width, self.height)
		self.rect_r.x = self.screen_rect.right - 85
		self.rect_r.y = 10
	
		#准备初始图像
		self.prep_time()
		self.prep_left_bombs()
	
	def prep_time(self):
		""" 将耗时转换为一副图像 """
		time_str = str(self.stats.elapsed_time)
		self.time_image = self.font.render(time_str, True, self.text_color, self.bg_color)
		
		#将耗时放在屏幕左上角
		self.time_rect = self.time_image.get_rect()
		self.time_rect.left = self.screen_rect.left + 15
		self.time_rect.top = 10
		
	def prep_left_bombs(self):
		""" 将剩余雷数转换为一副图像 """
		left_bombs_str = str(self.stats.bomb_numbers)
		self.left_bombs_image = self.font.render(left_bombs_str, True, self.text_color, self.bg_color)
		
		#将耗时放在屏幕右上角
		self.left_bombs_rect = self.left_bombs_image.get_rect()
		self.left_bombs_rect.right = self.screen_rect.right - 10
		self.left_bombs_rect.top = 10
	
	def show_all(self):
		""" 在屏幕上显示 """
		self.screen.fill(self.bg_color, self.rect_l)
		self.screen.blit(self.time_image, self.time_rect)
		self.screen.fill(self.bg_color, self.rect_r)
		self.screen.blit(self.left_bombs_image, self.left_bombs_rect)