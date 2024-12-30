import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

class LanguageProcessor:
    def __init__(self):
        self.grammar_rules = self.load_grammar_rules()
    
    def load_grammar_rules(self):
        return {
            'subject_verb_agreement': r'\b(I|you|we|they)\s+(am|is|are)\b',
            'article_usage': r'\b(a|an|the)\s+[aeiou]',
            'punctuation': r'[.,!?]$'
        }
    
    def is_english(self, text):
        # Simple check for English text
        english_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        text_chars = set(text)
        return len(text_chars - english_chars) / len(text) < 0.2
    
    def is_grammatically_correct(self, text):
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        
        # Check basic grammar rules
        has_subject = False
        has_verb = False
        
        for word, tag in pos_tags:
            if tag.startswith('NN'):  # Noun
                has_subject = True
            elif tag.startswith('VB'):  # Verb
                has_verb = True
        
        # Check sentence structure
        has_proper_structure = has_subject and has_verb
        has_proper_punctuation = bool(re.search(self.grammar_rules['punctuation'], text))
        
        return has_proper_structure and has_proper_punctuation
