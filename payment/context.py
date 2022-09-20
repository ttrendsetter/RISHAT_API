import yaml
import os
from rishat_api import BASE_DIR
import stripe


class Context:
    """ Project CONSTs """

    @staticmethod
    def read_configs(config_path: str) -> dict:
        with open(config_path, 'r') as f:
            configs = yaml.safe_load(f)
            return configs

    def __init__(self):
        # reading configs
        config_path = os.path.join(BASE_DIR, 'config.yaml')
        config_path_default = os.path.join(BASE_DIR, 'default_config.yaml')
        try:
            configs = self.read_configs(config_path)
        except FileNotFoundError:
            configs = self.read_configs(config_path_default)

        self.sk = configs['secret_key']
        self.pk = configs['public_key']
        # initializing stripe api key
        stripe.api_key = self.sk


context = Context()
