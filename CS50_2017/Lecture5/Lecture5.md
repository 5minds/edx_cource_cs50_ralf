# Lecture 5

## Problemset 5

1. Answer some questions about a spell checker.

2. Implement a spell checker.

## Notes.

### speller

1. First thing is to answer the questions, nothing too complicated.

2. The second task is to implement the functions `check`, `load`,
`size` and `unload`

3. In load i need to load the dictionary into a datastructure. This
is where things get a little more complicated.

4. In order to get a good loading time and checking time i need to
get a most dynamic data structure. But with fast running data
structures comes complexity.

5. My current attempts to store everything in a sort of `next` and
`child` structure, where the `next` char is either some other
possiblity for a letter that might occur after the one that came
before and the `child` char is a letter that comes afterward for
a word is running up against a wall very fast. I can't stitch
the structure together very efficiently.

6. I might go for a Hash table but that would merely divide the
running time by 26, and this is not ultimatly what i might want to
go for.

7. So i went for the Trie structure and it gave me a hard time in
return. I had several fresh approaches to the insertion of the
dictionary into the structure. But it soon dawned on me that the
whole structure, in order to be working correctly, was much more
complex to integrate than i anticipated.

8. My best attempt failed at the point where the temporary pointer
`currentNode` should return from the scope of 2 functions back to
the main function `load`. The node had the pointer to `newNode`
inside the `insert` function, but the pointer of `currentNode`
did not seem to act appropriatly within the scope depth of 2
functions. Thus, `newNode` and the `child` of `currentNode`never
truly connected via pointer and the values were never stored 
"permanently".

9. I tried several times in new attempts to recreate a similar
approch which all failed. Even after inquiring the help of a
much more experienced peer, me and him couldn't figure out a
working approach.

10. The Problemset will be delayed.