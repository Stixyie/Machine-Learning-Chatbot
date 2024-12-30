import numpy as np
from collections import defaultdict

class NeuralNetwork:
    def __init__(self):
        self.input_layer_size = 1000
        self.hidden_layer_size = 500
        self.output_layer_size = 1000
        
        self.weights1 = np.random.randn(self.input_layer_size, self.hidden_layer_size)
        self.weights2 = np.random.randn(self.hidden_layer_size, self.output_layer_size)
        self.vocabulary = {}
        self.word_embeddings = {}
        
        self.learned_sentences = set()
        self.word_patterns = defaultdict(int)
        
        # Load initial training data
        self.load_training_data()
    
    def load_training_data(self):
        try:
            with open('training_data.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith('//'):  # Skip empty lines and comments
                        self.learned_sentences.add(line)
        except FileNotFoundError:
            print("Training data file not found. Starting with empty dataset.")
        except Exception as e:
            print(f"Error loading training data: {e}")
    
    def learn(self, text):
        # Tokenize and create word embeddings
        tokens = text.lower().split()
        for token in tokens:
            if token not in self.vocabulary:
                self.vocabulary[token] = len(self.vocabulary)
                self.word_embeddings[token] = np.random.randn(self.input_layer_size)
        
        # Update weights based on input
        input_vector = self.create_input_vector(tokens)
        self._backpropagate(input_vector, input_vector)
        
        # Store new sentence
        if text not in self.learned_sentences:
            self.learned_sentences.add(text)
            words = text.split()
            
            # Learn word patterns
            for i in range(len(words) - 1):
                self.word_patterns[(words[i], words[i+1])] += 1
            
            # Save to file
            self.save_learned_data(text)
    
    def save_learned_data(self, sentence):
        try:
            with open('learned_sentences.txt', 'a', encoding='utf-8') as file:
                file.write(f"{sentence}\n")
        except Exception as e:
            print(f"Error saving learned data: {e}")
    
    def generate_response(self, input_text, context):
        tokens = input_text.lower().split()
        input_vector = self.create_input_vector(tokens)
        
        # Forward propagation
        hidden = self._sigmoid(np.dot(input_vector, self.weights1))
        output = self._sigmoid(np.dot(hidden, self.weights2))
        
        # Convert output to text
        return self._vector_to_text(output)
    
    def create_input_vector(self, tokens):
        vector = np.zeros(self.input_layer_size)
        for token in tokens:
            if token in self.word_embeddings:
                vector += self.word_embeddings[token]
        return vector / max(len(tokens), 1)
    
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def _backpropagate(self, input_vector, target_vector):
        # Implementation of backpropagation algorithm
        hidden = self._sigmoid(np.dot(input_vector, self.weights1))
        output = self._sigmoid(np.dot(hidden, self.weights2))
        
        output_error = target_vector - output
        output_delta = output_error * self._sigmoid(output)
        
        hidden_error = np.dot(output_delta, self.weights2.T)
        hidden_delta = hidden_error * self._sigmoid(hidden)
        
        self.weights2 += np.outer(hidden, output_delta)
        self.weights1 += np.outer(input_vector, hidden_delta)
    
    def _vector_to_text(self, vector):
        # Convert output vector to text
        result = []
        for i in range(min(10, len(self.vocabulary))):
            max_sim = -1
            best_word = None
            for word, embed in self.word_embeddings.items():
                sim = np.dot(vector, embed) / (np.linalg.norm(vector) * np.linalg.norm(embed))
                if sim > max_sim:
                    max_sim = sim
                    best_word = word
            if best_word:
                result.append(best_word)
        return ' '.join(result)
    
    def generate_response(self, input_message, context):
        # Generate response based on learned patterns
        # This is a simplified version
        matching_sentences = [s for s in self.learned_sentences 
                            if any(word in s for word in input_message.split())]
        
        if matching_sentences:
            return np.random.choice(matching_sentences)
        return "I'm still learning about that."
