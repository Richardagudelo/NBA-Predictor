class Division:

    def __init__(self, name):
        self._name = name
        self._teams = []

    def add_team(self, team):
        self._teams.append(team)

    def __str__(self):
        teams = ""
        for team in self._teams:
            teams += " " + team.name + ","

        return f"{self._name} -> {teams}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    ## get-set teams
    @property
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, teams):
        self._teams = teams
