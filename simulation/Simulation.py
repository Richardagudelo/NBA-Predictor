from random import random
from models import Team, Division, Conference
from simulation import CreateModel

CreateModel.initAll()
# CreateModel.printAll()


east_conference = CreateModel.get_conference_east()
west_conference = CreateModel.get_conference_west()

east_playoff = []
west_playoff = []


def simulate_game(the_team=Team):
    random_number = random()
    if random_number < the_team.win_prob:
        the_team.add_win()


def simulate_match(team1=Team, team2=Team):
    for i in range(0, 100):
        simulate_game(team1)
        simulate_game(team2)

    if team1.wins < team2.wins:
        return team2
    elif team1.wins > team2.wins:
        return team1
    else:
        return simulate_match(team1, team2)


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


##Conferencia este - todos los partidos de conferencia
def simulate_east_conference(east_conference=Conference):
    simulate_div_vs_div(east_conference)
    east_teams = []
    for division in east_conference.divisions:
        for team in division.teams:
            east_teams.append(team)
    return east_teams


##Conferencia oeste - todos los partidos de conferencia
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


def sort_teams_by_wins(teams=list):
    teams.sort(key=lambda team: team.wins, reverse=True)
    return teams


def get_play_offs_teams(teams=list):
    return teams[:8]

    # def start_simulation(east_conference=Conference, west_conference=Conference, east_playoff=[], west_playoff=[]):


east_playoff = simulate_east_conference(east_conference)
# simula la conferencia
west_playoff = simulate_west_conference(west_conference)

# Simula conferencia vs conferencia
simulate_conference_vs_conference(east_playoff, west_playoff)

# ordena las listas de conferencias por juegos ganados desc
east_playoff = sort_teams_by_wins(east_playoff)
west_playoff = sort_teams_by_wins(west_playoff)

# obtiene los playOffs de cada conferencia
east_playoff = get_play_offs_teams(east_playoff)
west_playoff = get_play_offs_teams(west_playoff)

# start_simulation(east_conference, west_conference,east_playoff,west_playoff)

# print("len ", east_playoff)

print("east top 8 conference")
for top_e in east_playoff:
    print(top_e)

print("")
print("")
print("west top 8 conference")
for top_e in west_playoff:
    print(top_e)
