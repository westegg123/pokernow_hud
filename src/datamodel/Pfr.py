from datamodel.Statistic import Statistic


class Pfr(Statistic):
    def __init__(self, value, occurences):
        super(Pfr, self).__init__("Pfr", value, occurences)