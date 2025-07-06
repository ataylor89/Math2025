# imagemagic

## What is algebra?

This repository contains a lot of linear algebra, so let's start with the question, "What is algebra?"

My family taught me that algebra means solving for an unknown.

Algebra is solving for an unknown.

There are many other good definitions of algebra.

Algebra is the field of mathematics concerned with solving equations and solving for unknowns.

Algebra is the art of solving equations.

You can see that there are many good definitions.

But algebra has a lot to do with two things in particular:
(1) Solving for an unknown
(2) Solving an equation

The unknown quantities are represented by variables. We give these variables names, like x, y, or z.

Arithmetic is really the field of math concerned with numbers and operations.

For example, 5 + (2 + 3)^3 is an arithmetic expression.

The arithmetic operations are addition, subtraction, multiplication, division, powers, and roots. We can also say that negation is an operation, but it's really a form of multiplication. (Since subtraction is a form of addition, and division is a form of multiplication, it makes sense to mention negation too. Negation is a unary operation whereas the other operations are binary operations.)

We start with the field of arithmetic, the study of numbers and operations.

When we introduce a variable, we arrive at the field of algebra.

5 + (2 + 3)^3 is an arithmetic expression.

5x + (2 + 3)^3 = 200 is an algebraic equation.

We can solve this equation for x, using the rules of algebra, also known as the laws of algebra.

We can simplify the expression 5 + (2 + 3)^3 using the rules of arithmetic.

We can simplify the expression ((x + 1/2) + isqrt(3)/2)((x + 1/2) - isqrt(3)/2) using the rules of complex arithmetic.

We can simplify the expression sqrt(-3) * sqrt(-3) using the rules of complex arithmetic.

We can solve the equation 5x + (2 + 3)^3 = 200 using the rules of algebra.

You might ask, are there rules of calculus? are there laws of calculus? The answer is yes, there are.

There are rules for differentiation, rules for integration. There is also l'Hopital's rule.

There is an algorithm for taking the definite integral of a function f(x) from a to b.

The definite integral of f(x) from a to b is F(b) - F(a), where F is any antiderivative of f(x), provided that f(x) is a continuous on [a, b]. (One condition for this theorem is that f(x) is continuous on [a, b]).

This theorem is called the fundamental theorem of calculus.

I'll repeat that, because it's important.

The fundamental theorem of calculus states that the definite integral of f(x) from a to b is F(b) - F(a), where F is any antiderivative of f, provided that f(x) is continuous on [a, b].

We can actually use our knowledge of differential calculus in order to use and apply the fundamental theorem of calculus.

For example, suppose we want to integrate cos(x) on the interval [0, π/2]. We know that the derivative of sin(x) is cos(x), so we can use sin(x) as our antiderivative.

Thus Integral_0^{π/2} cos(x) dx = sin(π/2) - sin(0) = 1 - 0 = 1.

We just used our knowledge of differential calculus, and the Fundamental Theorem of Calculus, to calculate the definite integral of cos(x) on the interval [0, π/2].

