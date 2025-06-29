# RSA encryption

## Usage
To test the encryption algorithm, you can type the following commands:

% python keygen.py message.txt\
% python encrypt.py message.txt publickey.txt\
% python decrypt.py cipher.txt privatekey.txt

You can also omit the key files, in which case they will be read from the default locations.

% python keygen.py message.txt\
% python encrypt.py message.txt\
% python decrypt.py cipher.txt
