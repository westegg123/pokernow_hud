import flask
from bson import json_util


class Application:

    def __init__(self, retriever):
        self._app = flask.Flask(__name__)
        self._retriever = retriever

        ## Routes
        @self._app.route('/api/statistics/<player_name>', methods=["GET"])
        def get_all_statistics_for_player(player_name):
            dumps = json_util.dumps(self._retriever.retrieve_player_statistics(player_name))
            response = flask.Response(dumps)
            response.headers['Access-Control-Allow-Origin'] = '*' ##todo: andkom - better access restriction
            print(response)
            return response

        @self._app.route('/api/statistics/all', methods=["GET"])
        def get_all_statistics():
            all_stats = self._retriever.retrieve_all_player_statistics()
            dumps = json_util.dumps(self._retriever.retrieve_all_player_statistics())
            response = flask.Response(dumps)
            response.headers['Access-Control-Allow-Origin'] = '*'  ##todo: andkom - better access restriction
            print(response)
            return response

    def start(self):
        return self._app.run()



