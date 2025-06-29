# xor

## XOR Encryption
XOR is useful in encryption because it has the following properties:
1. Commutative: A xor B = B xor A
2. Associative: A xor (B xor C) = (A xor B) xor C
3. Identity: A xor 0 = A
4. Self-inverse: A xor A = 0

We can use these properties to show that...

MSG = (MSG xor KEY) xor KEY

We can apply XOR encryption a first time to encrypt a message, and we can use the same algorithm a second time to decrypt a message.

To show this, we can run the following commands, from the root of this repository:\
% python keygen.py\
% python xor.py message.txt > cipher.txt\
% python xor.py cipher.txt > decrypted_message.txt

After running these commands, you will see that message.txt is equivalent to decrypted_message.txt.

We have explained why XOR is useful in encryption. There's one more thing I want to explain.

XOR encryption is relatively secure. If the key is randomly generated, and long enough in length (e.g. 1024 bytes in length or even 4096 bytes in length) then the encryption algorithm is fairly secure.

Suppose Alice has a mother named Barbara. Alice can figure out a secure way to send her mom a key file. Then her mom can use the key file to decrypt Barbara's encrypted messages. Only Alice and Barbara have the key file, and they can use it to send each other secure communications.

I think that... if you understand XOR encryption... then you have a really good grasp of encryption.

I had a lot of fun writing this repository. The repository demonstrates a secure encryption algorithm, and how it can be used to send secure communications.

I might add to this readme over time, but that's all for now.

The day is Saturday, June 28, 2025, and I'm already thinking about what I will eat for dinner and what TV shows I am going to watch. Perhaps I'll watch The Legend of Korra. I'm not sure what I will have for dinner.

Thanks for reading.

Addendum:
1. The encrypted message is often called the cipher or the ciphertext. That's why I name my file cipher.txt when I write the encrypted message to a file. This also explains the origin of the word "decipher".
2. XOR encryption is an example of symmetric key cryptography. RSA encryption, which we explore in a separate project, is an example of asymmetric key crytography, also called public key cryptography.
3. In XOR encryption we have only one key, and it's a private key. In RSA encryption, we have two keys, a public key and a private key.
