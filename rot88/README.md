# rot88

## What is character encoding?

Character encoding is the process of turning characters (like the letter 'a') into code (like the number 0x61).

Literally, it means, turning characters into code.

Character decoding does the reverse... it turns code (like the number 0x61) into characters (like the letter 'a').

In order to make this clear, let's give an example using the interactive Python shell.

    % python

    # Encode my name as a list of Unicode code points, in decimal
    >>> list('andrew'.encode('utf-8'))
    [97, 110, 100, 114, 101, 119]

    # Encode my name as a list of Unicode code points, in hexadecimal
    >>> [hex(x) for x in 'andrew'.encode('utf-8')]
    ['0x61', '0x6e', '0x64', '0x72', '0x65', '0x77']

    # Encode my name as a string of Unicode code points, in hexadecimal
    >>> 'andrew'.encode('utf-8').hex()
    '616e64726577'
