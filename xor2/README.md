# xor2

## XOR Encryption
In the xor repository, I offered a long-winded introduction to XOR encryption.

Let's make this introduction short.

XOR is useful in encryption because it has the following properties:
1. Commutative: A xor B = B xor A
2. Associative: A xor (B xor C) = (A xor B) xor C
3. Identity: A xor 0 = A
4. Self-inverse: A xor A = 0

We can use these properties to show that...

MSG = (MSG xor KEY) xor KEY

We can apply XOR encryption a first time to encrypt a message, and we can use the same algorithm a second time to decrypt a message.

To show this, we can run the following commands, from the root of this repository:
% python keygen.py message.txt key.txt
% python message.txt key.txt > encrypted_message.txt
% python encrypted_message.txt key.txt > decrypted_message.txt

After running these commands, you will see that message.txt is equivalent to decrypted_message.txt.

We have explained why XOR is useful in encryption. There's one more thing I want to explain.

XOR encryption is actually very secure, when the key is randomly generated, and when the key is the same length as the message. The encryption algorithm contained in this repository is actually very secure.

Suppose Alice has a mother named Barbara. Alice can figure out a secure way to send her mom a key file. Then her mom can use the key file to decrypt Barbara's encrypted messages. Only Alice and Barbara have the key file, and they can use it to send each other secure communications.

I think that... if you understand XOR encryption... then you have a really good grasp of encryption.

I had a lot of fun writing the xor and xor2 repositories. The xor2 repository really demonstrates a secure encryption algorithm, and how it can be used to send secure communications.

I might add to these readmes over time, but that's all for now.

The day is Saturday, June 28, 2025, and I'm already thinking about what I will eat for dinner and what TV shows I am going to watch. Perhaps I'll watch The Legend of Korra. I'm not sure what I will have for dinner.

Thanks for reading.
