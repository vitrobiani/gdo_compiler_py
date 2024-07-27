# The GDO Compiler
### **School project**
### by Gabi Levit, Dolev Telem and Omer Attia

- [x] Recieve Integers
- [ ] Recieve Booleans
- [ ] Perform all arithmatic operations (missing modolu)
- [ ] Perform Boolean operations (and, or, not)
- [X] Perform comparison operations (>, <, ==)

## Documentation
<details>

<summary>Declare a variable</summary>
To declare a variable use the equal sign '='.

exaple:
```
x = 5;
y = x*4;
```
</details>
<details>

<summary>Writing to the screen</summary>

### printing an int

After you declare a varible you can print it 
using the print function.
```
x = 5;
print x;
```

You could also use parentheses
```
x = 5;
print(x);
```
And do arithmatic operations:

```
x = 5;
y = x*4;
print(x+y);
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


