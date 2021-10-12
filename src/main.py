from wit_helper import WitHelper
from rich import print

class Alter:
    def __init__(self):
        self.wit_helper = WitHelper()
    def input_code(self):
        self.code = input("Please input the code: ")
        return self.wit_helper.get_response(self.code)
    def repl(self):
        while True:
            print(self.input_code())

alter = Alter()
print(alter.repl())