# The GDO Compiler
### **School project**
### by Gabi Levit, Dolev Telem and Omer Attia

TODO Compiler:
- [x] Recieve Integers
- [X] Recieve Booleans
- [X] Perform all arithmatic operations
- [X] Perform Boolean operations (and, or, not)
- [X] Perform comparison operations (>, <, ==. >=, <=)
- [X] Named functions
- [X] Basic lambda expressions
- [ ] advanced lambda expressions (her example and lambda expressions that can be given to functions as args)
- [X] Function application (function calling)
- [X] Recursion 
- [X] Interpreter mode like python
- [X] Files need to end in .lambda
- [ ] Type errors
- [ ] Comprehensive errors (line numbers)
- [X] (optional) Comments
- [ ] Function return nothing not working properly
- [X] Fix the redo problem
- [X] fix forced interruption
- [ ] 
- [ ] 


TODO Part B:
- [ ] Question 1 (Q1)
- [ ] Question 2 (Q2)
- [ ] Question 3 (Q3)
- [ ] Question 4 (Q4)
- [ ] Question 5 (Q5)

***

## Documentation
<details>

<summary>Declare a variable</summary>
To declare a variable use the equal sign '='.

## declare an int
exaple:
```
x = 5;
y = x*4;
```
## declare a boolean
exaple:
```
x = True;
y = False;
```
</details>
<details>

<summary>Writing to the screen</summary>

### Printing an int

After you declare a varible you can print it 
using the print function.
```
x = 5;
print(x);
```
output:
```
5
```
And do arithmatic operations:

```
x = 5;
y = x*4;
print(x+y);
```
output:
```
25
```
### Printing a Boolean 
You could put a boolean expression in the print function like so:
```
x = 5;
y = x*4;
print(x == y);
```
output:
```
False
```
</details>
<details>

<summary>Function declaration and calling</summary>
to declare a function you need to use the keyword 'zap', and to call on it write its name with the correct arguments.

exaple:
```
zap addNums(a,b){
    return a+b;
}
print(addNums(5,4);
```
output:
```
9
```
You could also preform recursion:
```
zap fib(n) {
    if (n == 0) { return 0; }
    if (n == 1) { return 1; }
    return addNums(fib(n - 1), fib(n - 2));
}
print(fib(6));
```
output:
```
8
```
You can take the output of a function and put it into a variable like so:
```
zap fib(n) {
    if (n == 0) { return 0; }
    if (n == 1) { return 1; }
    return addNums(fib(n - 1), fib(n - 2));
}
x = fib(6);
print(x);
```
output:
```
8
```
</details>
<details>

<summary>If statements</summary>

You could perform if, elseif and else functions using: <br />
greater then (>), <br />
greater equal (>=),  <br />
lesser then (<), <br />
lesser equal (<=),  <br />
equals (==),  <br />
not equal (!=)  <br />
like so:

```
x = 10;
if(x != 10){
  print(True);
} elseif (x <= 15) {
  print(False);
} else {
  print(x);
}
```
output:
```
False
```
You can also use the and (&&), or (||) , not (!) signs
```
x = 10;
y = x * 2;
if(x != 10 || y == 20){
  print(True);
} elseif (x <= 15) {
  print(False);
} else {
  print(x);
}
```
output:
```
True
```
And you could put True or False straight in there:
```
x = 10;
if(True){
  print(x);
} 
```
output:
```
10
```

</details>
<details>

<summary>Line by line interpreter Mode</summary>

When activating the interpreter without any arguments (i.e no files)
you enter line-by-line mode. <br />
in this mode you can run commands like the bash or python terminal. <br />
SIM LEV: semicolons are still required! <br />

To activate this mode you either need to compile the main code file lambda.py<b />
or if you are on windows you can run the executable.

### Running the executable (windows only!)
You can run the lambda.exe file or just double click like any other app.

```commandline
.\lambda.exe
```

### compiling the main file
To compile the main file lambda.py you call the python interpreter.<b />
If you are in the compiler directory run:
```commandline
python lambda.py
```

if you are in another directory you will need to know the path to the compiler directory and run:<b />
```commandline
python ./path/to/compiler/lambda.py
```
or for windows:
```commandline
python .\path\to\compiler\lambda.py
```
> Windows uses backslash as opposed unix based systems that use forward slash 

### Interpreter details
You will be greeted with this prompt:
```
Line-By-Line Mode: (;!)
(^u^)>> 
```
From here you can write code freely.
if your last command was errored out the interpreter won't like it:
```
Line-By-Line Mode: (;!)
(^u^)>> a = ;
Error: Blank space where it shoudn't be
(-_-)>> 
```
and happy if it passed:
```
Line-By-Line Mode: (;!)
(^u^)>> a = ;
Error: Blank space where it shoudn't be
(-_-)>> a = 5;
(^-^)>> 
```
you can use the r expression to redo a command, <br />
you could put several r's to redo srveral commands back
```
Line-By-Line Mode: (;!)
(^u^)>> x = 5;
(^-^)>> y = 6;
(^-^)>> z = 7;
(^-^)>> print(x);
5
(^-^)>> print(y);
6
(^-^)>> print(z);
7
(^-^)>> r
7
(^-^)>> rr
6
(^-^)>> rrr
5
```

And to close the application you can simply press what ever you know that closes application, <br />
as it would most likely work here too!. <br/>
>q, Q, quit, Quit, exit, Exit, :wq, :q, :q! <br/>

all this will get you out.

```
Line-By-Line Mode: (;!)
(^u^)>> q
See You Later Aligator! (^_^)
```


</details>
<details>

<summary>Compiling a code file</summary>

To compile a file with code in it you first need to make sure that the file ends in .lambda <b />
as the compiler won't accept any other suffix.
The code must either be in the file of the compiler, <b />
or you could run the compiler by referencing its exact location. <b />
If you're on windows there is the option of activating the executable file with the code file. <b />

> you could add the compiler directory to your system PATH but we won't do any of that

### Running the executable (windows only!)
You can run the lambda.exe file or just double click like any other app.
```commandline
.\lambda.exe
```

### Code file in the compiler
```commandline
python lambda.py code.lambda
```
This is the easiest way as the code file is in the same directory as the compiler main file and so <b />
you could run the python interpreter on the main file lambda.py giving it the code file (marked code.lambda)<b />
as an argument.

### Code file outside the compiler directory
```commandline
python ./path/to/compiler/lambda.py ./path/to/code/code.lambda
```
or for windows:
```commandline
python .\path\to\compiler\lambda.py .\path\to\code\code.lambda
```
> Windows uses backslash as opposed unix based systems that use forward slash 

As you can see it is possible to compile code anywhere in your system as long as you have the path the compiler.


</details>

***
## BNF Grammer
