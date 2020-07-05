import sys
import time
import random

import pygame
from time import sleep
from cube import Cube
from bomb import Bomb


def check_event(setting, screen, bombs, cubes, flags, nums, stats, bomb_image, reset_button):
	""" 响应键盘和鼠标事件 """
	left_click = setting.left_click
	wheel_click = setting.wheel_click
	right_click = setting.right_click
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pressed_array = pygame.mouse.get_pressed()
			for index in range(len(pressed_array)):
				if pressed_array[index]:
					if index == 0:
						#响应鼠标左键单击
						left_click = True
						mouse_x, mouse_y = pygame.mouse.get_pos()
						left_clicked(setting, screen, bombs, cubes, flags, nums, stats, bomb_image, reset_button, mouse_x, mouse_y)
					#只有游戏开始时才响应中键同时按下动作
					elif index == 1 and stats.game_active and stats.game_started:
						wheel_click =True
						pass
					#只有游戏开始时才响应右键和双键同时按下动作
					elif index == 2 and stats.game_active and stats.game_started:
						right_click = True
						if left_click:
							#响应鼠标左右键同时单击
							mouse_x, mouse_y = pygame.mouse.get_pos()
							both_clicked(setting, screen, cubes, bombs, stats, nums, flags, bomb_image, reset_button, mouse_x, mouse_y)
						else:
							#响应鼠标右键单击
							mouse_x, mouse_y = pygame.mouse.get_pos()
							right_clicked(setting, screen, cubes, bombs, flags, mouse_x, mouse_y)
		elif event.type == pygame.MOUSEBUTTONUP:
			pressed_array = pygame.mouse.get_pressed()
			for index in range(len(pressed_array)):
				if not pressed_array[index]:
					if index == 0:
						if left_click:
							#响应鼠标左键松开
							left_click = False
					elif index == 1:
						if wheel_click:
							wheel_click =False
					elif index == 2:
						if right_click:
							#响应鼠标右键松开
							right_click = False
		elif event.type == pygame.KEYDOWN:
			pass
		elif event.type == pygame.KEYUP:
			pass

def both_clicked(setting, screen, cubes, bombs, stats, nums, flags, bomb_image, reset_button, mouse_x, mouse_y):
	""" 响应鼠标左右键同时点击的情况 """
	for cube in cubes.sprites():
		botton_clicked = cube.rect.collidepoint(mouse_x, mouse_y)
		if botton_clicked:
			# 已翻开的格子点击才有效
			if cube.clicked:
				for num in range(1,9):
					if cube.image == nums[num]:
						cube_rectx = cube.rect.x
						cube_recty = cube.rect.y
						not_clicked_num = 0
						flag_num = 0
						#获取周围方格位置
						around = [[(cube_rectx + 30),cube_recty], [(cube_rectx - 30),cube_recty], [cube_rectx,(cube_recty + 30)], [cube_rectx,(cube_recty - 30)], [(cube_rectx + 30),(cube_recty - 30)], [(cube_rectx + 30),(cube_recty + 30)], [(cube_rectx - 30),(cube_recty - 30)], [(cube_rectx - 30) ,(cube_recty + 30)]]
						for x,y in around:
							for cube in cubes.sprites():
								if cube.rect.x == x and cube.rect.y == y:
									if not cube.clicked:
										not_clicked_num += 1
										if cube.image == flags[1]:
											flag_num += 1
						if num == not_clicked_num:
							for x,y in around:
								for cube in cubes.sprites():
									if cube.rect.x == x and cube.rect.y == y:
										if not cube.clicked:
											for bomb in bombs.sprites():
												if bomb.rect.x == cube.rect.x and bomb.rect.y == cube.rect.y:
													cube.flag_status = 1
													cube.image = flags[cube.flag_status]
													bomb.flag_status = True
						if num == flag_num:
							for x,y in around:
								for cube in cubes.sprites():
									if cube.rect.x == x and cube.rect.y == y:
										if cube.clicked == False and cube.flag_status == 0:
											cube.click = True
											bomb_flag = False
											#遍历bombs组，确定点击的cube是否有bomb
											for bomb in bombs.sprites():
												if bomb.rect.x == cube.rect.x and bomb.rect.y == cube.rect.y:
													bomb_flag = True
													stats.bomb_clicked = True
													stats.game_active = False
													bomb.image = bomb_image
													reset_button.image = setting.cry_image
												if not bomb_flag:
													#当前方格无雷，检测周围方格的雷数并显示
													mine_handle(cube, cubes, bombs, nums)
