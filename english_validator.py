import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from googletrans import Translator

class EnglishValidator:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        self.translator = Translator()

    def is_english(self, text):
        try:
            detected = self.translator.detect(text)
            return detected.lang == 'en'
        except:
            return False

    def translate_to_english(self, text):
        try:
            translation = self.translator.translate(text, dest='en')
            return translation.text
        except:
            return None

    def is_grammatically_correct(self, text):
        try:
            tokens = word_tokenize(text)
            tagged = pos_tag(tokens)
            # Basic check for sentence structure
            has_verb = any(tag.startswith('VB') for word, tag in tagged)
            return has_verb
        except:
            return False
