import sys
import random

from lexer import lexer
from parser import parser
from semantic_analyzer import SemanticAnalyzer
from interpreter import Interpreter

semantic_analyzer = SemanticAnalyzer()
interpreter = Interpreter()


def interpret_code(code):
    result = parser.parse(code, lexer=lexer)
    if result:
        try:
            interpreter.interpret(result)
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if filename.endswith('.gdo'):
            try:
                with open(filename, 'r') as file:
                    code = file.read()
                    interpret_code(code)
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
        else:
            print("Please provide a file with a '.gdo' extension.")
    else:
        print("interpret this UwU;(!)")
        while True:
            try:
                rand = random.randint(0, 100)
                if rand > 90:
                    s = input('(^_^)>> ')
                elif rand > 60:
                    s = input('(^-^)>> ')
                elif rand > 30:
                    s = input('(^+^)>> ')
                else:
                    s = input('(-_-)>> ')
            except EOFError:
                break
            if not s:
                continue
            elif s == 'q' or s == 'Q' or s == 'quit' or s == 'exit':
                print("See You Later Aligator! (^*^)")
                break
            interpret_code(s)



if __name__ == '__main__':
    main()
