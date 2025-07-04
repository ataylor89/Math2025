# rot13

## What is a cipher?

My family taught me the meaning of the word "cipher".

The word "cipher" has at least two meanings.

A cipher can be an encrypted message (like the encrypted message contained in cipher.txt).

A cipher can also be an encryption algorithm (like the rot13 substitution cipher).

The word "cipher" can be a noun (e.g. ciphertext, rot13 substitution cipher).

The word "cipher" can also be a verb (e.g. cipher a message, decipher a code).

The words "message" and "cipher" are used often in the field of encryption. The word "cipher" can refer to the output of an encryption algorithm... it can also refer to the encryption algorithm itself.

## What is rot13?

rot13 is the name of an encryption algorithm. rot13 is the name of a cipher. Previously we established that the word "cipher" can mean "encryption algorithm", so I wanted to put it both ways.

rot13 means "rotate 13" or "rotate 13 places".

When encrypting a message, we rotate each alphabetic character 13 places in the alphabet.

If a character is non-alphabetic (e.g. a number, punctuation mark, etc) then it remains unchanged.

## The algorithm

An algorithm is a list of instructions.

The rot13 algorithm can be written down as a list of instructions.

Let's write down the algorithm.

    # rot13 algorithm

    # In steps 1 through 5 we define our variables and functions
    1. Let result = ""
    2. Let message be the message we want to encrypt or decrypt
    3. Let table be a map
    4. Let ord(x) be a function that returns the Unicode code point for a character x
    5. Let chr(x) be a function that returns the Unicode character for a code point x

    # In step 6 we generate a lookup table
    6. For i = 0, i < 26, i++
    6.1 Let j = (i + 13) mod 26
    6.2 Let letter = chr(ord('a') + i)
    6.3 Let substitution = chr(ord('a') + j)
    6.4 table[letter] = substutition
    6.5 Let letter = chr(ord('A') + i)
    6.6 Let substitution = chr(ord('A') + j)
    6.7 table[letter] = substitution

    # In step 7 we encrypt the message (or alternately we decrypt it, since rot13 is its own inverse)
    7. For each character in message
    7.1 Let substitution = ""
    7.2 If the character is alphabetic, then substitution = table[character]
    7.3 If the character is non-alphabetic, then substitution = character
    7.4 result += substitution 

    # We have finished encoding (or decoding) the message. Now we return the result
    8. return result

## Usage

Now that we have finished describing the algorithm, let's give some example uses.

\# First we encode the message contained within message.txt
% python rot13.py message.txt
uryyb jbeyq!
guvf vf naqerj
vg'f sevqnl, vg'f whyl 4, naq v'z cynaavat gb jngpu gi gbqnl

\# This time we write the cipher to a file
% python rot13.py message.txt > cipher.txt

\# Now we decode the cipher
% python rot13.py cipher.txt
hello world!
this is andrew
it's friday, it's july 4, and i'm planning to watch tv today