def right_clicked(setting, screen, cubes, bombs, flags, mouse_x, mouse_y):
	""" 响应右键单击 """
	#遍历cube组，确定是哪个cube被点击中
	for cube in cubes.sprites():
		botton_clicked = cube.rect.collidepoint(mouse_x, mouse_y)
		if botton_clicked:
			#左键翻开的格子不能再右键单击
			if not cube.clicked:
				if cube.flag_status < 2:
					cube.flag_status += 1
				else:
					cube.flag_status = 0
				cube.image = flags[cube.flag_status]
			for bomb in bombs.sprites():
				botton_clicked = bomb.rect.collidepoint(mouse_x, mouse_y)
				if botton_clicked:
					if cube.flag_status == 1:
						bomb.flag_status = True
					else:
						bomb.flag_status = False
			
def left_clicked(setting, screen, bombs, cubes, flags, nums, stats, bomb_image, reset_button, mouse_x, mouse_y):
	""" 响应左键单击 """
	if stats.game_active:
		#遍历cube组，确定是哪个cube被点击中
		for cube in cubes.sprites():
			botton_clicked = cube.rect.collidepoint(mouse_x, mouse_y)
			if botton_clicked:
				if not stats.game_started:
					stats.start_time = time.time()
					stats.game_started = True
				#如果是格子非旗帜状态
				if cube.flag_status != 1:
					cube.flag_status = 3
					bomb_flag = False
					#遍历bombs组，确定点击的cube是否有bomb
					for bomb in bombs.sprites():
						botton_clicked = bomb.rect.collidepoint(mouse_x, mouse_y)
						if botton_clicked:
							bomb_flag = True
							#判断是不是第一次点击就触雷,如果是第一次点击就触雷则强制重新随机雷直至该位置为非雷为止
							if stats.first_step:
								first_step_handle(setting, screen, bomb_flag, bombs, mouse_x, mouse_y)
								bomb_flag = False
							else:
								#点中炸弹，游戏失败
								stats.bomb_clicked = True
								stats.game_active = False
								bomb.image = bomb_image
								reset_button.image = setting.cry_image
					if not bomb_flag:
						stats.first_step = False 
						#当前方格无雷，检测周围方格的雷数并显示
						mine_handle(cube, cubes, bombs, nums)
	#确定是否按下的是重置游戏按钮
	check_reset_button(setting, screen, bombs, cubes, stats, reset_button, mouse_x, mouse_y)

							


def check_reset_button(setting, screen, bombs, cubes, stats, reset_button, mouse_x, mouse_y):
	""" 按键后重置游戏 """
	buttion_clicked = reset_button.rect.collidepoint(mouse_x, mouse_y)
	#如果按下，无论游戏处于什么状态都将重置游戏
	if buttion_clicked:
		#重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True
		reset_button.image = setting.normal_image
		
		#清空cubes和bombs群组
		cubes.empty()
		bombs.empty()
		
		#清空记分牌和计时器

	
		#创建新的cubes和随机bombs
		create_cubes(setting, screen, cubes)
		create_bombs(setting, screen, bombs)

def first_step_handle(setting, screen, bomb_flag, bombs, mouse_x, mouse_y):
	""" 第一步就是雷的情况 """
	#不停创建随机雷直到当前按下所在的格子里没有雷为止
	while bomb_flag:
		for bomb in bombs.sprites():
			botton_clicked = bomb.rect.collidepoint(mouse_x, mouse_y)
			if botton_clicked:
				bombs.empty()
				create_bombs(setting, screen, bombs)
			else:
				bomb_flag = False

