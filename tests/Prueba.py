from nba_api.stats.endpoints import teamestimatedmetrics

resultado = teamestimatedmetrics.TeamEstimatedMetrics('00', '2019-20', 'Regular Season')

equipos = resultado.get_dict()["resultSet"]["rowSet"]  # vector de equipos

for i in range(0, len(equipos)):
	# print(equipos[i][1])
	if equipos[i][1] in {1610612737,
						 1610612748,
						 1610612753,
						 1610612764,
						 1610612766}:
		print('Pertenece a la division Southeast el equipo: ', equipos[i][0], equipos[i][1])