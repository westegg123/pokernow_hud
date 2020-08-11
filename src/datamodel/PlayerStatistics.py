class PlayerStatistics:
    _player_name = ""
    _statistics = {}

    def __init__(self, name):
        self._player_name = name

    def add_stat(self, stat):
        self._statistics[stat.name()] = {"value": stat.value(), "occurences": stat.occurences()}

    def name(self):
        return self._player_name

    def statistics(self):
        return self._statistics