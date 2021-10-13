from process_intents import *
class Intents:
    def __init__(self, response):
        self.response = response
        head = ProcessHead(self.response)
        self.intents = {
            "print_plain": PrintPlain,
        }
    def get_intent(self):
        return self.intents[self.response["intent"]]
    
    def execute(self):
        self.get_intent()(self.response)
