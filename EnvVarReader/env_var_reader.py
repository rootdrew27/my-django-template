import json
from django.core.exceptions import ImproperlyConfigured


class Secrets():

    def __init__(self, filename:str):
        """Initialize a Secrets Instance   

        Args:
            filename (str): a json file
        """
        try:
            with open(filename) as f:
                self.secrets = json.loads(f.read())
        except OSError:
            error_msg = "The file: {0} failed to open.. Has it been created?".format(filename)
            print(error_msg)

    def getSecret(self, setting:str):
        """Get the secret variable or return explicit exception."""
        try:
            return self.secrets[setting]
        except KeyError:
            error_msg = "Set the {0} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)