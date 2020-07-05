class GameStats():
	""" 跟踪统计游戏的统计信息 """
	def __init__(self, setting):
		""" 初始化统计信息 """
		self.setting = setting
		self.reset_stats()
		self.game_active = True
		
	def reset_stats(self):
		""" 初始化游戏运行期间可能发生变化的统计信息 """
		self.first_step = self.setting.first_step
		self.bomb_clicked = self.setting.bomb_clicked
		self.bomb_numbers = self.setting.bomb_numbers
		self.start_time = 0
		self.elapsed_time = 0 
		self.game_started = False

