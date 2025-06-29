# xor

## XOR Encryption
XOR encryption is one of the easiest and most secure encryption algorithms. When the key is short, it's not secure. But if the key is as long as the message, and randomly generated, then it can be very secure.

In this repository, I choose a one-byte key, so the encryption algorithm is not secure. (That is, it can be easily cracked by brute force, since a hacker only has to try 256 possible keys to find the encryption key.)

In the xor2 repository, I choose a randomly generated key that is equal in size to the message. If the message is 300 characters, then the key is 300 characters. This means that the encrypted message has 256^300 possible keys. For a hacker to crack the code, they have to try out 256^300 possible keys, which is practically impossible for the average hacker. It's a lot different than trying out 256 possible keys. It is possible to crack a code when there are 256 possible keys. It is practically impossible to crack a code when there are 256^300 possible keys.

The xor2 repository offers a secure encryption algorith. I started out by writing the xor repository, and then I realized, the encryption algorithm is not secure. So I decided to write a secure encryption algorithm in the xor2 repsitory. My family recommended that I make the key as long as the message, so I decided to do that.

XOR encryption is at the heart of encryption. If you understand XOR encryption, then you understand encryption.

The XOR operator is commutative and associative. It has the properties A xor 0 = A and A xor A = 0.

It makes sense then that MSG xor KEY = ENC_MSG and ENC_MSG xor KEY = MSG, because...

(MSG xor KEY) xor KEY = MSG xor (KEY xor KEY) = MSG xor 0 = MSG

Since the XOR operator has these properties, it is well suited for use in encryption.

In other words, when we understand the properties of the XOR operator (commutative, associative, A xor A = 0 and A xor 0 = A), it makes sense that XOR is used in encryption.

We can say that 0 is the identity element in the set of integers under the XOR operation. We can say that 0 is the XOR identity.

We can also say that every element is its own inverse in the set of integers under the XOR operation. We can say that XOR has the self-inverse property.

We can summarize these properties as follows.

XOR Properties:
1. Commutativity: A xor B = B xor A
2. Associativity: A xor (B xor C) = (A xor B) xor C
3. Identity: A xor 0 = A
4. Self-inverse: A xor A = 0

This is kind of like a long-winded introduction to XOR encryption. But it contains a lot of useful information. The main points are as follows:

Main points
1. XOR is useful in encryption because of its properties (commutativity, associativity, identity, self-inverse)
2. XOR encryption is very secure when the key is randomly generated and the key is the same length as the message

In the xor repository, the key is one byte long. But in the xor2 repository, the key is randomly generated, and the key length is equal to the message length.
