from prolog_ast import Term, Predicate
from typing import Union

def unify(term1: Term, term2: Term, subst: dict) -> Union[dict, None]:
    """Unify two terms and return a substitution dict if successful, otherwise None."""
    if term1.is_variable:
        return unify_variable(term1, term2, subst)
    elif term2.is_variable:
        return unify_variable(term2, term1, subst)
    elif term1.value == term2.value:
        return subst
    else:
        return None


def unify_variable(var: Term, term: Term, subst: dict) -> Union[dict, None]:
    if var.value in subst:
        return unify(subst[var.value], term, subst) 
    elif term.is_variable and term.value in subst:
        return unify(var, subst[term.value], subst)
    else:
        """If the variable is not in the substitution, add new mapping."""
        subst = subst.copy()
        subst[var.value] = term
        return subst
    
def unify_predicates(p1: Predicate, p2: Predicate, subst: dict) -> Union[dict, None]:
    """Unify two predicates."""
    if p1.name != p2.name or len(p1.args) != len(p2.args):
        return None
    
    for t1, t2 in zip(p1.args, p2.args):
        subst = unify(t1, t2, subst)
        if subst is None:
            return None
    return subst