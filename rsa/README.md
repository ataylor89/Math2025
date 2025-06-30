# RSA encryption

## Usage
To test the encryption algorithm, you can type the following commands:

% python keygen.py\
% python encrypt.py message.txt\
% python decrypt.py cipher.txt

## Security
In order to make the algorithm secure, we need to choose unfathomably large n values.

This is a difficult computation problem.

What we can do is this...

We can run keytable.py on AWS cloud, in a cluster, and set an extremely high threshold. This will result in extremely high n values. Then we can download the key table and use it to create key pairs.

When the n values are high enough (unfathomably high) it is very difficult to derive p and q from n.

If a hacker is unable to derive p and q values from n values, then they won't be able to decipher our ciphertext.
