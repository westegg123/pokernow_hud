class HandHistory:
    def __init__(self, players, preflop, flop, turn, river, hand_timestamp, winner):
        self._players = [player.replace("'", "").replace('"', "") for player in players]
        self._preflop = preflop
        self._flop = flop
        self._turn = turn
        self._river = river
        self._hand_timestmap = hand_timestamp
        self._winner = winner

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

    def hand_timestamp(self):
        return self._hand_timestmap

    def winner(self):
        return self._winner