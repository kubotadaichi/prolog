from dataclasses import dataclass
from typing import List

@dataclass
class Term:
    value: str
    is_variable: bool

@dataclass
class Predicate:
    name: str
    args: List[Term]

@dataclass
class Fact:
    head: Predicate

@dataclass
class Rule:
    head: Predicate
    body: List[Predicate]

@dataclass
class Query:
    goals: List[Predicate]
    variables: List[str]