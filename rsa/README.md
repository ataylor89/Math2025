# RSA encryption

## Usage
To test the encryption algorithm, you can type the following commands:

% python keygen.py message.txt\
% python encrypt.py message.txt publickey.txt\
% python decrypt.py cipher.txt privatekey.txt

If the second argument is omitted (the path to the key file) then the key will be read from the default location.

% python keygen.py message.txt\
% python encrypt.py message.txt\
% python decrypt.py cipher.txt
