# The GDO Compiler
### **School project**
### by Gabi Levit, Dolev Telem and Omer Attia

TODO Compiler:
- [x] Recieve Integers
- [X] Recieve Booleans
- [X] Perform all arithmatic operations
- [X] Perform Boolean operations (and, or, not)
- [X] Perform comparison operations (>, <, ==)
- [X] Named functions
- [ ] Lambda expressions
- [ ] Function application??
- [X] Recursion (tested only with fib function)
- [X] Interpreter mode like python
- [ ] Files need to end in .lambda (.gdo at the moment)
- [ ] Type errors
- [ ] Comprehensive errors (line numbers, place in line etc)
- [X] (optional) Comments

TODO Part B:
- [ ] Question 1 (Q1)
- [ ] Question 2 (Q2)
- [ ] Question 3 (Q3)
- [ ] Question 4 (Q4)
- [ ] Question 5 (Q5)


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
You could also predorm recursion:
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
You could perform if, elseif and else functions using the greater then (>), greater equal (>=), lesser then (<), lesser equal (<=), equals (==) and not equal (!=) like so:

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

<summary></summary>

exaple:
```
```
</details>


## BNF Grammer
```
S' -> program
program -> statement_list
statement_list -> statement
statement_list -> statement_list statement
statement -> assign_statement
statement -> print_statement
statement -> if_statement
statement -> if_else_statement
statement -> function_definition
statement -> return_statement
statement -> expr SEMI
assign_statement -> ID ASSIGN expr SEMI
print_statement -> PRINT expr SEMICOLON
if_statement -> IF expr LBRACE statement_list RBRACE
if_else_statement -> IF expr LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
function_definition -> ZAP ID LPAREN param_list RPAREN LBRACE statement_list RBRACE
param_list -> ID
param_list -> param_list COMMA ID
param_list -> empty
return_statement -> RETURN expr SEMI
expr -> expr PLUS expr
expr -> expr MINUS expr
expr -> expr TIMES expr
expr -> expr DIVIDE expr
expr -> expr EQ expr
expr -> expr NE expr
expr -> expr LT expr
expr -> expr LE expr
expr -> expr GT expr
expr -> expr GE expr
expr -> MINUS expr
expr -> LPAREN expr RPAREN
expr -> NUMBER
expr -> ID
expr -> ID LPAREN arg_list RPAREN
arg_list -> expr
arg_list -> arg_list COMMA expr
arg_list -> empty
empty -> <empty>
```


