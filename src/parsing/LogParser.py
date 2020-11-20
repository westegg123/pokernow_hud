import csv

from datamodel.HandHistory import HandHistory
from datamodel.PlayerAction import PlayerAction


class LogParser:
    def __init__(self):
        self._player_mappings = {}

    def parse(self, csv_path):
        return self.parse_all_hands(self.get_all_actions(csv_path))

    def get_all_actions(self, csv_path):
        with open(csv_path, newline='') as file:
            reader = csv.reader(file)
            actions = []
            for row in reader:
                entry = list(row)[0]
                timestamp = list(row)[1]
                actions.append(entry + ',' + timestamp)
            return actions

    def parse_all_hands(self, actions):
        actions.reverse() ##view from bottom up, since bottom is first hand
        hand_histories = []
        for i, action in enumerate(actions):
            if "starting hand #" in action:
                hand_history = self.parse_hand(actions[i::])
                hand_histories.append(hand_history)
        return hand_histories

    def parse_hand(self, actions):
        players = set()
        street_actions = self.init_street_actions()
        winner = ""

        street = 0
        for i, action in enumerate(actions):
            if "flop" in action or "turn" in action or "river" in action:
                street = street + 1
            if "collected " in action:
                winner = self.get_player_from_action(action)
            if "ending hand #" in action:
                hand_timestamp = action.split(',')[1]
                return HandHistory(players, street_actions[0], street_actions[1], street_actions[2], street_actions[3], hand_timestamp, winner)
            parsed_player_action = self.get_action_type_from_action(action)
            if parsed_player_action:
                player = self.get_player_from_action(action)
                players.add(player)
                street_actions[street].append(PlayerAction(player, parsed_player_action))

    def get_action_type_from_action(self, action):
        if " raises" in action or " bets " in action:
            return "raise"
        if " folds" in action:
            return "fold"
        if " calls" in action:
            return "call"
        if " checks" in action:
            return "check"
        return False

    def get_player_from_action(self, action):
        return action.split(" ")[0].replace('"', "")

    def init_street_actions(self):
        return {0:[], 1:[], 2:[], 3:[]}
