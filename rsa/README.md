# RSA encryption

## Usage
To test the encryption algorithm, you can type the following commands:

% python keygen.py\
% python encrypt.py message.txt publickey.txt > cipher.txt\
% python decrypt.py cipher.txt privatekey.txt

## How secure is this algorithm?
If a hacker knows the public key, then they can actually bruteforce the private key, by trying every possible d value between 1 and n.

If the hacker does not know the public key, then it's less easy to crack.

## Challenges
I have tested this encryption algorithm a number of times. It works like 90% of the time. 10% of the time, the decrypted text is close to the original, but not exactly the original. I'm still investigating why this is.

## How can we make this algorithm more secure?
We are choosing small n values, which means that, if a hacker knows the public key, it is easy to bruteforce the private key, because they can try every possible d value between 1 and n.

In order to make this algorithm more secure, we can choose a much larger n value... a very large n value.
