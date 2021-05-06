class PlayOffBracket:

	def __init__(self, teamone, teamtwo):
		self._teamone = teamone
		self._teamtwo = teamtwo

	def __str__(self):
		return f"{self._teamone} -VS- {self._teamtwo}"

	@property
	def teamone(self):
		return self._teamone

	@teamone.setter
	def teamone(self, teamone):
		self._teamone = teamone

	@property
	def teamtwo(self):
		return self._teamtwo

	@teamtwo.setter
	def teamtwo(self, teamtwo):
		self._teamtwo = teamtwo