# Lecture 9

## Problemset 7

1. Implement a website via which users can "buy" and "sell" stocks, a la the below.

## Notes

### register

1. In order to get a good template for register i simply copied `login.html` ,
changed a few things and added another input for password confirmation.

2. In register i needed to check the following things: Has the user provided a username?
Has the user provided a password and confirmation? Do the passsword and confirmation
match? If all if the conditions i gathered with `request.form.get` above matched i could
hash the password with `pwd_context.encrypt`.

3. After hashing the password, i needed to check wether the the user i wanted to register
already existed. To do that i simply attempted an `INSERT` into the users table. If it
failed i would return an apology page, if it succeeded, the insertion has been made.

4. After successfully inserting the new user into the database, i stored the `user_id`
in the session and returned the index page

### quote

1. `quote.html` and `quoted.html` can also be very simply be derived from `login.html`.
if the route of quote gets called via `GET` , return the quote html and if the route
gets called via `POST` the quoted html gets returned. Before returning quote the
variables of the stock have to be aquired by `helper.py`'s `lookup()`. If `lookup()`
fails, simply return an apology page.

### buy

1. The `GET` method simply returns `buy.html`, the `POST` method is where the magic happens.

2. When the buy route get's called via `POST`, run `lookup()` and check if it fails. If it fails
return an apology page.

3. When `lookup()` succeeds retrieve the userdata via `db.execute` and get the username and cash
within the dict (`[0]["Cash/Username"]`). Get the count of the shares (be careful to cast the
value to `int()`). Calculate the resulting cash in another variable for later insertion.

4. Check if the user has cash, check if the user has ENOUGH cash. If that's not the case, return
an apology page, if the user has enough dosh to roll on, query some SQL.

5. In my case i have a table for stocks and for stock history. I check if the stock table has
the stock i want to add/insert already by `SELECT`ing form the stock table `WHERE` the user_id
AND the stock symbol match.

6. If `db.execute` doesn't return a value, insert the desired values via `INSERT`. If the table
contains the desired stock with the matching user_id, simply update the number of shares (else
case) .

7. After handling the stock table, simply insert the desired information into the history table.
The history table can easily disregard if any information may "seem" redundant, since we want
every transaction to be contained there.

8. Lastly, update the users cash, since nothing is free.

9. Return to index to have an overview over your belongings and cash.

### index

1. Index is fairly easy. The html simply needs a for loop of table elements (which are explained
in the problemsets walkthorugh). The static elements need to be implemented manually (values are
being inserted by `{{}}`).

2. Once the HTML is done, `SELECT` form the stock table `WHERE` the user_id matches the one in
the session, initialize a value for the total capital, iterate throug the elements wihtin the
stock and append the price via `lookup()` and the `total` value with a simple mulitplication.
Afterwards calculate the total value by adding every `total` value within each iteration.
when the for loop is done, `SELECT` the cash of the sessions' user and also add that to the
total value.

3. Simply return the rendered `index.html` with the values calculated above.

### sell

1. For the sell template simply mix the elements from buy and index.

2. Sell has the same logic as buy, with the difference that stocks are being substracted and
money is being added.

3. Another important difference is that it needs to be checked wether the stocks can be substracted
BEFORE querying to do so. If there are enoug shares, simply substract them. If the shares would be
exactly 0, `DELETE` the entry from the stock table. If there would be negative shares, return an
apology. The hirstory table however can simply contain the transaction as it is.

### history

1. Just like above, almost the same as index, with a different table and some slight alterations.
History merely needs to query a `SELECT` the history table where the user_id matches.
Then render the page with the values within the queried history dict.

### personal touch

1. In personal touches i was free to add one of three optional features... so i chose 2 of them.
Adding cash to the inventory and changing the password.

2. I made 3 html templates: special, password and cash. I also altered the `layout.html` to have
the button for the `special.html` page.

3. The special page just had 2 buttons that returned either the route for password or cash via GET.+

4. On the password route i went through a similar process of the one in register, with some slight
alterations to match my needs. I also borrowed the hash comparison from login. After checking each
condition, i simply `UPDATE`d the user's hash value to the new one.

5. For cash i set up the condition so that you have to give input (else it simply returns an apology).
I required the input to be above 0 (in consequence to be not negative).

6. After the conditions have been met, i added the cash input from the html input field and the users
cash value and queried an `UPDATE` on the users cash, and re-rendered the page with updated information.