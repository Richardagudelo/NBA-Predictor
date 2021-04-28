class Team:

	# crear conferencia con vector de divisiones
	# crear interfaz division con vector de equipos

	def __init__(self, team_id, name, wins, loses, win_prob):
		self._id = team_id
		self._name = name
		self._wins = wins
		self._loses = loses
		self._win_prob = win_prob

	def __str__(self):
		return "to string"

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name