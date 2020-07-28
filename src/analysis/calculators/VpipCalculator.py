from analysis.calculators.Calculator import Calculator
from datamodel.Vpip import Vpip


class VpipCalculator(Calculator):
    def __init__(self):
        super(VpipCalculator, self).__init__()

    def calculate(self, player_name):
        hand_histories = self.get_all_hand_histories()

        vpip_count = 0
        hand_count = 0
        for hand_history_dict in hand_histories:
            if player_name in hand_history_dict["players"]:
                hand_count += 1
                vpip_count += self.vpip_any_street(player_name, hand_history_dict)
        return Vpip(vpip_count / hand_count, hand_count)

    def vpip_any_street(self, player, hand_history):
        for vpip_action_string in self.vpip_action_strings(player):
            if vpip_action_string in hand_history["preflop"] or vpip_action_string in hand_history["flop"] or vpip_action_string in hand_history["turn"] or vpip_action_string in hand_history["river"]:
                return 1
        return 0

    def vpip_action_strings(self, player):
        return [player + ": raise", player + ": call"]
