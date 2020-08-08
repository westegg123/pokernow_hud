import flask
from bson import json_util


class Application:

    def __init__(self, retriever):
        self._app = flask.Flask(__name__)
        self._retriever = retriever

        ## Routes
        @self._app.route('/statistics/<player_name>', methods=["GET"])
        def get_all_statistics(player_name):
            return json_util.dumps(self._retriever.retrieve_player_statistics(player_name))

    def start(self):
        return self._app.run()



