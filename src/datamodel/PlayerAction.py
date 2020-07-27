class PlayerAction:
    _player = ""
    _action = ""

    def __init__(self, player, action):
        self._player = player
        self._action = action

    def action(self):
        return self._action

    def player(self):
        return self._player

    def to_string(self):
        return self.player() + ": " + self.action()