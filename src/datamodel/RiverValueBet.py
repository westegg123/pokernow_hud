from datamodel.Statistic import Statistic


class RiverValueBet(Statistic):
    def __init__(self, value, occurences):
        super(RiverValueBet, self).__init__("rvb", value, occurences)