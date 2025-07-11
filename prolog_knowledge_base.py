from prolog_ast import Predicate, Fact, Rule

class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add(self, stmt):
        if isinstance(stmt, Fact):
            self.facts.append(stmt)
        elif isinstance(stmt, Rule):
            self.rules.append(stmt)
        else:
            raise ValueError("Unknown statement type")
        
    def get_candidates(self, goal: Predicate):
        candidates = []
        for fact in self.facts:
            if fact.head.name == goal.name and len(fact.head.args) == len(goal.args):
                candidates.append(fact)
        for rule in self.rules:
            if rule.head.name == goal.name and len(rule.head.args) == len(goal.args):
                candidates.append(rule)
        return candidates