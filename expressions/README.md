# Evaluating expressions

## Usage

To run the program, you type "python eval.py \<file\>" in the command-line, where \<file\> is the path to a file containing an arithmetic expression.

Here are some examples.

% cat expr/1.txt\
1 + (2 + 3) * 4 + ((1 + 2) * 3)

% python eval.py expr/1.txt\
30

% cat expr/2.txt            
5 + 2^3 - 3 + 2*7

% python eval.py expr/2.txt\
24
