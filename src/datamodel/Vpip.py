from datamodel.Statistic import Statistic


class Vpip(Statistic):
    def __init__(self, value, occurences):
        super(Vpip, self).__init__("Vpip", value, occurences)