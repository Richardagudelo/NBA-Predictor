class Team:

	def __init__(self, team_id, name, games_played, wins, loses, win_probability, total_points,
				 free_throws_made, free_throws_percentage):
		self.id = team_id
		self.name = name
		self.games_played = games_played
		self.wins = wins
		self.loses = loses
		self.win_probability = win_probability
		self.total_points = total_points
		self.free_throws_made = free_throws_made
		self.free_throws_percentage = free_throws_percentage
		self.players = []

	def add_player(self, player):
		self.players.append(player)