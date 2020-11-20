import threading

from datamodel.PlayerStatistics import PlayerStatistics


class AnalysisService:
    _calculators = []
    _inserter = ""

    def __init__(self, inserter, calculators):
        self._calculators = calculators
        self._inserter = inserter

    def start(self):
        timer = threading.Event()
        while not timer.wait(10.0):  ##todo: andkom - extract time to config
            self.run()

    def run(self):
        for name in ["Andreas", "Yutes", "sotiri", "Steven", "Ahmet", "Jim", "btakao", "Ran", "aakash", "Jake"]:
            print("Updating " + name)
            player_stats = PlayerStatistics(name)
            for calculator in self._calculators:
                statistic = calculator.calculate(name, 8) ##todo: andkom - run for all names
                player_stats.add_stat(statistic)
            self.update_player_statistic(player_stats)
            print("Updated " + name)

    def update_player_statistic(self, player_statistics):
        return self._inserter.insert_player_statistics(player_statistics)
