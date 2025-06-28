# Polynomials

## Modular design
This project adheres to the principle of modular design.
- The ComplexNumber class is in the complexnumbers module
- The Polynomial class is in the polynomials module
- The Quadratic class is in the quadratic module
- The Parser and ParseTree classes are in the parser module

I think that the principle of modular design can really help a developer organize their code.

We can test each module independently. It is also easier to read the code. 

(We know, for example, that the code for parsing is located in the parser module, and the code for solving a quadratic equation, and applying the quadratic formula, is located in the quadratic module.)

A Python module is just a file. So this project has four modules:
- complexnumbers.py
- polynomials.py
- quadratic.py
- parser.py

The principle of modular design is related to the divide-and-conquer strategy. We can divide a problem into many subproblems. This is what we do in this project. Parsing a quadratic equation is one subproblem. Solving a quadratic equation is another subproblem. We break down the problem into many subproblems, and solve each subproblem.
