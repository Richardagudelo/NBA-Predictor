from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.static import teams

teams = teams.get_teams()

# {'id': 1610612737, 'full_name': 'Atlanta Hawks', 'abbreviation': 'ATL', 'nickname': 'Hawks', 'city': 'Atlanta',
# 'state': 'Atlanta', 'year_founded': 1949} {'id': 1610612743, 'full_name': 'Denver Nuggets', 'abbreviation': 'DEN',
# 'nickname': 'Nuggets', 'city': 'Denver', 'state': 'Colorado', 'year_founded': 1976}

dict_division = {}
dict_conferences = {}

for team in teams:
	team_info_common = teaminfocommon.TeamInfoCommon(team.get("id"), "00", "2019-20", 'Regular Season')
	team_info = team_info_common.get_dict()["resultSets"][0]['rowSet'][0]
	division = team_info[6]
	team_id = team_info[0]

	if division not in dict_division:
		dict_division[division] = [team_id]
	else:
		dict_division[division].append(team_id)

print(dict_division)

# 1610612737
# team_info_common = teaminfocommon.TeamInfoCommon('1610612737', "00", "2019-20", 'Regular Season')
# team_info = team_info_common.get_dict()["resultSets"][0]['rowSet'][0]
# print(team_info)