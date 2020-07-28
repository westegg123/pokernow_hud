class PlayerAction:
    _player = ""
    _action = ""
    _amount = ""

    ##todo: andkom - add amount to player action
    def __init__(self, player, action):
        self._player = player
        self._action = action
        self._amount = ""

    def action(self):
        return self._action

    def player(self):
        return self._player

    def amount(self):
        return self._amount

    def to_string(self):
        amount = "" if self.amount() == "" else ":" + self.amount()
        return self.player() + ": " + self.action() + amount