# RSA encryption

## Usage
To test the encryption algorithm, you can type the following commands:

% python keygen.py\
% python encrypt.py message.txt publickey.txt > cipher.txt\
% python decrypt.py cipher.txt privatekey.txt

## The problem
The problem with this repository is that the encryption algorithm is very easy to crack. You can just bruteforce the d value if you already know the n value.

The xor2 repository has a secure encryption algorithm... but this repository does not.
