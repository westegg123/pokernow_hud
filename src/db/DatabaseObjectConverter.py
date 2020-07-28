class DatabaseObjectConverter:

    @staticmethod
    def convert_hand_history(hand_history):
        return {"players": hand_history.players_string(),
                "preflop": hand_history.street_string(hand_history.preflop()),
                "flop": hand_history.street_string(hand_history.flop()),
                "turn": hand_history.street_string(hand_history.turn()),
                "river": hand_history.street_string(hand_history.river())}