from analysis.calculators.Calculator import Calculator
from datamodel.Pfr import Pfr


class PfrCalculator(Calculator):
    def __init__(self):
        super(PfrCalculator, self).__init__()

    def calculate(self, player_name, min_players):
        hand_histories = self.get_all_hand_histories()

        rfi_count = 0
        hand_count = 0
        for hand_history_dict in hand_histories:
            if (not self.has_enough_players(hand_history_dict, min_players)):
                continue
            if player_name in hand_history_dict["players"]:
                hand_count += 1
                rfi_count += self.pfr(player_name, hand_history_dict)
        return Pfr(rfi_count / hand_count, hand_count)

    def pfr(self, player, hand_history):
        for pfr_action_string in self.pfr_action_strings(player):
            if pfr_action_string in hand_history["preflop"]:
                return 1
        return 0

    def pfr_action_strings(self, player):
        return [player + ": raise"]
