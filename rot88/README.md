# rot88

## What is character encoding?

Character encoding is the process of turning characters (like the letter 'a') into code (like the number 0x61).

Literally, it means, turning characters into code.

Character decoding does the reverse... it turns code (like the number 0x61) into characters (like the letter 'a').

In order to make this clear, let's give an example using the interactive Python shell.

    % python

    # Encode my name as a decimal list of Unicode code points
    >>> list('andrew'.encode('utf-8'))
    [97, 110, 100, 114, 101, 119]

    # Encode my name as a hexadecimal list of Unicode code points
    >>> [hex(x) for x in 'andrew'.encode('utf-8')]
    ['0x61', '0x6e', '0x64', '0x72', '0x65', '0x77']

    # Encode my name as a hexadecimal string of Unicode code points
    >>> 'andrew'.encode('utf-8').hex()
    '616e64726577'

## What is Unicode?

Unicode is the most popular character encoding system. It is also the most commonly used.

Before Unicode, there was ASCII.

ASCII is a 7-bit character encoding system. The ASCII charset contains 128 characters. Most of the characters that we type on an everyday basis are included in the ASCII charset. But there are some notable exceptions. 

The Greek letter π, which is commonly used in mathematics, is actually missing from the ASCII charset.

We need π in order to write mathematical equations. For example, the area of a circle of radius 1 is π. The area of a circle of radius 10 is 100π. The circumference of a circle of radius 1 is 2π.

It's important that we include π, and other Greek letters.

It's important that we include the Spanish letter ñ, which is used in the Spanish word año.

The Spanish letter ñ is included in Extended ASCII, but it is missing from the original ASCII charset.

The Greek letter π is not even included in Extended ASCII. It is out of range of the extended ASCII codespace.

The nice thing about Unicode is that it includes every character that we need.

The Unicode codespace consists of 0x110000 code points, or 1,114,112 code points, to write this number in decimal

The ASCII charset contains 128 characters...

The Extended ASCII charset contains 256 characters...

The Unicode charset contains 1,114,112 characters.

You can see that Unicode is a much bigger charset.

One virtue of Unicode is that the Unicode charset has every character we need.

A second virtue of Unicode is that it is consistent with ASCII.

The first 128 characters in Unicode are equivalent to the 128 characters in ASCII.

Unicode is consistent with ASCII, but it is not consistent with Extended ASCII.

We can say that ASCII is a subset of Unicode.

Extended ASCII, on the other hand, is not a subset of Unicode.

There are some other popular charsets, like ISO-8859-1 and Windows-1252.

ISO-8859-1 was the default charset in HTML4, but it was supplanted by Unicode in HTML5.

Windows-1252 is a character encoding system used in Microsoft Windows computers.

ISO-8859-1 and Windows-1252 are 8-bit encoding systems that consist of 256 characters.

ISO-8859-1 and Windows-1252 are consistent with ASCII, since the first 128 characters for each are equivalent to the 128 characters in ASCII.

We see that Unicode, ISO-8859-1, and Windows-1252 are all consistent with ASCII.

Of all the charsets we have mentioned, Unicode is by far the largest.

ISO-8859-1 and Windows-1252 contain 256 characters.

Unicode contains 1,114,112 characters.

Unicode is the universal coding system. It is used everywhere.

It is hard to think of a character that cannot be encoded with Unicode.

Mandarin can be encoded with Unicode.

Hebrew can be encoded with Unicode.

Arabic can be encoded with Unicode.

Unicode is the universal charset, the universal character encoding system.
