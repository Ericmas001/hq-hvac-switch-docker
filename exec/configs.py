class AppConfig:

    def __init__(self, config):
        self.pin_on = int(config["pin_on"])
        self.pin_off = int(config["pin_off"])
        self.api_key = config["api_key"]
        self.base_url = config["base_url"]