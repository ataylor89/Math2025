# Evaluating expressions

## Usage

To run the program, you type "python eval.py \<file\>" in the command-line, where \<file\> is the path to a file containing an arithmetic expression.

Here are some examples.

    % cat expr/1.txt
    1 + (2 + 3) * 4 + ((1 + 2) * 3)
    % python eval.py expr/1.txt
    30

    % cat expr/2.txt            
    5 + 2^3 - 3 + 2*7
    % python eval.py expr/2.txt
    24

    % cat expr/3.txt
    5+(2+3)^3
    % python eval.py expr/3.txt
    130

    % cat expr/4.txt
    2-3+5
    % python eval.py expr/4.txt
    4

    % cat expr/5.txt
    100^(1/2)
    % python eval.py expr/5.txt
    10

    % cat expr/6.txt
    -1 * 2 + -3 + 5
    % python eval.py expr/6.txt
    0
