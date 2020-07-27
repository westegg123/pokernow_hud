## for now, very simple. just players
class HandHistory:
    _players = []
    _preflop = []

    def __init__(self, players, preflop):
        self._players = players
        self._preflop = preflop

    def players(self):
        return self._players

    def preflop(self):
        return self._preflop

    def players_string(self):
        return ', '.join(self.players())

    def preflop_string(self):
        return ', '.join(map(lambda x: x.to_string(), self.preflop()))