from datamodel.Statistic import Statistic


class Pf3b(Statistic):
    def __init__(self, value, occurences):
        super(Pf3b, self).__init__("pf3b", value, occurences)