(When taking the definite integral of f(x) on [a, b], we can integrate f(x) directly if we know the rules for integrating f(x), but if we don't, we can work our way backwards, and find a function F(x) whose derivative is f(x), using trial and error, using the rules of differentation. In general, differentiation is easier than integration. We can use the definition of a derivative to calculate a derivative. We can use the concept of an antiderivative to integrate a function, since the definite integral is related to the antiderivative. The definition of a derivative is easier to work with than the Riemann sum definition of an integral... which is why the Fundamental Theorem of Calculus is so useful, since it allows us to use an antiderivative and apply our knowledge of derivatives.)

So listen...

We went off on a tangent.

We covered the rules of arithmetic (it's important to know the arithmetic operations -- addition, subtraction, multiplication, division, powers, roots, negation -- and also the order of operations... PEMDAS).

We covered the rules of complex arithmetic (we need these rules in order to calculate sqrt(-3) * sqrt(-3)).

We covered the rules of algebra (we need these rules in order to solve equations).

We covered the rules of calculus (differentiation, integration, the fundamental theorem of calculus, l'Hopital's rule).

It's worth mentioning the fundamental theorem of algebra... since we mentioned the fundamental theorem of calculus.

The fundamental theorem of algebra states that a polynomial of degree n has exactly n complex roots, and a polynomial equation of degree n has exactly n complex solutions, provided that n is a positive integer.

It's also important to know the rules of modular arithmetic. Modular arithmetic has many uses in encryption. For example, we use modular arithmetic whenever we write a rotation cipher, like rot13 or rot88.

Okay. Let's go back to the original question.

What is algebra?

Algebra is solving for an unknown.

There are many other branches of mathematics (like arithmetic, algebra, geometry, trigonometry, calculus, linear algebra, combinatorics, probability, number theory, et cetera).

Arithmetic is the study of numbers and operations.

Calculus is calculating a slope or an area.

Trigonometry is the study of triangles.

Combinatorics is the field of math concerned with counting.

I actually learned these definitions from my family.

My family taught me these definitions, and I thought I would share them.

Now, what is the definition of linear algebra?

We use so much linear algebra in this repository. What is the definition of linear algebra?

We will now proceed to answer this question, since we have enough background to begin studying this subject.

We will proceed to answer the questions:
1) What is the definition of linear algebra?
2) Do we really need linear algebra, and why do we have it in the first place?
3) What are some applications of linear algebra?
4) How do we use linear algebra in this repository?

## Mathematics is a language

I would like to take a moment to share an insight from my family.

My family taught me that mathematics is a language.

Numbers are part of this language.

Operations are part of this language.

Relations are part of this language.

There are all kinds of numbers, operations, and relations.

Consider numbers...

We know that there are positive numbers (1, 2, 3...)

We can count the number of trees in a garden using the natural numbers (0 and the positive integers). Then we can write down the number of trees in a garden, using the base ten system.

Without the base ten system, we have to resort to simpler systems.

For example, before the base ten system, there was the tally system.

If we visit a garden and count seventeen trees, we can write this down using the tally system.

||||| ||||| ||||| ||

We divided our tallies into three groups of five, and one group of two.

We can also use strikethrough notation, where we cross four tallies to signify the number five.

The tally system works if the garden contains a small number of trees.

But what if we visit a really big garden, or even a forest?

What if there are one hundred and seventeen trees in the garden?

What if there are one hundred and seventeen trees in the forest?

It takes a long time to write this number down using the tally system.

So we need a more convenient number system.

For this purpose, the base ten system was invented.

We can write down the number one hundred seventeen as 117 using the base ten system.

All it takes is three characters, three symbols.

Using three symbols, we can record a thousand different numbers... every number from 0 to 999.

With three tally marks, we can record every number from 0 to 3.

With three digits, we can record every number from 0 to 999.

If we want to record more, we can use the hexadecimal system.

With four digits, we can record 10,000 numbers, using the base ten system.

With four digits, we can record 65536 numbers, using the hexadecimal system.

The hexadecimal system is very useful for computers because binary data is stored as bits... literally it is stored in memory cells as "high voltage" or "low voltage", which is a binary value.

We can always represent 8 bits as two characters in hexadecimal.

But we cannot always represent 8 bits as two characters in decimal.

That's why hexadecimal is so useful in computing.

Listen, this is an aside, but it's an important aside.

We are talking about numbers. We are talking about integers.

We actually have all kinds of numbers -- positive numbers, negative numbers, zero, integers, fractions, real numbers, complex numbers.

We can use numbers to make measurements.

What is a measurement?

A measurement is a number accompanied by a unit of measurement.

For example, a football field is 100 yards long, and that's a measurement of length.

The temperature can reach 80 degrees Fahrenheit in the summer, and that's a measurement of temperature.

There are twenty four hours in a day, and that's a measurement of time.

In all of these examples, we are combining a number with a unit of measurement.

100 yards... the number is 100 and the unit of measurement is a yard.

