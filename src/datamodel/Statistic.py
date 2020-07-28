class Statistic:
    _name = ""
    _value = ""
    _occurences = ""

    def __init__(self, name, value, occurences):
        self._name = name
        self._value = value
        self._occurences = occurences

    def value(self):
        return self._value

    def name(self):
        return self._name