from db.DatabaseObjectConverter import DatabaseObjectConverter

class Retriever:
    _client = ""

    def __init__(self, client):
        self._client = client

    def retrieve_player_statistics(self, player_name):
        query = { "player" : player_name}
        return self._client.db().player_statistics.find_one(query) ## todo: andkom - extract constant to file (player_statistics)

    def retrieve_all_player_statistics(self):
        return self._client.db().player_statistics.find()