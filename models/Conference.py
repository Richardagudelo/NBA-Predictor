class Conference:

	def __init__(self, name):
		self._name = name
		self._divisions = []

	def add_division(self, division):
		self._divisions.append(division)

	def __str__(self):
		divisions = ""
		for division in self._divisions:
			divisions += "," + division.name

		return f"{self._name} -> {divisions}"

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def divisions(self):
		return self._divisions

	@divisions.setter
	def divisions(self, divisions):
		self._divisions = divisions