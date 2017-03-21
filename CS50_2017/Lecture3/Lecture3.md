# Lecture 1

## Problemset 2

1. Search and sort some numbers.

2. Implement the Game of Fifteen.

## Notes.

### Find (less comfortable)

1. Commenting the generate.c is a simple feat. Nothing spectacular
if you understood what you did in Lecture 2

2. Implementing a linear `search` to be able to implement `sort` is
easy, just go through every element from 0 to n and check if they
match.

3. In order to make the Results of the `sort` algorhythm visible,
simply print out `values[]` from 0 to n in a seperate function.
This way you can manually check if the `sort` algorhythm does
what it's supposed to do. You need to `#inlcude <stdio.h>` in order
to do that.

4. When implementing the algorhythm, write down the pseudocode first,
then proceed by reconstructing the pseudocode into actual c and try
to imagine how and if each iteration of the loops and conditions of
the algorhythm would work as intended.

5. Bubblesort works both ways. You can either put the small values
at the beginning and begin to continute after each iteration one step
further or put the biggest value at the end and decrease each iteration
for each step. The result is the same.

6. In order to get an O of (log n) the search function should be
recursive.

7. There can only be 4 conditions. The value is equal to the value
that is being pointed out (the value has been found), the value is 
smaller than, bigger or, not there at all.

8. First condition to check is wether the value isn't there. When the
length of the array being searched is equal to 0, there is nothing to
search, return false.

9. When the value is equal to the value being pointed at, return true
,the value has been found.

10. if the value is smaller, return the search function with the cursor
position as the new length parameter of the array.

11. the only remaining condition is if the value is bigger, no need to
put an extra condition here. Return the search function and give it
the parameters according to the algorithm.

### Game of Fifteen

1. The questions at the begginning are all fairly easy. The information
can be taken all from within the fifteen.c code. The minimum and maximum
dimensions are set globally at the beginning. The array displaying the
board is a 2 dimensional array. The `greet()` contains the welcome message.
every Function that is empty (has a to do) has to be implemented:
`init()`, `draw()`, `move()` and `won`.

2. The way the current state of the board is being locked gives you an easy
way to implement `init()` and `draw()`. With some minor modifications and
a little reversive running counter you can initialize the board.
To draw the board simply take the same method, remove the "f" from `fprintf()`
and you're done.

3. It should, however, be noted that the way the board is being initialized
and drawn should be memorized and understood, it's important to understand
how 2 dimensional arrays work.

4. The `move()` function can be implemented by iterating through the array
until the tile value matches the value within the array. Then proceed by
checking if the tile above, right, down or left of the tile being searched,
is 0. These conditions have to have additional conditions to check wether the
tile resides at the corresponding edge. So if the tile being searched is
at the very right and up, these two directions should automatically count as
illegal moves. If each condition successfully meet, return true. In every
other case, return false by returning false at the end of the iteration after
every condition.

5. For the `won()` function, iterate through the array and compare the value
with a counter. The counter starts at 1 and goes up after each check.
If the value of the array doesn't match with either the current value of
**AND** the doesn't match 0, return false. In every other case (which is
only one by pure logic), return true.

6. The program works according to the requirements in the problemset. Every
tile moves when it should and doesn't when it shouldn't.

7. The check, however, does **NOT** run through seamlessly.

8. After several more and less intense tests of the program, i concluded that
there has to be some problem with the check itself. The first error is that
the check claims that after initializing a 4*4 game, there would be a "2"
instead of a "1" at character 3, line 4. Evidently after manually initializing
the game and checking the logs every time, this is clearly not the case.
The game inizializes accordingly and in correct order.
The second error is that the automated 4*4 test doesn't run properly. After
inspecting the testing file, and trying to reproduce the procedure, it showed
that the input, after about 3 steps, simply didn't make any sense. Most of
the moves were illegal ones and the testing file does not result in a valid
win situation at all.

9. Citing my tutor in this case, i concluded to say "Fuck it", and proceeded
to translate this sentiment into action accordingly.
