import pymongo

class ClientConnection:
    _client = ""

    def __init__(self, connection_string):
        self._client = pymongo.MongoClient(connection_string)

    def db(self):
        return self._client.poker ##todo: andkom - extract constant to file (poker)