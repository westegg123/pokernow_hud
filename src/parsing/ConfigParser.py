class ConfigParser:
    _file_path = ""
    _config = {}

    def __init__(self, file_path):
        self._file_path = file_path
        self.parse_file_to_config()

    def parse_file_to_config(self):
        with open(self._file_path, newline='') as file:
            for line in file.readlines():
                parsed = line.split(" = ")
                self._config[parsed[0]] = parsed[1]

    def get_config_value(self, key):
        return self._config[key]