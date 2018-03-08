# Lecture 10

## Problemset 8

1. Implement a website that lets users search for articles atop a map, a la the below.

## Notes

### mashup.db

1. arguably the simplest part, mashup.db had to get a table
with certain fields. The corresponding value types had to be
derived from the content in US.txt (or DE.txt in my case).
Afterwards the table simply had to be filled with the imports
from the .txt file.

### application.py

1. First in application.py the route `/articles` had to be
implemented. It should simply take an input string and return
a json body from it's source. Easy said, easy done, simply
put the the value of `geo` with `request.args.get()` in a.
Check if the contents of the string are empty, raise a 
runtime error if so. `lookup()` the contents of geo and save
the content in another variable. Pay attention that you want
to get the first 5 entries, not all of them (`[0:5`).
At last return the jsonified version of the lookup results.
Note that you have to return the [0]th entry since the result
of `lookup()` is a a layer onion-i-fied (as i like to call it).

2. Second in application.py is the `/search` route. Just as in
`/articles`, get the value fom `q` with `request.args.get()` and
store it in a variable. Again, check for content. The interesting
part is the query, where you have to `SELECT everything (*) from
your table `WHERE` the postal code, place name `OR` "admin_name1"
have to match the stored variable `q`. Store the value in another
variable and return the [0]th entry of the jsonified version.

### scripts.js

1. `configure` of scripts.js is the most obvious an easy one.
Just replace TODO with literally what the specification tells you
to do.

2. `addMarker` is the most complex, but not really hard on it's
own. The function's one and ONLY argument contains everything you
need. Infact it contains every value within each respective entry
of your database table `places`. First of all, store your
latitude and longitude according to the tutorial of google's 
API for markers. Add the marker (which is also described here
https://developers.google.com/maps/documentation/javascript/markers).
Keep in mind that you already have a `map` to set your marker on,
creating another one like in the tutorial WILL result in an error.
With google's API for listeners, create a click-listerner for your 
marker. `add.listener` is you friend here. Within the function of the
listener, create a string that opens up an unsorted list `<ul>` in HTML.
then define `parameters` with the content of geo being the `place_name`
of the argument place. `$.getJSON` the data of the route `/articles` and
add each entry in `data` to your string as a hyperlink that opens in a 
new tab `<a target='_blank' href=...` **WITHIN** a `<li>` tag in a 
for-loop. Don't forget to close each tag approproatly.  Sounds like a
doozy, but it really is easier than it sounds. At the end of the
for-loop that iterated through each element of `data`, finally add the
closing tag `</ul>`.
After all this, `.push` the `marker` into the `markers` array to store
it (and delete it afterwards in `removeMarkers`).

3. `removeMarkers` is the last function to do. in 4 simple lines, just
iterate through the elements in `markers` in a for loop, `.setMap(null)`
each one respectively and empty out the `markers` simply by setting them
to `[]`.

4. The website works accordingly and fulfills every aspect within the
specifications.