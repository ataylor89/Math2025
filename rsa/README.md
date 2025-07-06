# RSA encryption

## Usage
To test the encryption algorithm, you can type the following commands:

    # Generate a prime table of one million primes
    % python primetable.py 1000000

    # Generate a key table with 10 keys and a threshold of ten thousand
    % python keytable.py 10 10000

    # Generate a key pair
    % python keygen.py

    # Encrypt a message using our public key
    % python encrypt.py message.txt

    # Decrypt the cipher using our private key
    % python decrypt.py cipher.txt

## Security
In order to make the algorithm secure, we need to set a very high threshold for p and q.

Let n = p * q.

If we set a high enough threshold for p and q, then the product n will be very difficult to factor.

For example, if p and q are both greater than one trillion, the resulting n value might be difficult to factor.

It actually takes a lot of compute time, a lot of memory, a lot of disk space, and a lot of processing power to factor very large numbers, e.g. numbers greater than 10^100.

Practically speaking, it's hard to create a prime table that big. But we can create a really big prime table, and the bigger our prime table, the higher our threshold, the more secure our algorithm is.

## The cloud solution

Another thing we can do is this.

We can run primetable.py and keytable.py on AWS cloud, and generate a keytable with an extremely high threshold. Then we can download this keytable, run keygen.py, and create a key pair that is very secure.

Cloud computing is a really good solution to difficult computational problems.

AWS cloud is kind of like Netflix. We can easily turn on Netflix and start watching a TV show.

With AWS cloud, we can easily rent an EC2 instance, or a cluster of EC2 instances, and use them to run a program that requires a lot of CPU and memory.
