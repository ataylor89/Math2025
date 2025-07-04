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

## Examples

Let's get to know Unicode better through a few examples.

    % cat name.txt
    andrew

    % file -I name.txt
    name.txt: text/plain; charset=us-ascii

    % hexdump -C name.txt
    00000000  61 6e 64 72 65 77 0a                              |andrew.|
    00000007

In our first example, you can see that our file has an ASCII charset.

We can examine the contents of the file by doing a hexdump.

You can see that the file is actually a sequence of bytes, 61 6e 64 72 65 77 0a.

The 0a byte is code for "new line". Let's update the file so that it does not end with a new line.

    % python -c "print('andrew',end='')" > name.txt

    % file -I name.txt
    name.txt: text/plain; charset=us-ascii

    % hexdump -C name.txt
    00000000  61 6e 64 72 65 77                                 |andrew|
    00000006

You can see that the new file does not end with a new line.

The new file is a sequence of six bytes: 61 6e 64 72 65 77.

In order to read the file as plain text, we have to decode these bytes.. we have to decode the file.

Let's do that, quickly.

    >>> bytes.fromhex('61 6e 64 72 65 77').decode('utf-8')
    'andrew'

    >>> bytes([0x61, 0x6e, 0x64, 0x72, 0x65, 0x77]).decode('utf-8')
    'andrew'

Above, we take two approaches to decoding a file.

In the first approach, we represent a file as a hexadecimal string, and decode the string.

In the second approach, we represent a file as a list of bytes, and decode the sequence of bytes.

Whenever we read a file from our hard drive, and open it in a text editor, we have to decode the file behind-the-scenes...

The text editor does the decoding behind the scenes.

Even when we do file I/O, we have to decode a file.

Consider the following Python program.

    >>> file = open('name.txt', 'r')
    >>> text = file.read()
    >>> print(text)
    andrew

In this simple, three-line Python program, we open a file, decode the file as text, and print the text.

The line "text = file.read()" actually does all the decoding behind the scenes.

It uses the Unicode character decoding system to decode a file as text.

By default, the built-in open function uses Unicode as the decoding system. (It specifically uses UTF-8.)

We can actually specify the encoding when we open a file.

Let's do that.

    >>> file = open('name.txt', 'r', encoding='ascii')
    >>> file.read()
    'andrew'

    >>> file = open('pirsquared.txt', 'r', encoding='ascii')
    >>> file.read()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File ".../python3.11/encodings/ascii.py", line 26, in decode
        return codecs.ascii_decode(input, self.errors)[0]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xcf in position 4: ordinal not in range(128)
    
    >>> file = open('pirsquared.txt', 'r', encoding='utf-8')
    >>> file.read()
    'A = πr²\n'

In the above examples, you can see that we are able to decode name.txt as an ASCII file.

But we are not able to decode pirsquared.txt as an ASCII file, since it contains the character π.

We can, however, decode pirsquared.txt as a Unicode (UTF-8) file, since the Unicode charset includes π.

UTF-8 is one of three main Unicode formats. The other two are UTF-16 and UTF-32.

UTF-8 is the most common Unicode format.

In UTF-8, every character has a minimum width of 1 byte and a maximum width of 4 bytes.

UTF-8 is a variable-width encoding, since some characters are encoded using 1 byte, some are encoded using 2 bytes, some are encoded using 3 bytes, and some are encoded using 4 bytes.

In UTF-16, every character has a minimum width of 2 bytes and a maximum width of 4 bytes.

UTF-16 is also a variable-width encoding.

UTF-32 is a fixed-width encoding, since every character gets encoded as 4 bytes.

Let's see this in action.

    % file -I pirsquared.txt
    pirsquared.txt: text/plain; charset=utf-8

    % hexdump -C pirsquared.txt
    00000000  41 20 3d 20 cf 80 72 c2  b2 0a                    |A = ?.r².|
    0000000a

In the above file, you can see that A gets encoded as 0x41, space gets encoded as 0x20.

= gets encoded as 0x3d. π gets encoded as 0xcf80. π actually gets encoded as two bytes.

r gets encoded as 0x72. The superscript ² gets encoded as 0xc2b2.

The file ends with a new line, 0x0a.

You can see that... in the file pirsquared.txt... which has a utf-8 encoding... some characters are encoded using a single byte, and other characters are encoded using two bytes.

The reason for this is that... we simply cannot encode π using one byte.

We need two bytes to encode π.

UTF-8 files are shorter than UTF-32 files, since UTF-8 is more concise.

A UTF-32 file uses four bytes to encode every character.

A UTF-8 file uses the minimum number of bytes needed to encode every character.

We only need one byte to encode the character 'A', so a UTF-8 file encodes 'A' as 0x41.

But a UTF-32 file encodes the character 'A' as 0x41000000.

Let's see this in action.

    >>> file = open('pirsquared.utf32.txt', 'w', encoding='utf-32')
    >>> file.write('A = πr²')

    % hexdump -C pirsquared.utf32.txt
    00000000  ff fe 00 00 41 00 00 00  20 00 00 00 3d 00 00 00  |??..A... ...=...|
    00000010  20 00 00 00 c0 03 00 00  72 00 00 00 b2 00 00 00  | ...?...r...?...|
    00000020

The file starts with a byte order mark (BOM).

The byte order mark is ff fe 00 00. It indicates that the byte order is little endian.

After that, the character 'A' gets encoded as 41 00 00 00.

The space character gets encoded as 20 00 00 00.

The = character gets encoded as 3d 00 00 00.

The character π gets encoded as c0 03 00 00, because the byte order is little endian.

The letter r gets encoded as 72 00 00 00.

The superscript ² gets encoded as b2 00 00 00.

We can see that a UTF-32 file takes up more space than a UTF-8 file.

A UTF-32 file stores each character as four bytes.

A UTF-8 file stores each character as 1, 2, 3, or 4 bytes, depending on how many bytes are needed.

The letter A gets encoded as 0x41 in a UTF-8 file.

The letter A gets encoded as 0x41000000 in a UTF-32 file.

The most common Unicode format is UTF-8.

The default character encoding for MacOS files is UTF-8.

The default character encoding for HTML5 files is UTF-8.

In an HTML file, you can write <meta charset="utf-8">. It's not needed, since utf-8 is the default charset for HTML5. But you can still write it anyway, to show that you know about charsets.

In an HTML file, if you write <meta charset="ascii">, then your browser won't be able to render the character π.

Try writing an HTML file with the letter π in the body.

If you include <meta charset="ascii"> in the header, then your browser won't be able to render π, since it's not included in the ASCII charset.

If you include <meta charset="utf-8"> in the header, or you omit a meta/charset tag, then your browser should be able to render π just fine.

It's important to know that... π is both a character and a glyph.

A character is kind of like an abstract thing. A glyph is an image that represents a character.

π is a glyph... it's a picture that represents the Greek letter Pi.

π is also a character.

0x03c0 is the code point, in Unicode, that maps to π.

π is the character, in Unicode, that maps to the code point 0x03c0.

π is also a glyph (an image or a picture) that you see on your computer screen when you read this document.

Ultimately, the code point 0x03c0 gets rendered as a glyph, and the glyph is π.
