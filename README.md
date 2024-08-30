# Prodigy_CS_01
# Task-01
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption

# Ceaser Cipher
The Caesar cipher is a classic example of ancient cryptography that involves shifting each letter of a plaintext message by a certain number of letters, historically three. It is a type of substitution cipher where one letter is substituted for another in a consistent fashion. The earliest known use of a substitution cipher, and the simplest, was by Julius Caesar. The Caesar cipher involves replacing each letter of the alphabet with the letter standing three places further down the alphabet.

For example,

plain: meet me after the toga party

cipher: PHHW PH DIWHU WKH WRJD SDUWB

Note that the alphabet is wrapped around, so that the letter following Z is A. We can define the transformation by listing all possibilities, as follows:

plain: a b c d e f g h i j k l m n o p q r s t u v w x y z

cipher: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

The algorithm can be expressed as follows. For each plaintext letter p, substitute the ciphertext letter C:

We define a mod n to be the remainder when a is divided by n. For example, 11 mod 7 = 4.

C= E(3, p) = (p+ 3) mod 26

Description In this task, I created a Python program that performs the following functions:

Encrypts a given message using the Caesar Cipher algorithm by giving user input. Decrypts an encrypted message using the same algorithm by giving user input. Allows users to input a message and a shift value to perform the encryption and decryption. Example Do you want to (e)Encrypt or (d)Decrypt the message? Enter 'e' or 'd': e

Enter the message: hello

Enter the shift value: 22

The resulting message is: dahhk

Do you want to perform another operation? (yes/no): yes

Do you want to (e)Encrypt or (d)Decrypt the message? Enter 'e' or 'd': d

Enter the message: dahhk

Enter the shift value: 22

The resulting message is: hello

Do you want to perform another operation? (yes/no): no

How it works: 1.Encryption (caesar_cipher_encrypt):

Iterate through each character in the input text. If the character is a letter, calculate its shifted position based on the ASCII value, wrap around using modulo operation, and convert it back to a character. If the character is not a letter, leave it unchanged. 2.Decryption (caesar_cipher_decrypt):

Decryption is done by calling the encryption function with the negative of the shift value. 3.Main function (main):

Prompt the user to choose between encryption and decryption. Ask for the message and shift value. Perform the selected operation and display the result. Allow the user to perform multiple operations until they decide to exit.

Repository Contents
PRODIGY_CS_01.py : The main Python script containing the implementation of the Caesar Cipher. README.md : This file, providing an overview of the task and the project.
