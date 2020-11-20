from analysis.calculators.Calculator import Calculator
from datamodel.RiverValueBet import RiverValueBet

class RiverValueBetCalculator(Calculator):
    def __init__(self):
        super(RiverValueBetCalculator, self).__init__()

    def calculate(self, player_name, min_players):
        hand_histories = self.get_all_hand_histories()

        final_river_aggressor = 0
        showdown_win_when_called = 0
        for hand_history_dict in hand_histories:
            if (not self.has_enough_players(hand_history_dict, min_players)):
                continue
            if self.final_river_aggressor(hand_history_dict) == player_name and self.called(hand_history_dict):
                final_river_aggressor += 1
                if hand_history_dict["winner"] == player_name:
                    showdown_win_when_called += 1
        return RiverValueBet(showdown_win_when_called / final_river_aggressor, final_river_aggressor)

    def final_river_aggressor(self, hand_history_dict):
        river_actions = hand_history_dict["river"]
        last_aggressor = ""
        for action in river_actions.split(", "):
            if "raise" in action:
                last_aggressor = action.split(":")[0]
        return last_aggressor

    def called(self, hand_history_dict):
        river = hand_history_dict["river"]
        last_river_raise = river.rfind("raise")
        if last_river_raise > 0 and last_river_raise < river.rfind("call"):
            return True
        return False