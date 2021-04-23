class Player:

	def __init__(self, player_id, name, age, free_throws_percentage):
		self._player_id = player_id
		self._name = name
		self._age = age
		self._free_throws_percentage = free_throws_percentage

	def __str__(self):
		return f"{self.player_id}-{self._name} has {self._age} years old and {self._free_throws_percentage} %"

	@property
	def player_id(self):
		return self._player_id

	@player_id.setter
	def player_id(self, player_id):
		self._player_id = player_id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name