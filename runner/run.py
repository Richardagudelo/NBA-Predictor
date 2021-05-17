from simulation import Simulation

object_season_winners, array_season_winners = Simulation.init_simulation()

print("Objeto resultados 1000 temporadas")
print(object_season_winners)

print("-------")
print("Resultados por temporada")

aux = "";
for season_winner in array_season_winners:
	print(season_winner)
	aux = season_winner.name
	#print('--------------------->' + aux)

from views import MainW
MainW.llenar_team_list(array_season_winners)
MainW.graficarImagen(aux)





