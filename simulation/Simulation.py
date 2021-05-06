from random import random
from models import Team, Division, Conference, PlayOffBracket
from simulation import CreateModel

CreateModel.initAll()
# CreateModel.printAll()


east_conference = CreateModel.get_conference_east()
west_conference = CreateModel.get_conference_west()

east_playoff = []
west_playoff = []


def restart_east_conference(east_conference):
	for eadiv in east_conference.divisions:
		for eadivteam in eadiv.teams:
			eadivteam.change_win_prob()


def restart_west_conference(west_conference):
	for wediv in west_conference.divisions:
		for wedivteam in wediv.teams:
			wedivteam.change_win_prob()


def restart_all(east_playoff, west_playoff):
	restart_east_conference(east_conference)
	restart_west_conference(west_conference)
	east_playoff = []
	west_playoff = []


def simulate_game(the_team=Team):
	random_number = random()
	if random_number < the_team.win_prob:
		the_team.add_win()


def simulate_match(team1=Team, team2=Team):
	for ipi in range(0, 100):
		simulate_game(team1)
		simulate_game(team2)

	if team1.wins < team2.wins:
		return team2
	elif team1.wins > team2.wins:
		return team1
	else:
		if random() > 0.5:
			return team1
		else:
			return team2


def simulate_playoff_match(team1: Team, team2: Team):
	team1.restart_playoff_wins()
	team2.restart_playoff_wins()

	while True:
		winner = simulate_match(team1, team2)
		if winner == team1:
			team1.add_play_off_win()
		else:
			team2.add_play_off_win()

		if team1.playoffwins > 3 or team2.playoffwins > 3:
			break

	return team1 if team1.playoffwins > 3 else team2


def simulate_division(division=Division):
	for team in division.teams:
		for team2 in division.teams:
			if team.id != team2.id:
				winner = simulate_match(team, team2)
				winner.add_win()


def simulate_div_vs_div(conference=Conference):
	for div in conference.divisions:
		simulate_division(div)
		simulate_division(div)

		for team_div in div.teams:
			for divi in conference.divisions:
				if divi.name != div.name:
					for teami in divi.teams:
						simulate_match(team_div, teami)


# Conferencia este - todos los partidos de conferencia
def simulate_east_conference(east_conference=Conference):
	simulate_div_vs_div(east_conference)
	east_teams = []
	for division in east_conference.divisions:
		for team in division.teams:
			east_teams.append(team)
	return east_teams


# Conferencia oeste - todos los partidos de conferencia
def simulate_west_conference(west_conference=Conference):
	simulate_div_vs_div(west_conference)
	west_teams = []
	for division in west_conference.divisions:
		for team in division.teams:
			west_teams.append(team)
	return west_teams


def simulate_conference_vs_conference(east_conference=[], west_conference=[]):
	for east_team in east_conference:
		for west_team in west_conference:
			simulate_match(east_team, west_team)


def sort_teams_by_wins(teams):
	teams.sort(key=lambda team: team.wins, reverse=True)
	return teams


def get_play_offs_teams(teams):
	return teams[:8]


def calculate_east_and_west_play_offs():
	aux_east_playoff = simulate_east_conference(east_conference)
	# simula la conferencia
	aux_west_playoff = simulate_west_conference(west_conference)

	# Simula conferencia vs conferencia
	simulate_conference_vs_conference(east_playoff, west_playoff)

	# ordena las listas de conferencias por juegos ganados desc
	aux_east_playoff = sort_teams_by_wins(aux_east_playoff)
	aux_west_playoff = sort_teams_by_wins(aux_west_playoff)

	# obtiene los playOffs de cada conferencia
	aux_east_playoff = get_play_offs_teams(aux_east_playoff)
	aux_west_playoff = get_play_offs_teams(aux_west_playoff)

	return aux_east_playoff, aux_west_playoff


def create_conference_playoff_bracket(out_east_or_west_playoff):
	"""
	Crea el bracket exterior (octavos de final) de la conferencia este o este, la que reciba por parametro
	"""
	playoff_bracket = []
	while len(out_east_or_west_playoff) > 0:
		first_team, last_team = out_east_or_west_playoff[0], out_east_or_west_playoff[-1]
		playoff_bracket.append(PlayOffBracket.PlayOffBracket(first_team, last_team))
		out_east_or_west_playoff = out_east_or_west_playoff[1:len(out_east_or_west_playoff) - 1]

	return playoff_bracket


def simulate_octavos_playoff(octavos_bracket: PlayOffBracket):
	"""
	Simula el playoff mas exterior
	"""
	cuartos = []

	cuartos.append(
		PlayOffBracket.PlayOffBracket(
			simulate_playoff_match(octavos_bracket[0].teamone, octavos_bracket[0].teamtwo),
			simulate_playoff_match(octavos_bracket[3].teamone, octavos_bracket[3].teamtwo)
		))

	cuartos.append(
		PlayOffBracket.PlayOffBracket(
			simulate_playoff_match(octavos_bracket[2].teamone, octavos_bracket[2].teamtwo),
			simulate_playoff_match(octavos_bracket[1].teamone, octavos_bracket[1].teamtwo)
		))

	return cuartos


def simulate_cuartos_playoff(cuartos_bracket: PlayOffBracket):
	"""
	Simula los cuartos de  final de una temporada y retorna la semifinal
	:return: la semifinal de la temporada
	"""
	return PlayOffBracket.PlayOffBracket(
		simulate_playoff_match(cuartos_bracket[0].teamone, cuartos_bracket[0].teamtwo),
		simulate_playoff_match(cuartos_bracket[1].teamone, cuartos_bracket[1].teamtwo),
	)


def simulate_semifinals_playoff(semifinal_este: PlayOffBracket, semifinal_oeste: PlayOffBracket):
	"""
	Simula una semifinal
	:param semifinal:
	:return: la FINAL
	"""
	return PlayOffBracket.PlayOffBracket(
		simulate_playoff_match(semifinal_este.teamone, semifinal_este.teamtwo),
		simulate_playoff_match(semifinal_oeste.teamone, semifinal_oeste.teamtwo)
	)


def simulate_to_calculate_final_of_season():
	"""
	Inicia la simulación
	"""
	east_playoff, west_playoff = calculate_east_and_west_play_offs()

	octavos_east = create_conference_playoff_bracket(east_playoff)
	octavos_west = create_conference_playoff_bracket(west_playoff)

	cuartos_east = simulate_octavos_playoff(octavos_east)
	cuartos_west = simulate_octavos_playoff(octavos_west)

	semifinal_east = simulate_cuartos_playoff(cuartos_east)
	semifinal_west = simulate_cuartos_playoff(cuartos_west)

	return simulate_semifinals_playoff(semifinal_east, semifinal_west)


def simulate_season():
	final = simulate_to_calculate_final_of_season()
	final_winner = simulate_playoff_match(final.teamone, final.teamtwo)
	final_winner.add_season_win()
	return final_winner


def init_simulation():
	seasons_results = {}
	array_results = []

	for it in range(0, 1000):
		restart_all(east_playoff, west_playoff)

		season_winner = simulate_season()
		if season_winner.name not in seasons_results:
			seasons_results[season_winner.name] = 1
		else:
			seasons_results[season_winner.name] += 1
		array_results.append(season_winner)

	return seasons_results, array_results


# seas_results, arrayr = init_simulation()
# print(seas_results)
#
# for k in arrayr:
# 	print(k)