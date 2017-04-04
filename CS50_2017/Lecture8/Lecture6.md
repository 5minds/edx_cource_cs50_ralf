# Lecture 6

## Problemset 6

1. Port some programs from C to Python.

2. Analyze some sentiments.

## Notes

### Mario(less comfortable)

1. Getting used to the new syntax of Python is fairly easy.
After understanding how the syntax is formatted, the code
was simply up to be translated.

2. Pretty much every function could remain as it is 
functionally. The only thing that has attention to be paid
to is the difference in how the print function sets newlines.

3. after adjusting the syntax the end of the file simply
needed the main function to be called. No compiling, just
running the programm the first time. Runs perfectly fine.

### Greedy(less comfortable)

1. Translating Greedy into Python was even faster after
getting a grip on the syntax, thee was nothing i had to pay
attention to in specific, everything worked nicely the first
try.

### Vigenere(less comfortable)

1. As opposed to the former 2, Vigenere was a bit more
complicated to translate into Python.

2. Strings in and on themselves are immutable, at least when
it comes to manipulating single chars. Then you can't just
add integers on chars or substract them from chars, that just
doesn't work here.

3. After changing every char array access to a new string
which is being constructed by appending, and reading every
integer value of a char with `ord` everything is working
perfectly fine.

### Sentiments

1. This problem is broken down into 3 sub-sets:
  * smile
  * tweets
  * application / piechart

2. In smile i need to take a set of words from a file and put
them into a data structure, one for positive and negative
expressions. I simply needed to initialize 2 lists, one for
positives and one for negatives (bound to `self.` so they are
usable in other parts of the code). Then i needed to open each
file and iterade throug each line, checking each line for an
alphabetical expression at the first char, stripping the
newline from it and appending it to the respective list.

3. Next up i needed to implement the `analyze`function. I
tokenized the text and iterated through each word in the
tokenized Text, then compared it with if it matched a word in
the former mentioned data struct and added or substracted 1 from
the score respectively.

3. For tweets, i got the tweets from `helpers.get_user_timeline()`
and handed the twitterhandle without "@" into the funciton as
parameter. If the function returned "None" i would exit the program

3. Then i analyzed each element within the object of `tweets` in order
to correctly interate through each one at a time.

4. I copied the colouring conditions and changed them to display the
score of each tweet, the message and the twitter handle. Done.

5. For the piechart i could simply import some necessary libaries and
copy the code from `tweets` with some minor changes. Every scored
tweet added +1 to each category: positive, negative or neutral. The
rest was handled by `helpers.py`

6. Though i had to research the tools i was using, the problemset did
not pose a real Problem. Everything worked quite easily after i put
some effort into understanding my tools.
Every asset of the problemset was solved accordingly and the code works
as required.