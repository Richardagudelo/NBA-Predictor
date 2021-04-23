from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import teamestimatedmetrics

teams = teams.get_teams()
teamGame = teamgamelog.TeamGameLog(1610612741, '2020-21', 'Regular Season')

# for team in teams:
# 	print(team['id'], team['full_name'])

# print(teamGame.get_json())

exame = teamestimatedmetrics.TeamEstimatedMetrics('00', '2020-21', 'Regular Season')
a = exame.get_dict()
resultSet = a['resultSet']
# 0, 5
teamis = resultSet['rowSet']
print("Nombre Equipo" + "\t\t" + "% de win\n")
for tami in teamis:
	print(tami[0] + "\t\t" + str(tami[5]))

# print(exame.get_json())