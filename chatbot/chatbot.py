import json
import random
import wikipedia


class ChatBot:
    def __init__(self, userAnswer):
        self.userAnswer = userAnswer
        with open('chatbot.json') as json_file:
            self.data = json.load(json_file)

    def check_answer(self):
        while True:
            for p in self.data['chatbot']:
                if p['tag'] != 'noanswer':
                    for i in p['patterns']:
                        if i == self.userAnswer:
                            return random.choice(p['responses'])
                else:
                    return 'I search on wikipedia the informations for {}'.format(str(self.userAnswer)) + '\r\n' + wikipedia.summary(self.userAnswer, sentences=2)
