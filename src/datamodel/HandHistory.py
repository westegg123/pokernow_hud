class HandHistory:
    _players = []
    _preflop = []
    _flop = []
    _turn = []
    _river = []

    def __init__(self, players, preflop, flop, turn, river):
        self._players = players
        self._preflop = preflop
        self._flop = flop
        self._turn = turn
        self._river = river

    def players(self):
        return self._players

    def preflop(self):
        return self._preflop

    def flop(self):
        return self._flop

    def turn(self):
        return self._turn

    def river(self):
        return self._river

    def players_string(self):
        return ', '.join(self.players())

    def street_string(self, street_action):
        return ', '.join(map(lambda x: x.to_string(), street_action))