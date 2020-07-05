import pygame
class Setting():
	""" 存放所有后台配置类信息 """
	
	def __init__(self):
		#屏幕设置
		self.screen_width = 273
		self.screen_height = 336
		self.screen_color = (178, 178, 178)
		
		#格子行数和列数
		self.number_lines = 9
		self.number_rows = 9
		
		#资源路径
		self.cube = 'images/cube.jpg'
		self.num_0 = 'images/0.jpg'
		self.num_1 = 'images/1.jpg'
		self.num_2 = 'images/2.jpg'
		self.num_3 = 'images/3.jpg'
		self.num_4 = 'images/4.jpg'
		self.num_5 = 'images/5.jpg'
		self.num_6 = 'images/6.jpg'
		self.num_7 = 'images/7.jpg'
		self.num_8 = 'images/8.jpg'
		self.bomb = 'images/bomb.jpg'
		self.bomb0 = 'images/bomb0.jpg'
		self.flag1 = 'images/flag.jpg'
		self.flag2 = 'images/flag2.jpg'
		self.smile = 'images/smile.png'
		self.cry = 'images/cry.png'
		self.normal = 'images/normal.png'
		
		self.font = 'a.ttf'
		
		#加载图片资源
		self.flag0_oldimage = pygame.image.load(self.cube)
		self.flag0_image = pygame.transform.scale(self.flag0_oldimage, (30,30))
	
		self.flag1_oldimage = pygame.image.load(self.flag1)
		self.flag1_image = pygame.transform.scale(self.flag1_oldimage, (30,30))
	
	
		self.flag2_oldimage = pygame.image.load(self.flag2)
		self.flag2_image = pygame.transform.scale(self.flag2_oldimage, (30,30))
		
		self.num_0_oldimage = pygame.image.load(self.num_0)
		self.num_0_image = pygame.transform.scale(self.num_0_oldimage, (30,30))
		self.num_1_oldimage = pygame.image.load(self.num_1)
		self.num_1_image = pygame.transform.scale(self.num_1_oldimage, (30,30))
		self.num_2_oldimage = pygame.image.load(self.num_2)
		self.num_2_image = pygame.transform.scale(self.num_2_oldimage, (30,30))
		self.num_3_oldimage = pygame.image.load(self.num_3)
		self.num_3_image = pygame.transform.scale(self.num_3_oldimage, (30,30))
		self.num_4_oldimage = pygame.image.load(self.num_4)
		self.num_4_image = pygame.transform.scale(self.num_4_oldimage, (30,30))
		self.num_5_oldimage = pygame.image.load(self.num_5)
		self.num_5_image = pygame.transform.scale(self.num_5_oldimage, (30,30))
		self.num_6_oldimage = pygame.image.load(self.num_6)
		self.num_6_image = pygame.transform.scale(self.num_6_oldimage, (30,30))
		self.num_7_oldimage = pygame.image.load(self.num_7)
		self.num_7_image = pygame.transform.scale(self.num_7_oldimage, (30,30))
		self.num_8_oldimage = pygame.image.load(self.num_8)
		self.num_8_image = pygame.transform.scale(self.num_8_oldimage, (30,30))
		
		self.bomb0_oldimage = pygame.image.load(self.bomb0)
		self.bomb0_image = pygame.transform.scale(self.bomb0_oldimage, (30,30))
		
		self.smile_oldimage = pygame.image.load(self.smile)
		self.smile_image = pygame.transform.scale(self.smile_oldimage, (60,60))
		self.cry_oldimage = pygame.image.load(self.cry)
		self.cry_image = pygame.transform.scale(self.cry_oldimage, (60,60))
		self.smile_oldimage = pygame.image.load(self.smile)
		self.smile_image = pygame.transform.scale(self.smile_oldimage, (60,60))
		self.normal_oldimage = pygame.image.load(self.normal)
		self.normal_image = pygame.transform.scale(self.normal_oldimage, (60,60))
		
		#鼠标按键状态
		self.left_click = False
		self.wheel_click = False
		self.right_click = False
		
		#初始状态
		self.first_step = True
		self.bomb_clicked = False
		self.bomb_numbers = 10