80 degrees Fahrenheit... the number is 80 and the unit of measurement is one degree Fahrenheit.

24 hours... the number is 24 and the unit of measurement is one hour.

It's really useful to know numbers. It's really useful to know a number system.

When we have numbers, when we have a number system, we can make measurements.

A measurement is a number combined with a unit of measurement.

We can use the base ten system, or the decimal system, to make measurements.

We can measure the width of our living room in inches, the length of our living room in inches.

We can measure our height in inches.

We can record the number of trees in a garden in a diary, using the base ten system or the decimal system.

We can do all kinds of things with a number system.

You can see that... a number system really empowers us.

A number system empowers us to make measurements, and to think quantitatively.

We can measure a slope, an area, or a volume.

In calculus, there are all kinds of slope problems, area problems, volume problems.

We can measure a likelihood.

In the field of probability, we measure a likelihood.

(What is the unit of measurement when we measure a likelihood? Good question... I have to think about that.)

We also use numbers in computing.

Computer data is numeric.

Computers store data as numbers.

We call this binary data.

Computers really do store numbers as data, as a sequence of 1s and 0s, as a sequence of bits.

The reason for this is that... computers store data in memory cells, as a 1 or a 0, and a 1 represents a high voltage, and a 0 represents a low voltage.

Computers actually have to decode voltage levels, to determine the value of a memory cell.

Computers read the voltage levels in adjacent memory cells to form a binary number, a string of 1s and 0s.

That binary number can represent data.

For example, the number 0x61 = 97 represents the letter 'a' in Unicode.

When we store the letter 'a' in a text file, we store it as the number 0x61, or 97, and in binary this looks like 01100001.

In other words, we encode the letter 'a' as 01100001 in binary.

We need 8 memory cells to encode the letter 'a'.

If the byte order is big endian, then the first memory cell has a low voltage level, the next two memory cells have a high voltage level, the next four memory cells have a low voltage level, and the eighth memory cell has a high voltage level.

This is what the letter 'a' looks like in memory... 01100001.

Low voltage, high voltage, high voltage, low voltage, low voltage, low voltage, low voltage, high voltage.

LV, HV, HV, LV, LV, LV, LV, HV.

So we have talked about measurements. We have talked about numbers.

We have talked about why hexadecimal is useful.

My family taught me that using hexadecimal, we can always store 8 bits as 2 characters.

This is a property of hexadecimal that is not shared by decimal.

The decimal system is the system I learned at a young age.

For me, the decimal system is the most natural number system.

For me, the decimal system is the easiest number system.

