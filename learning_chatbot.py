from english_validator import EnglishValidator
from message_history import MessageHistory
import random

class LearningChatbot:
    def __init__(self):
        self.validator = EnglishValidator()
        self.history = MessageHistory()
        self.responses = self.load_training_data()

    def load_training_data(self):
        responses = {}
        with open('training_data.txt', 'r') as f:
            for line in f:
                if '->' in line:
                    question, answers = line.strip().split('->')
                    responses[question.strip()] = answers.strip().split('|')
        return responses

    def learn_response(self, user_input, response):
        if self.validator.is_english(response) and self.validator.is_grammatically_correct(response):
            if user_input in self.responses:
                if response not in self.responses[user_input]:
                    self.responses[user_input].append(response)
            else:
                self.responses[user_input] = [response]
            self.save_training_data()

    def save_training_data(self):
        with open('training_data.txt', 'w') as f:
            for question, answers in self.responses.items():
                f.write(f"{question} -> {'|'.join(answers)}\n")

    def get_response(self, user_input):
        # Translate if not in English
        if not self.validator.is_english(user_input):
            user_input = self.validator.translate_to_english(user_input)
            if not user_input:
                return "I couldn't understand that. Please try in English."

        # Find response
        if user_input in self.responses:
            response = random.choice(self.responses[user_input])
        else:
            response = "I'm still learning. Could you teach me how to respond to that?"

        # Save interaction
        self.history.add_message(user_input, response)
        return response
