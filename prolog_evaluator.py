from typing import Iterator, Dict
from prolog_ast import Predicate, Rule, Fact, Query, Term
from prolog_knowledge_base import KnowledgeBase
from prolog_unification import unify_predicates

class QueryEvaluator:
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self.cut_triggered = False

    def solve(self, goals: list[Predicate], subst: Dict[str, Term]) -> Iterator[Dict[str, Term]]:
        if self.cut_triggered:
            # print("Cut triggered, stopping further solutions.")
            return

        if not goals:
            yield subst
            return 
        
        goal, *rest_goals = goals

        if goal.name == "!":
            # print("Cut encountered, stopping further solutions.")
            self.cut_triggered = True
            yield subst
            return 

        for stmt in self.kb.get_candidates(goal):
            if isinstance(stmt, Fact):
                new_subst = unify_predicates(goal, stmt.head, subst)
                if new_subst is not None:
                    yield from self.solve(rest_goals, new_subst)
            elif isinstance(stmt, Rule):
                renamed_rule = self._rename_variables(stmt)
                new_subst = unify_predicates(goal, renamed_rule.head, subst)
                if new_subst is not None:
                    new_gaols = renamed_rule.body + rest_goals
                    yield from self.solve(new_gaols, new_subst)

    def _rename_variables(self, rule: Rule) -> Rule:
        var_map = {}
        def rename_term(t: Term):
            if not t.is_variable:
                return t
            if t.value not in var_map:
                var_map[t.value] = Term(f"{t.value}_{id(t)}", True)
            return var_map[t.value]
        
        new_head = Predicate(rule.head.name, [rename_term(t) for t in rule.head.args])
        new_body = [Predicate(p.name, [rename_term(t) for t in p.args]) for p in rule.body]
        return Rule(new_head, new_body)