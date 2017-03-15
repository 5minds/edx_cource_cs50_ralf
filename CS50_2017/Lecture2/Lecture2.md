# Lecture 1

## Problemset 2

1. Infer a user’s initials from their name with initials.c.

2. Choose two adventures:

    * Implement Caesar’s cipher.

    * Implement Vigenère’s cipher.

    * Crack passwords.

## Notes.

### initials.c (less comfortable)

1. Writing some code in `main(void)`first, then abstracting it into
a function is a good and easy way to get working functions fast.

2. `isalpha()` from `<ctype.h>` opens up an easy option to check for
a valid input.

3. The code works accordingly to the requirements of the problemset.

### ceasar.c (less comfortable)

1. `main` can get starting parameters. 

2. You can transform `argv[1]` into an integer by using the `strol`function,
turning it into a long value, then converting it into an int.

3. The `sanityCheck` needs to have exception for a '-' in at the 0th place
in order to allow negative integers

4. The message that is going to be encrypted has to have exceptions for spaces

5. The only 2 difficult parts about caesar encryption are:

    * Checking if the encryption key's value is higher than 26 or lower than 0
    and increment / decrement it accordingly

    * Checking if the incrementation or decrementation of the key value exceeds
    the ascii range of the Alphabet (captial and non-capital letters)

### vigenere.c (less comfortable)

1. You can add up values from chars directly from a string array, but keep in mind
that you only want to add in proportion to the alphabet, not to the ascii table.

2. In case you want to convert the characters of `argv` to a simple to use value,
get the `strlen` before you do that. When you calculate `strlen` and it hit's a
value of nul / 0 , it automatically ends.

3. In order to get an easy to use value within the enycryptionKey, simply convert
each `char` `toupper` and substract 65 from it, that way the result is still acsii
but the exact values that are needed to correctly add up. pay attention to step 2
while doing that.

4. In order to "roll around" to the beginning of the encryption-key, simply use the
modulo of the length of the encryption-key after the counter within the pointer of
the array.

5. The encryption-key should have it's own counter when encrypting in order to
proceed with the key's pointer only when a value of the message has been encrypted
