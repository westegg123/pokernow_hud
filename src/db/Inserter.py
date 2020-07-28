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