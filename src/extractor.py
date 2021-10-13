class Extractor:
    def __init__(self):
        pass

    def extract(self, response):
        intent = response['intents'][0]['name']
        entities = []
        for i in response['entities']:
            name = i
            for j in response['entities'][i]:
                value = j['value']
                entities.append({'name': name, 'value': value})
        print(intent, entities)
        return {'intent': intent, 'entities': entities}
