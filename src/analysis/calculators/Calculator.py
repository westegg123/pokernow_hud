from parsing.ConfigParser import ConfigParser
from db.ClientConnection import ClientConnection


class Calculator:
    _client_connection = ""

    def __init__(self):
        self._client_connection = ClientConnection(ConfigParser("C:\\Users\\Admin\\dev\\pokernow_hud\\config\\db_connection").get_config_value("db_connection_string"))

    def calculate(self, player_name, min_players):
        pass

    def get_all_hand_histories(self):
        documents = []
        cursor = self._client_connection.db().hand_histories.find() ##todo: andkom - insert hand_histories to config
        for document in cursor:
            documents.append(document)
        return documents

    def has_enough_players(self, hand_history, min_players):
        return len(hand_history['players'].split(',')) >= min_players
