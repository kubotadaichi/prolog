from pprint import pprint
from lark import Lark, Transformer
from prolog_transformer import PrologTransformer
from prolog_ast import Term, Predicate, Fact, Rule, Query
from prolog_knowledge_base import KnowledgeBase
from prolog_unification import unify, unify_predicates

def main():
    with open("prolog.lark", "r") as f:
        grammar = f.read()

    parser = Lark(grammar)

    program = """
parent(john, mary).
parent(mary, anne).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
?- ancestor(john, anne).
"""

    tree = parser.parse(program)
    # print(tree.pretty())
    transformer = PrologTransformer()
    ast = transformer.transform(tree)
    
    # pprint(ast)

    query = Predicate(name="parent", args=[
        Term(value="john", is_variable=False),
        Term(value="Y", is_variable=True)
    ])

    kb = KnowledgeBase()
    kb.add(Fact(head=Predicate(name="parent", args=[Term("john", False), Term("mary", False)])))
    kb.add(Fact(head=Predicate(name="parent", args=[Term("john", False), Term("bob", False)])))

    for stmt in kb.get_candidates(query):
        subst = unify_predicates(query, stmt.head, {})
        if subst:
            print(f"Success: {subst}")

if __name__ == "__main__":
    main()
