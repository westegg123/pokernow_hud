class DatabaseObjectConverter:

    @staticmethod
    def convert_hand_history(hand_history):
        return {"players": hand_history.players_string(), "preflop": hand_history.preflop_string()} ##todo, implement hand history conversion for all fields