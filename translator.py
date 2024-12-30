import re
from langdetect import detect
import numpy as np

class Translator:
    def __init__(self):
        self.word_vectors = {}
        self.translation_memory = {}
        self.embedding_size = 300
        
    def translate_to_english(self, text):
        try:
            # Detect language
            source_lang = detect(text)
            if source_lang == 'en':
                return text
                
            # Check translation memory
            if text in self.translation_memory:
                return self.translation_memory[text]
            
            # Tokenize input
            words = self._tokenize(text)
            translated_words = []
            
            for word in words:
                # Try to translate each word
                if word in self.word_vectors:
                    vector = self.word_vectors[word]
                    translated_word = self._find_closest_english_word(vector)
                    translated_words.append(translated_word)
                else:
                    # If word is unknown, create new embedding
                    self.word_vectors[word] = np.random.randn(self.embedding_size)
                    translated_words.append(word)
            
            translation = ' '.join(translated_words)
            self.translation_memory[text] = translation
            return translation
            
        except:
            return text  # Return original text if translation fails
    
    def _tokenize(self, text):
        # Simple tokenization
        return re.findall(r'\w+', text.lower())
    
    def _find_closest_english_word(self, vector):
        best_similarity = -1
        best_word = None
        
        for word, vec in self.word_vectors.items():
            similarity = np.dot(vector, vec) / (np.linalg.norm(vector) * np.linalg.norm(vec))
            if similarity > best_similarity:
                best_similarity = similarity
                best_word = word
        
        return best_word if best_word else "unknown"
    
    def learn_translation(self, source_text, english_text):
        """Learn from parallel texts"""
        source_words = self._tokenize(source_text)
        english_words = self._tokenize(english_text)
        
        if len(source_words) == len(english_words):
            for s_word, e_word in zip(source_words, english_words):
                if s_word not in self.word_vectors:
                    self.word_vectors[s_word] = np.random.randn(self.embedding_size)
                if e_word not in self.word_vectors:
                    self.word_vectors[e_word] = np.random.randn(self.embedding_size)
                
                # Update vectors to be more similar
                self.word_vectors[s_word] = 0.9 * self.word_vectors[s_word] + 0.1 * self.word_vectors[e_word]
