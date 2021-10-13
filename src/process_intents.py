class PrintPlain():
    def __init__(self, response):
        self.response = response["entities"]
        self.process()
        self.translate()

    def process(self):
        self.text = self.response[0]["value"]
    
    def format(self):
        return f"print(\"{ self.text }\")"
    
    def translate(self):
        print(self.format())
        return self.format()
    
    

class ProcessHead:
    def __init__(self, response):
        self.response = response
    
    