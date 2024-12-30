
import json
from datetime import datetime

class MessageHistory:
    def __init__(self, history_file='message_history.json'):
        self.history_file = history_file
        self.messages = self.load_history()

    def load_history(self):
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except:
            return []

    def add_message(self, user_message, bot_response):
        self.messages.append({
            'timestamp': datetime.now().isoformat(),
            'user_message': user_message,
            'bot_response': bot_response
        })
        self.save_history()

    def save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.messages, f, indent=2)