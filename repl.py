import sys
from prolog_parser import parse_program
from prolog_knowledge_base import KnowledgeBase
from prolog_evaluator import QueryEvaluator
from prolog_ast import Query, Term
from prolog_unification import resolve

def build_kb_from_file(path: str) -> KnowledgeBase:
    with open(path, "r") as f:
        text = f.read()
    stmts = parse_program(text)
    kb = KnowledgeBase()
    for stmt in stmts:
        if isinstance(stmt, Query):
            continue
        kb.add(stmt)
    return kb


def repl(kb: KnowledgeBase):
    
    evaluator = QueryEvaluator(kb)

    print("Welcome to the Prolog REPL! (type 'halt.' to exit)")
    while True:
        try:
            line = input("| ?- ").strip()
            if line == "halt.":
                print("Exiting REPL.")
                break
            line = "?- " + line

            stmts = parse_program(line)

            for stmt in stmts:
                if not isinstance(stmt, Query):
                    print("Only queries are allowed in REPL")
                    continue

                # for solution in evaluator.solve(stmt.goals, {}):
                #     bindings = [f"{var} = {val.value}" for var, val in solution.items()]
                #     print("".join(bindings) if bindings else "true")
                solutions = evaluator.solve(stmt.goals, {})
                try:
                    while True:
                        solution = next(solutions)
                        filtered = {
                            var : resolve(val, solution) for var, val in solution.items()
                            if var in stmt.variables
                        }
                        if not filtered:
                            print("true", end=" ")
                            continue

                        bindings = [f"{var} = {val.value}" for var, val in filtered.items()]
                        print("".join(bindings), end=" ")
                        if input() != ";":
                            break
                except StopIteration:
                    print("no")


        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python repl.py input.pl")
        sys.exit(1)

    file_path = sys.argv[1]
    kb = build_kb_from_file(file_path)
    repl(kb)