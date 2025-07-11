from lark import Transformer
from prolog_ast import Term, Predicate, Fact, Rule, Query

class PrologTransformer(Transformer):
    def variable(self, items):
        return Term(value=str(items[0]), is_variable=True)
    
    def atom(self, items):
        return Term(value=str(items[0]), is_variable=False)
    
    def term_list(self, items):
        return items
    
    def predicate(self, items):
        name = str(items[0])
        args = items[1]
        return Predicate(name=name, args=args)
    
    def predicate_list(self, items):
        return items
    
    def fact(self, items):
        return Fact(head=items[0])
    
    def rule(self, items):
        head = items[0]
        body = items[1]
        return Rule(head=head, body=body)
    
    def query(self, items):
        goals = items[0]
        vars_in_query = set()
        def collect_vars(term):
            if isinstance(term, Term) and term.is_variable:
                vars_in_query.add(term.value)
        
        for predicate in goals:
            for arg in predicate.args:
                collect_vars(arg)

        return Query(goals=items[0], variables=list(vars_in_query))

    def statement(self, items):
        return items[0]
    
    def start(self, items):
        return items