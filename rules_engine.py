from dataclasses import dataclass
import re
from typing import List, Dict, Tuple
import numpy as np

class Rule:
    def __init__(self, pattern, response, context_requirements=None):
        self.pattern = pattern
        self.response = response
        self.context_requirements = context_requirements or {}
        
    def __hash__(self):
        return hash((self.pattern, str(self.response), str(self.context_requirements)))
        
    def __eq__(self, other):
        if not isinstance(other, Rule):
            return False
        return (self.pattern == other.pattern and 
                self.response == other.response and 
                self.context_requirements == other.context_requirements)

class RulesEngine:
    def __init__(self):
        self.rules = []
        self._initialize_rules()
    
    def _initialize_rules(self):
        # Add your rules here
        self.rules.append(Rule(
            pattern=r"hello|hi|hey",
            response="Hello! How can I help you today?",
            context_requirements={"greeting": True}
        ))
        # ...existing code...

    def _evaluate_context(self, context):
        context_scores = {}
        for rule in self.rules:
            score = 0
            if context and rule.context_requirements:
                matches = sum(1 for k, v in rule.context_requirements.items() 
                            if k in context and context[k] == v)
                score = matches / len(rule.context_requirements) if rule.context_requirements else 0
            context_scores[rule] = score
        return context_scores

    def get_best_response(self, message, context=None):
        best_rule = None
        best_confidence = 0
        context_scores = self._evaluate_context(context)
        
        for rule in self.rules:
            # Pattern matching logic
            pattern_match = re.search(rule.pattern, message.lower())
            if pattern_match:
                confidence = 0.5 + 0.5 * context_scores.get(rule, 0)
                if confidence > best_confidence:
                    best_confidence = confidence
                    best_rule = rule
        
        if best_rule:
            return best_rule.response, best_confidence
        return "I'm not sure how to respond to that.", 0.0
