import re, sys, signal, time
from lexer import lexer
from parser import parser
from interpreter import Interpreter

exittime = 1
exit_symbol = ["quit", "exit", "q", "e", ":q", ":wq", ":q!", "c", "x"]
interpreter = Interpreter()
command_history = []


def interpret_code(code, add_to_command_history):
    err = 0
    try:
        result = parser.parse(code, lexer=lexer)
        if result:
            interpreter.interpret(result)
    except Exception as e:
        err = 1
        print(f"Error: {e}")

    if add_to_command_history:
        command_history.append((code, err))


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
        line_by_line()


def handler(signum, frame):
    print("You forced interrupted!"
          "\nGoodbye!")
    time.sleep(exittime)
    sys.exit(0)


def line_by_line():
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
        elif re.fullmatch(r'^q[1-8]$', s):
            match s:
                case 'q1':
                    from PartB import Q1
                    continue
                case 'q2':
                    from PartB import Q2
                    continue
                case 'q3':
                    from PartB import Q3
                    continue
                case 'q4':
                    from PartB import Q4
                    continue
                case 'q5':
                    from PartB import Q5
                    continue
                case 'q6':
                    from PartB import Q6
                    continue
                case 'q7':
                    from PartB import Q7
                    continue
                case 'q8':
                    from PartB import Q8
                    continue
                case _:
                    print("Something went wrong.")

        interpret_code(s, add_to_command_history)


if __name__ == '__main__':
    main()
