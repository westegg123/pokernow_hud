class DatabaseObjectConverter:

    @staticmethod
    def convert_hand_history(hand_history):
        return {"players": hand_history.players_string(),
                "preflop": hand_history.street_string(hand_history.preflop()),
                "flop": hand_history.street_string(hand_history.flop()),
                "turn": hand_history.street_string(hand_history.turn()),
                "river": hand_history.street_string(hand_history.river()),
                "date": hand_history.hand_timestamp(),
                "winner": hand_history.winner()}

    def convert_player_statistics(player_statistics):
        converted_player_statistics = {}
        converted_player_statistics["stats"] = player_statistics.statistics().copy()
        converted_player_statistics["player"] = player_statistics.name()
        return converted_player_statistics