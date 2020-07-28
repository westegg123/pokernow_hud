from db.DatabaseObjectConverter import DatabaseObjectConverter

class Inserter:
    _client = ""

    def __init__(self, client):
        self._client = client

    def insert_hand_history(self, hand_history):
        converted_hand_history = DatabaseObjectConverter.convert_hand_history(hand_history)
        print(converted_hand_history)
        self._client.db().hand_histories.insert_one(converted_hand_history) ## todo: andkom - extract constant to file (hand_histories)

    def insert_hand_histories(self, hand_histories):
        for hand_history in hand_histories:
            self.insert_hand_history(hand_history)

    def insert_player_statistics(self, player_stats):
        converted_player_stats = DatabaseObjectConverter.convert_player_statistics(player_stats)
        print(converted_player_stats)
        self._client.db().player_statistics.insert_one(converted_player_stats) ## todo: andkom - extract constant to file (player_statistics)