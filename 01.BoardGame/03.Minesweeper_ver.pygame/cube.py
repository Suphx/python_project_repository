import pygame
from pygame.sprite import Sprite

class Cube(Sprite):
	""" 描述所有未点开的方块 """
	def __init__(self, setting, screen):
		""" 初始化cube并设置起其实位置 """
		super().__init__()
		self.screen = screen 
		self.setting = setting
		
		#加载cube的图像,并设置其rect属性
		self.oldimage = pygame.image.load(setting.cube)
		self.image = pygame.transform.scale(self.oldimage, (30,30))
		self.rect = self.image.get_rect()
		
		#每个cube最初都在屏幕左上角附件
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		#设置默认的flag_status
		self.flag_status = 0
		self.clicked = False
		
	def blitme(self):
		"""在指定位置绘制cube """
		self.screen.blit(self.image, self.rect)