from prolog_ast import Predicate, Fact, Rule

class KnowledgeBase:
    def __init__(self):
        self.statements: list[Fact | Rule] = []

    def add(self, stmt):
        if isinstance(stmt, Fact) or isinstance(stmt, Rule):
            self.statements.append(stmt)
        else:
            raise ValueError("Unknown statement type")
        
    def get_candidates(self, goal: Predicate):
        candidates = []
        for stmt in self.statements:
            if isinstance(stmt, Fact) and stmt.head.name == goal.name and len(stmt.head.args) == len(goal.args):
                candidates.append(stmt)
            elif isinstance(stmt, Rule) and stmt.head.name == goal.name and len(stmt.head.args) == len(goal.args):
                candidates.append(stmt)
        return candidates
    
    def __repr__(self):
        # return f"KnowledgeBase(statements={"\n".join(self.statements)})"
        statements_str = "\n".join(str(stmt) for stmt in self.statements)
        return f"KnowledgeBase(statements=[\n{statements_str}\n])"