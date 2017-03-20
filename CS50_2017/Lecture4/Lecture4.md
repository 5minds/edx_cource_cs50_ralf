# Lecture 1

## Problemset 2

1. Figure out whodunit.

2. Resize some images.

3. Recover some photos.

## Notes.

### Whodunit

1. The hardest part about this is understanding exactly how
a BMP works. When going through the questions, i simply needed
to follow the sources cited and the data within the project in
order to answer the questions.

2. As soon as the questions are answered, everything about the
task at hand should be clear (given that the questions were
answered with your own knowledge and not just google).

3. The implementation of `whodunit.c` is probably the the simplest
part. Just copy the entire code of `copy.c` and search for the
part where the `RGBTRIPLE` is being read and written. In between
that, just check if the the current triple's blue AND green value
are at the maximum and set them to zero. everythingthat is not
entirely red, will be red. then check if red is at the maximum for
that triplet aswell and set it to zero too. That way both red and
white (and by extension every hue of turquoise) will be entirely
black.

4. Then simply execute the program with the parameters:
`./whodunit clue.bmp verdict.bmp` , and you're done

5. The murderer is some Colonel with a culinary name, a horrible
taste of murdertool and an inappropriate choice of location.

### resize (less comfortable)

1. Just like "Whodunit", the exact understanding of a BMP is the
key to success here. Understanding each question is required to
have enough knowledge to solve this problem.

2. The links in the annotations within bmp.h should give enough
additional insight to understand everything.

3. Again, just like "Whodunit" a copy of "copy.c" is the best
foundation to solve this problem. It is even recommended to
do so in the Hints.

4. Before going to the task at hand, the start-check with `argc`
and `argv` have to be altered. Since you have 3 arguments, these
need to be patched a little.

4. After loading the Bitmapfileheader and Bitmapinfoheader from
the original file, biHeight, biWidth, padding, biSizeImage and
bfSize have to be altered with the multiplying factor before
being written into the output file.

5. Now comes the hardest part of the problem. Each pixel has to
be written into the output file multiple times (with the
multiplying factor from `argv[1]`) **AND** each complete scanline
has to be repeated the same multiple times.

6. Most important is to keep perfect track of where the cursor is
in the input file. Padding needs to be skipped after each full
set of multiple scanlines in the outputfile when going to the next
scanline in the input file. The padding in the outputfile, however,
has to be applied after each scanline being put into the outputfile.
Getting everything perfect is necessary, if the mulitplying factor,
the file-cursor or the padding are off just at one single place,
the entire output will be screwed up.

7. Every multiplying factor applies accordingly, the rescaling works
properly.

### recover

1. First issue that appeared was the datatype the buffer that would
be searched for JPG signatures would have. Char is a single byte in
size but lacks the capability to be compared with raw hexadecimal
values. I simply opted to `typedef` an unsigned integer of size 8
`uint8_t` as `BYTE` and used that as datatype for an array with 512
elements. With that set up i had a buffer i could easily inspect
byte by byte and compare the values with raw hexadecimal values.

2. I checked a few hundred chunks of data for JPG signatures until
i figured out the right pattern to search and used the resulting
search conditions to open a new JPG file.

3. To get get proper dynamic file naming, i made a formatted output
with `sprintf` and used the resulting variable in `fopen`.

4. In order to get every piece of data dynamically, regardless of
the size of the file that is being searched, I put `fread` in the
the `while` condition. `fread`returns the size of the elements
being searched, as long as it matches the buffer size, there is
more to be searched. As soon as the condition doesn't meet the
buffer size, the program siezes to search the file (since it
ended).

5. Before the first jpg file starts, there is some space with data
that can't be properly translated into pictures. To properly go past
this chunk of data, the initialization of `outptr` begins with a
file named `emptyspace` that is being deleted at the end of the
restoring proccess.

6. The code works accordingly and restores the deleted pictures
properly.

7. The code passes the `check50` check.
