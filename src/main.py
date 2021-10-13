from wit_helper import WitHelper
from rich import print
from intents import Intents
from extractor import Extractor
class Alter:
    def __init__(self):
        self.wit_helper = WitHelper()
        self.extractor = Extractor()
    def input_code(self):
        self.code = input("> ")
        return self.wit_helper.get_response(self.code)
    def repl(self):
        while True:
            self.intents = Intents(self.extractor.extract(self.input_code()))
            self.intents.execute()
            

alter = Alter()
alter.repl()