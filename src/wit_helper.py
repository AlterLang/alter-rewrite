import constants
from wit import Wit

class WitHelper:
    def __init__(self):
        self.client = Wit(constants.WIT_KEY)

    def get_response(self, text):
        return self.client.message(text)
