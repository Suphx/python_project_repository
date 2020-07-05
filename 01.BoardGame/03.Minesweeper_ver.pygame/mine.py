import sys

import game_functions as gf
import pygame

from setting import Setting
from bomb import Bomb
from button import Button
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard





def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	setting = Setting()
	screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
	pygame.display.set_caption('扫雷')
	
	#加载图片资源
	flags = [setting.flag0_image, setting.flag1_image, setting.flag2_image]
	nums = [setting.num_0_image, setting.num_1_image, setting.num_2_image, setting.num_3_image, setting.num_4_image, setting.num_5_image, setting.num_6_image, setting.num_7_image, setting.num_8_image]
	bomb_image = setting.bomb0_image
	
	#创建统计信息和计分牌
	stats = GameStats(setting)
	sb = Scoreboard(setting, screen, stats)
	
	#创建重玩的按键图片
	reset_button = Button(setting, screen)
	
	#创建cubes编组
	cubes = Group()
	gf.create_cubes(setting, screen, cubes)
	
	#创建bombs编制
	bombs = Group()
	gf.create_bombs(setting, screen, bombs)


	
	#开始游戏的主循环
	while True:
		
		gf.check_event(setting, screen, bombs, cubes, flags, nums, stats, bomb_image, reset_button)
		gf.update_screen(setting, screen, cubes, bombs, stats,reset_button,sb)
		gf.check_win(setting, screen, cubes, bombs, stats,reset_button)


run_game()

