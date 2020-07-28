from ConfigParser import ConfigParser
from db.ClientConnection import ClientConnection


class Calculator:
    _client_connection = ""

    def __init__(self):
        self._client_connection = ClientConnection(ConfigParser("C:\\Users\\Admin\\dev\\pokernow_hud\\config\\db_connection").get_config_value("db_connection_string"))

    def get_all_hand_histories(self):
        documents = []
        cursor = self._client_connection.db().hand_histories.find() ##todo: andkom - insert hand_histories to config
        for document in cursor:
            documents.append(document)
        return documents
