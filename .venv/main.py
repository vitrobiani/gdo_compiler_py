import re
import sys
import random
from lexer import lexer
from parser import parser
from semantic_analyzer import SemanticAnalyzer
from interpreter import Interpreter

semantic_analyzer = SemanticAnalyzer()
interpreter = Interpreter()

command_history = []

def interpret_code(code):
    err = 0
    try:
        result = parser.parse(code, lexer=lexer)
        if result:
            interpreter.interpret(result)
    except Exception as e:
        err = 1
        print(f"Error: {e}")
    command_history.append((code,err))


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
        print("Line-By-Line Mode: (;!)")
        while True:
            try:
                if command_history[-1][1] == 0:
                    s = input('(^-^)>> ')
                elif command_history[-1][1] == 1:
                    s = input('(-_-)>> ')
            except EOFError:
                break
            except KeyboardInterrupt:
                print("See You Later Aligator! (^*^)")
                break
            except IndexError:
                s = input('(^u^)>> ')

            if not s:
                continue
            elif s == 'q' or s == 'Q' or s == 'quit' or s == 'Quit' or s == 'exit' or s == 'Exit' or s == ':wq' or s == ':q!' or s == ':q':
                print("See You Later Aligator! (^_^)")
                break
            elif re.fullmatch(r'r+', s):
                try:
                    for i in range(len(s)):
                        s = command_history.pop()[0]
                except Exception:
                    print("Not enough commands left.")
                    continue

            interpret_code(s)



if __name__ == '__main__':
    main()
