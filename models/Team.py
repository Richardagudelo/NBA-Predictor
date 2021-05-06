from random import random


class Team:

	def __init__(self, team_id, name, wins, loses, win_prob):
		self._id = team_id
		self._name = name
		self._wins = wins
		self._loses = loses
		self._win_prob = win_prob
		self._playoffwins = 0
		self._seasonwins = 0

	def __str__(self):
		return f"{self._name} -> {self._win_prob} victorias: {self._wins} ### Playoff wins {self._playoffwins} %%% Season wins: {self._seasonwins}"

	def add_win(self):
		self._wins += 1

	def add_play_off_win(self):
		self._playoffwins += 1

	def restart_playoff_wins(self):
		self._playoffwins = 0

	def add_season_win(self):
		self._seasonwins += 1

	def change_win_prob(self):
		random_number = random()
		if random_number > 0.60:
			self._win_prob += 0.01
		else:
			self._win_prob -= 0.01

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def wins(self):
		return self._wins

	@wins.setter
	def wins(self, wins):
		self._wins = wins

	@property
	def win_prob(self):
		return self._win_prob

	@win_prob.setter
	def win_prob(self, win):
		self._win_prob = win

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, team_id):
		self._id = team_id

	@property
	def playoffwins(self):
		return self._playoffwins

	@playoffwins.setter
	def playoffwins(self, playoffwins):
		self._playoffwins = playoffwins

	@property
	def seasonwins(self):
		return self._seasonwins

	@seasonwins.setter
	def seasonwins(self, seasonwins):
		self._seasonwins = seasonwins