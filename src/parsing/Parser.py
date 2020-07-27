import csv

from datamodel.HandHistory import HandHistory
from datamodel.PlayerAction import PlayerAction


class Parser:
    ##todo: andkom - implement more than just vpip parsing
    def __init__(self):
        return

    def parse(self, csv_path):
        return self.get_preflop_actions(self.get_all_actions(csv_path))

    def get_all_actions(self, csv_path):
        with open(csv_path, newline='') as file:
            reader = csv.reader(file)
            actions = []
            for row in reader:
                entry = list(row)[0]
                actions.append(entry)
            return actions

    ##todo: andkom - also include hands that fold through
    def get_preflop_actions(self, actions):
        preflop_hand_histories = []
        for i, action in enumerate(actions):
            if "flop:" in action:
                players = set()
                preflop_hand_history_actions = []
                while "starting hand" not in actions[i]:
                    current_action = actions[i]
                    action = self.get_action_type_from_action(current_action)
                    if action == False:
                        i = i+1
                        continue
                    player = self.get_player_from_action(current_action)

                    players.add(player)
                    preflop_hand_history_actions.append(PlayerAction(player, action))
                    i = i+1
                preflop_hand_history_actions.reverse()
                preflop_hand_histories.append(HandHistory(players, preflop_hand_history_actions))
        return preflop_hand_histories

    def get_action_type_from_action(self,action):
        if "raise" in action:
            return "raise"
        if "fold" in action:
            return "fold"
        if "call" in action:
            return "call"
        if "check" in action:
            return "check"
        return False

    def get_player_from_action(self, action):
        return action.split(" ")[0]