from lark import Lark, Transformer
from prolog_ast import *
from prolog_transformer import PrologTransformer

with open("prolog.lark", "r") as f:
        GRAMMAR = f.read()

def parse_program(text: str):
        parser = Lark(GRAMMAR, start="start")
        tree = parser.parse(text)
        return PrologTransformer().transform(tree)