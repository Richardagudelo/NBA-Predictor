from nba_api.stats.endpoints import teamestimatedmetrics

from models.Conference import Conference
from models.Division import Division
from models.Team import Team

east_conference = Conference('East')
west_conference = Conference('West')

atlantic = Division('Atlantic')
southeast = Division('Southeast')
central = Division('Central')
northwest = Division('Northwest')
pacific = Division('Pacific')
southwest = Division('Southwest')


def fillDivisionsTeams():
    result = teamestimatedmetrics.TeamEstimatedMetrics('00', '2019-20', 'Regular Season')

    equipos = result.get_dict()["resultSet"]["rowSet"]  # vector de equipos

    for i in range(0, len(equipos)):
        equipo = equipos[i]

        if equipo[1] in {1610612737, 1610612748, 1610612753, 1610612764, 1610612766}:
            southeast.add_team(Team(equipo[1], equipo[0], 0, equipo[4], equipo[5]))
        elif equipo[1] in {1610612738, 1610612751, 1610612752, 1610612755, 1610612761}:
            atlantic.add_team(Team(equipo[1], equipo[0], 0, equipo[4], equipo[5]))
        elif equipo[1] in {1610612739, 1610612741, 1610612749, 1610612754, 1610612765}:
            central.add_team(Team(equipo[1], equipo[0], 0, equipo[4], equipo[5]))
        elif equipo[1] in {1610612740, 1610612742, 1610612745, 1610612759, 1610612763}:
            southwest.add_team(Team(equipo[1], equipo[0], 0, equipo[4], equipo[5]))
        elif equipo[1] in {1610612743, 1610612750, 1610612757, 1610612760, 1610612762}:
            northwest.add_team(Team(equipo[1], equipo[0], 0, equipo[4], equipo[5]))
        else:
            pacific.add_team(Team(equipo[1], equipo[0], 0, equipo[4], equipo[5]))


def fillConferences():
    east_conference.add_division(central)  # Central
    east_conference.add_division(southeast)  # Southeast
    east_conference.add_division(atlantic)  # Atlantic

    west_conference.add_division(southwest)  # Southwest
    west_conference.add_division(pacific)  # Pacific
    west_conference.add_division(northwest)  # Northwest


def initAll():
    fillDivisionsTeams()
    fillConferences()


def get_conference_east():
    return east_conference


def get_conference_west():
    return west_conference


def printAll():
    print("Conferencia este")
    for east_divisions in east_conference.divisions:
        print(east_divisions)

    print()
    print("Conferencia oeste")
    for west_divisions in west_conference.divisions:
        print(west_divisions)
