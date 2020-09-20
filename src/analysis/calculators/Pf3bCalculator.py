from analysis.calculators.Calculator import Calculator
from datamodel.Pf3b import Pf3b


class Pf3bCalculator(Calculator):
    def __init__(self):
        super(Pf3bCalculator, self).__init__()

    def calculate(self, player_name):
        hand_histories = self.get_all_hand_histories()

        pf3b_count = 0
        hand_count = 0
        for hand_history_dict in hand_histories:
            raise_tree = self.parse_raise_history(hand_history_dict)
            if len(raise_tree) >= 2:
                pf3b_tier = raise_tree[1]
                if pf3b_tier[0] == player_name:
                    pf3b_count += 1
                if player_name in pf3b_tier[1]:
                    hand_count += 1

        return Pf3b(pf3b_count / hand_count, hand_count)

    def parse_raise_history(self, hand_history):
        raise_tree = []
        players = hand_history['players']
        preflop = hand_history['preflop']
        raises = preflop.split(': raise')

        for tier in raises[:-1]:
            could_have_raised = []
            for player in players.split(', '):
                if player in tier:
                    could_have_raised.append(player)
            raiser = tier.split(', ')[-1]
            raise_tree.append([raiser, could_have_raised])
        could_have_raised = []
        for player in players.split(', '):
            if player in raises[-1]:
                could_have_raised.append(player)
        raise_tree.append(["", could_have_raised])
        return raise_tree
