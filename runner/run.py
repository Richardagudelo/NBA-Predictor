from simulation import Simulation

object_season_winners, array_season_winners = Simulation.init_simulation()

eighth = Simulation.getEighthList()
quarter = Simulation.getQuarterList()
semifinalE1, semifinalE2, semifinalW1, semifinalW2 = Simulation.getSemifinal()
finalE, finalW = Simulation.getFinal()

print("Objeto resultados 1000 temporadas")
print(object_season_winners)

print("-------")
print("Resultados por temporada")

aux = "";
for season_winner in array_season_winners:
	print(season_winner)
	aux = season_winner.name

from views import MainW
MainW.listOnScreen(eighth, quarter, semifinalE1, semifinalE2, semifinalW1, semifinalW2, finalE, finalW)
MainW.graficarImagen(aux)





