import pygame

class Button():
	def __init__(self, setting, screen):
		""" 初始化飞船并设置其初始位置 """
		self.screen = screen
		self.ai_setting = setting
		
		#加载飞船图像并获取其外接矩形
		self.image = setting.normal_image
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
	
		#将每艘飞船放在屏幕顶部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.top = self.screen_rect.top + 5	
		
		#在飞船的属性x,y中存储小数值
		self.x = float(self.rect.centerx)
		self.y = float(self.rect.centery)
	
	def blitme(self):
		#在指定位置绘制飞船
		self.screen.blit(self.image, self.rect)