def mine_handle(cube, cubes, bombs, nums):
	""" 处理当前格子翻开后无雷的情况 """
	#格子未翻开才执行后续操作
	if not cube.clicked:
		num = 0
		cube_rectx = cube.rect.x
		cube_recty = cube.rect.y
		#获取周围方格位置
		around = [[(cube_rectx + 30),cube_recty], [(cube_rectx - 30),cube_recty], [cube_rectx,(cube_recty + 30)], [cube_rectx,(cube_recty - 30)], [(cube_rectx + 30),(cube_recty - 30)], [(cube_rectx + 30),(cube_recty + 30)], [(cube_rectx - 30),(cube_recty - 30)], [(cube_rectx - 30) ,(cube_recty + 30)]]
		for x,y in around:
			for bomb in bombs.sprites():
				if bomb.rect.x == x and bomb.rect.y == y:
					num += 1
		cube.image = nums[num]
		cube.clicked = True
		if num == 0:
			for x,y in around:
				for cube in cubes.sprites():
					if cube.rect.x == x and cube.rect.y == y:
						mine_handle(cube, cubes, bombs, nums)

def check_win(setting, screen, cubes, bombs, stats,reset_button):
	""" 检测游戏是否胜利 """
	num_0 = 0
	num_1 = 0
	for bomb in bombs.sprites():
		if bomb.flag_status:
			num_0 += 1
	for cube in cubes.sprites():
		if cube.flag_status == 1:
			num_1 += 1
	if num_0 == 10 and num_1 == 10:
		#游戏胜利
		stats.game_active = False
		reset_button.image = setting.smile_image
		
def check_flags(setting, screen, cubes, stats):
	""" 检测游戏是否胜利 """
	num = 0
	for cube in cubes.sprites():
		if cube.flag_status == 1:
			num += 1
	stats.bomb_numbers = setting.bomb_numbers - num
			
def update_screen(setting, screen, cubes, bombs, stats,reset_button,sb):
	""" 更新屏幕上的图案并切换到新屏幕 """
	#每次循环时重绘屏幕
	screen.fill(setting.screen_color)
	reset_button.blitme()	
	cubes.draw(screen)
	#游戏失败
	if stats.bomb_clicked:
		bombs.draw(screen)
	if stats.game_active and stats.game_started:
		stats.elapsed_time = int(time.time() - stats.start_time)
	check_flags(setting, screen, cubes, stats)
	sb.prep_left_bombs()
	sb.prep_time()
	sb.show_all()
	#让最近绘制的屏幕可见
	pygame.display.flip()

def create_cube(setting, screen, cubes, line_number, row_number):
	""" 创建一个cube并将其放在当前行 """
	# number_rows = setting.number_rows
	# screen_height = setting.screen_height
	cube = Cube(setting, screen)
	cube_width = cube.rect.width
	cube.x = 1.5 + cube_width * line_number
	cube.rect.y = (setting.screen_height - setting.number_rows * 30) + cube.rect.height * row_number
	cube.rect.x = cube.x
	cubes.add(cube)
 
def create_cubes(setting, screen, cubes):
	""" 创建cube格子 """
	cube = Cube(setting, screen)
	number_lines = setting.number_lines
	number_rows = setting.number_rows

	for row_number in range(number_rows):
		for line_number in range(number_lines):
			#创建一个cube并将其加入当前行
			create_cube(setting, screen, cubes, line_number, row_number)
			
 
def create_bombs(setting, screen, bombs):
	""" 创建随机bombs """
	
	#生成大于10个不重复的二维数组，如果数组长度小于10则再次生成直到数组长度大于10为止
	num = 0
	while num <10:
		random_number_0 = [[random.randint(0,8) for i in range(2)] for j in range(12)]
		#将列表转换为tuple，再通过set去重复数据
		random_number = list(set([tuple(t) for t in random_number_0]))
		num = len(random_number)
	for value in range(10):
		bomb = Bomb(setting, screen)
		bomb_width = bomb.rect.width
		bomb.x = 1.5 + bomb_width * random_number[value][0]
		bomb.rect.y = (setting.screen_height - setting.number_rows * 30) + bomb.rect.height * random_number[value][1]
		bomb.rect.x = bomb.x
		bombs.add(bomb)