(Honestly  it's subjective and everyone has different preferences.)

But the binary system and the hexadecimal are also very natural to me.

The three number systems that I use most often are decimal, hexadecimal, and binary.

I also use the tally number system (||||| | means 6 in tally) because it's cool.

Listen...

Numbers are part of the language of mathematics.

As soon as we define natural numbers, we discover that there are non-natural numbers.

What's a non-natural number?

Well, the solution to the equation 5 + x = 0 is not a natural number.

There is no natural number such that, when we add it to five, we get zero.

To represent this solution, we need negative numbers.

As soon as we define natural numbers, we realize that there are negative numbers.

Let's consider fractions.

The solution to the equation 3x = 2 is a fraction.

But the solution to the equation x^2 = 2 cannot be represented as a fraction.

We can actually prove that the solution to the equation x^2 = 2 cannot be represented as a fraction.

We can actually prove that the square root of two is not a fraction.

So as soon as we define fractions, we discover that there are non-fractions.

We call non-fractions by the name non-fractions or irrational numbers.

Then we consider every number on the number line.

We call these numbers real numbers.

We consider every number that can be written using the decimal system.

We call these numbers real numbers.

But then we come across the equation x^2 + x + 1 = 0, and we realize that the solutions to this equation cannot be represented by real numbers.

If we factor the equation x^2 + x + 1 = 0 into the form (x - r1)(x - r2) = 0, we realize that r1 and r2 cannot be represented as real numbers.

We find that the solutions are -1/2 + sqrt(-3)/2 and -1/2 - sqrt(-3)/2.

We cannot take the square root of negative three.

We cannot represent the square root of negative three as a real number.

So we define the imaginary number i, we invent the complex number system, we define the rules of complex arithmetic, and we represent sqrt(-3) as i * sqrt(3).

Now we can represent the solutions of x^2 + x + 1 = 0 as complex numbers.

As soon as we define real numbers, we realize that there are non-real numbers. We call non-real numbers by the name of complex numbers.

So you see, there are all kinds of numbers.

There are other types of numbers we have not even mentioned.

Is infinity a number? That's a really good question, and it's beyond the scope of this document.

Numbers are part of the language of mathematics, and there are many types of numbers.

Operations are also part of the language of mathematics.

The basic arithmetic operations are addition, subtraction, multiplication, division, powers, roots, and negation.

In modular arithmetic, we add a new operation, called the modulo operation.

In calculus, we add three new operations: limits, differentiation, and integration.

All of these operations have an operator associated with them.

For example, limits have the limit operator, differention has the derivative operator, and integration has the integral operator.

The modulo operation has the modulo operator.

Addition has the + operator. Subtraction has the - operator.

Multiplication has the * operator. Division has the / operator.

Powers has the ^ operator. Roots has the radical operator.

Negation has the - operator.

So in arithmetic we have the operations of addition, subtraction, multiplication, division, powers, roots, and negation.

In modular arithmetic we add the modulo operation.

In calculus we add the limit, derivative, and integral operations.

So far we have covered 11 operations: ASMDPRN, Modulo, Limit, Derivative, Integral.

Are there more? The answer is yes.

We also have the factorial operation, like 3! = 6. That's a total of twelve operations that we know of.

We also have two operations in combinatorics, nCr and nPr, which gives us a total of fourteen operations.

We also have many operations in linear algebra, including...
1) Matrix addition
2) Matrix subtraction
3) Scalar multiplication
4) Matrix multiplication
5) Determinant of a matrix
6) Inverse of a matrix
7) Transpose of a matrix

That gives us a total of twenty one operations.

I think I'll stop there... that's a lot of operations.

It's worth pointing out that we also have complex number operations (dividing complex numbers is quite interesting, and we use the conjugate operator to do this).

We also have set operations, like union, intersection, difference, and complement.

But what I'm getting at is this...

There are many types of numbers, and there are many types of operations.

Every operation is defined on a set of operands, and it produces a result.

The operands can also be called "inputs", and the result can also be called the "output".

So we know about numbers and operations.

We should also talk about relations.

Each relation is defined on a set of numbers.

We can define the equality relation on many sets of numbers, including, natural numbers, nonnatural numbers, fractions, non-fractions, real numbers, non-real numbers (complex numbers).

We can also define the equality relation on vectors and matrices.

We can define the greater than, greater than or equal to, less than, less than or equal to relations on many sets of numbers.

We can define the subset relation, the member of relation, and the equality relation, on sets.

What I'm getting at is...

Numbers, operations, and relations are all part of the language of mathematics.

In addition to numbers, we also have other objects like matrices.

A matrix is a rectangular array of numbers.

While it's not a number itself... it's composed of numbers.

A set is another kind of object that's not a number.

A set can be composed of numbers, but it can also be composed of books or countries or people.

We can generalize the concept of a number by calling something an object.

We can do operations with sets, because sets are mathematical objects.

When we take the union of the sets {'blue', 'green'} and {'red'}, we are doing a mathematical operation on sets. The sets are not numbers... but they are, more generally, mathematical objects.

So the concept of a mathematical object is more general than the concept of a number.

We can form relations between mathematical objects.

The set {'blue'} is equal to the set {'blue'}.

The set {'blue'} is a subset of the set {'red', 'green', 'blue'}.

These sets are not number per se, but they are mathematical objects.

So the word "object" has a place in mathematics.

Numbers, operations, relations, and objects, all have a place in the language of mathematics.
