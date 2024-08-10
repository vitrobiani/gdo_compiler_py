import re,sys,signal,time
from pyreadline3 import Readline
from lexer import lexer
from parser import parser
from interpreter import Interpreter

exittime = 0
exit_symbol = ["quit", "exit", "q", "e", ":q", ":wq", ":q!", "c", "x"]
interpreter = Interpreter()
command_history = []

# Filling command history for easier use
command_history.append(("foo = lambda(a):{lambda(b):{a+b}};", 0))
command_history.append(("println((foo(5))(6));", 0))

def interpret_code(code, add_to_command_history):
    err = 0
    try:
        result = parser.parse(code, lexer=lexer)
        #print(result)
        if result:
            interpreter.interpret(result)
    except Exception as e:
        err = 1
        print(f"Error: {e}")

    if add_to_command_history:
        command_history.append((code,err))


def main():
    signal.signal(signal.SIGINT, handler)
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if filename.endswith('.lambda'):
            try:
                with open(filename, 'r') as file:
                    code = file.read()
                    interpret_code(code, 0)
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
        else:
            print("Please provide a file with a '.lambda' extension.")
    else:
        print("Line-By-Line Mode: (;!)")
        while True:
            add_to_command_history = 1
            try:
                if command_history[-1][1] == 0:
                    s = input('(^-^)>> ').strip()
                elif command_history[-1][1] == 1:
                    s = input('(-_-)>> ').strip()
            except IndexError:
                s = input('(^u^)>> ').strip()
            except Exception:
                print("Something went wrong.")
                break

            if not s:
                continue
            elif s.lower() in exit_symbol:
                print("See You Later Aligator!")
                time.sleep(exittime)
                break
            elif re.fullmatch(r'r+', s):
                add_to_command_history = 0
                try:
                    ch = [];
                    for i in range(len(s)):
                        ch.append(command_history.pop())
                    s = ch[-1][0]
                    print(s)
                    for i in range(len(ch)):
                        command_history.append(ch.pop())
                except Exception:
                    print("Not enough commands left.")
                    for i in range(len(ch)):
                        command_history.append(ch.pop())
                    continue

            interpret_code(s, add_to_command_history)


def handler(signum, frame):
    print("You forced interrupted!"
          "\nGoodbye!")
    time.sleep(exittime)
    sys.exit(0)

if __name__ == '__main__':
    main()
