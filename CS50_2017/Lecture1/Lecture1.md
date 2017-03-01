# Lecture 1

## Problemset 1

1. Say hello to the world with hello.c.

2. Calculate your water consumption with water.c.

3. Recreate one of Mario’s pyramids, in mario.c.

4. Provide a user with either cash or credit in greedy.c or credit.c.

## Notes.

1. I am using the online CS50 ide in order to write the code for the
Problemset

### Hello.c

1. In order to use `printf` i need to `#include <stdio.h>`

2. The code works accordingly to the requirements of the problemset.

### Water.c

1. In order to use `get_int` i need to `#include <cs50.h>`

2. The code works accordingly to the requirements of the problemset.

### Mario.c (less comfortable)

1. The mario's pyramide problem was solved by creating 3 functions,
additional to `main`. One of them get's called within main. This
function calls 2 other functions that print out the spaces and 
hashes respectively to the time the loop has been called. After that,
a simple break is printed.

2. The code works accordingly to the requirements of the problemset.

3. The code passes the `check50` check.

### Greedy.c (less comfortable)

1. The greedy problem was solved by a function that checked if the entered
float value is smaller than the compare values (0.25 , 0.10 , 0.05 and 0.01).
After the function was called, a counter increased by one.
The value was then decreased by the compare value.
This function ran until the calculated value hit 0.

After this, the result of the counter value was printed.

2. This particular problem was peculiarily odd because the float values did not
behave as expected. After a few caluclations with certain values, the value
itself seemed to be precise, but in reality wasn't. After a closer look into the
issue, the value showed to be slightly less than the calulated value. So slight
infact that the difference to the expected value didn't even show up after
checking it 10 after the comma.

3. The problem has been worked around by simply comparing the value with another
compare value that was 0.001 smaller than the actual compare value.

4. The code works accordingly to the requirements of the problemset.

5. The code passes the `check50` check.

6. The problem has been solved but the workaround doesn't really seem appropriate.
There has to be a different approach to this.

7. I multiplied the value `change` i request at the beginning of the programm by
100 and convert it another value `cents` of the integer type. After that i rework
the function that calculates the number of coins used so that the compare values
match accordingly.

8. At this point the programm works, except for one input, which is `4.2`.

9. The float `4.2` and its multiplied version 420 are not actually exactly 420.
The actual float value of `4,2` is lower and this is only viewable after a few
digits behind the comma (for those who want to know, it's :`4.199999809265137`.
This number will ultimatly interpreted as 419 when used. In order to achieve the
actual round value, the calculation of `change*100` will be rounded. Since
I multiplied with 100 when rounding, I will still have the accurate value I
want (at least for the purposes the program needs to serve).
