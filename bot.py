import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters
from neural_network import NeuralNetwork
from memory_manager import MemoryManager
from language_processor import LanguageProcessor
from translator import Translator
from rules_engine import RulesEngine

# Load environment variables
load_dotenv()

class ProtogenBot:
    def __init__(self):
        self.neural_network = NeuralNetwork()
        self.memory = MemoryManager()
        self.language = LanguageProcessor()
        self.translator = Translator()
        self.rules_engine = RulesEngine()
        
        # Get token from environment variables
        token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not token:
            raise ValueError("Telegram bot token not found in environment variables!")
            
        # Replace Updater with Application
        self.application = Application.builder().token(token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        # Update handlers to use new filter syntax
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(CommandHandler('start', self.start))
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello! I'm a Protogen chatbot. Let's talk!")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_message = update.message.text
        user_id = update.message.from_user.id
        
        # Translate if not English
        if not self.language.is_english(user_message):
            user_message = self.translator.translate_to_english(user_message)
        
        # Get context from memory
        user_context = self.memory.get_context(user_id)
        
        # Try rules engine first
        rule_response, confidence = self.rules_engine.get_best_response(
            user_message, 
            user_context
        )
        
        if confidence > 0.7:  # High confidence in rule-based response
            response = rule_response
        else:
            # Fallback to neural network
            response = self.neural_network.generate_response(user_message, user_context)
        
        # Apply personality and store interaction
        self.memory.store_interaction(user_id, user_message, response)
        
        await update.message.reply_text(response)
    
    def run(self):
        self.application.run_polling()

if __name__ == '__main__':
    bot = ProtogenBot()
    bot.run()
