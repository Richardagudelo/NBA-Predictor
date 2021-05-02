class Team:

    def __init__(self, team_id, name, wins, loses, win_prob):
        self._id = team_id
        self._name = name
        self._wins = wins
        self._loses = loses
        self._win_prob = win_prob

    def __str__(self):
        return f"{self._name} -> {self._win_prob} victorias: {self._wins}"

    def add_win(self):
        self._wins += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, wins):
        self._wins = wins

    @property
    def win_prob(self):
        return self._win_prob

    @win_prob.setter
    def win_prob(self, win):
        self._win_prob = win

    #get set id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, team_id):
        self._id = team_id