from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    
    stocks = db.execute("SELECT * FROM stocks WHERE user_id = :user_id", user_id = session["user_id"])
    total = 0
    for stock in stocks:
        stock["price"] = lookup(stock["symbol"])["price"]
        stock["total"] = stock["price"] * stock["shares"]
        total = total + stock["total"]
    cash = db.execute("SELECT * FROM users WHERE id = :userID", userID=session["user_id"])[0]["cash"]
    total = total+cash
    
    return render_template("index.html", stocks=stocks, cash=cash, total=total)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    
    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("Invalid stock symbol")
            
        userdata = db.execute("SELECT * FROM users WHERE id = :userID", userID=session["user_id"])
        username= userdata[0]["username"]
        cash = userdata[0]["cash"]
        count = int(request.form.get("count"))
        quote = lookup(request.form.get("symbol"))
        newCash = cash-quote["price"] * count
        
        if cash == None:
            return apology("Cash is None")
        
        if quote["price"] * count >= cash:
            return apology("Not enough cash")
            
        stocks = db.execute(
                    "SELECT * FROM stocks WHERE \
                    symbol = :symbol AND \
                    user_id = :user_id",
                    symbol = quote["symbol"],
                    user_id = session["user_id"]
                    )
                    
        if not stocks:
            db.execute("INSERT INTO stocks \
                    (user_id, symbol, name, \
                    shares) VALUES (:user_id, \
                    :symbol, :name, :shares)",
                    user_id=session["user_id"],
                    symbol=quote["symbol"],
                    name=quote["name"],
                    shares=count
                    )
                    
        else: 
            shareCount = db.execute("SELECT * FROM stocks WHERE symbol = :symbol",
            symbol=quote["symbol"])[0]["shares"]
            newShareCount = shareCount + count
            db.execute(
                    "UPDATE stocks SET shares \
                    = :newShareCount WHERE \
                    symbol = :symbol AND \
                    user_id = :user_id", 
                    newShareCount = newShareCount,
                    symbol = quote["symbol"],
                    user_id = session["user_id"]
                    )
        

        db.execute(
                    "INSERT INTO history \
                    (user_id, username, \
                    stockname, stockprice,\
                    stockcount, symbol) VALUES \
                    (:user_id, :username,\
                    :stockname, :stockprice,\
                    :stockcount, :symbol)",
                    user_id=session["user_id"],
                    username=username,
                    stockname=quote["name"],
                    stockprice=quote["price"],
                    stockcount=count,
                    symbol=quote["symbol"]
        )
        
        db.execute("UPDATE users SET cash=:newCash WHERE id =:userID",
            newCash = newCash,
            userID = session["user_id"]
        )
    
        return index()
        
    if request.method == "GET":
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    
    history = db.execute("SELECT * FROM history WHERE user_id = :user_id", user_id = session["user_id"])
    
    return render_template("history.html", history=history)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    
    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("Invalid stock symbol")
        return render_template("quoted.html", name=quote["name"] ,price=quote["price"] , symbol=quote["symbol"])
    if request.method == "GET":
        return render_template("quote.html")

    

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # ensure password confirmation was submitted
        elif not request.form.get("confirm_password"):
            return apology("must provide password confirmation")
            
        if request.form.get("password") != request.form.get("confirm_password"):
            return apology("password and confirmation must be equal")
            
        hash=pwd_context.encrypt(request.form.get("password"))
            
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"), hash=hash)
        if not result:
            return apology("Username already taken")
            
        result = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        session["user_id"] = result[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("Invalid stock symbol")
            
        userdata = db.execute("SELECT * FROM users WHERE id = :userID", userID=session["user_id"])
        username= userdata[0]["username"]
        cash = userdata[0]["cash"]
        count = int(request.form.get("count"))
        quote = lookup(request.form.get("symbol"))
        newCash = cash+quote["price"] * count
            
        stocks = db.execute(
                    "SELECT * FROM stocks WHERE \
                    symbol = :symbol AND \
                    user_id = :user_id",
                    symbol = quote["symbol"],
                    user_id = session["user_id"]
                    )
                    
        if not stocks:
            return apology("Stock is not in your Inventory")
                    
        else: 
            shareCount = db.execute("SELECT * FROM stocks WHERE symbol = :symbol",
            symbol=quote["symbol"])[0]["shares"]
            newShareCount = shareCount - count
            
            if newShareCount < 0:
                return apology("Not enough Shares to sell")
                
            if newShareCount == 0:
                db.execute(
                        "DELETE FROM stocks WHERE \
                        symbol = :symbol AND \
                        user_id = :user_id",
                        symbol = quote["symbol"],
                        user_id = session["user_id"]
                        )
                
            if newShareCount > 0:
                db.execute(
                        "UPDATE stocks SET shares \
                        = :newShareCount WHERE \
                        symbol = :symbol AND \
                        user_id = :user_id", 
                        newShareCount = newShareCount,
                        symbol = quote["symbol"],
                        user_id = session["user_id"]
                        )
        

        db.execute(
                    "INSERT INTO history \
                    (user_id, username, \
                    stockname, stockprice,\
                    stockcount, symbol) VALUES \
                    (:user_id, :username,\
                    :stockname, :stockprice,\
                    :stockcount, :symbol)",
                    user_id=session["user_id"],
                    username=username,
                    stockname=quote["name"],
                    stockprice=quote["price"],
                    stockcount= count * -1,
                    symbol=quote["symbol"]
        )
        
        db.execute("UPDATE users SET cash=:newCash WHERE id =:userID",
            newCash = newCash,
            userID = session["user_id"]
        )
    
        return index()
        
    if request.method == "GET":
        stocks = db.execute("SELECT * FROM stocks WHERE user_id = :user_id", user_id = session["user_id"])
        total = 0
        for stock in stocks:
            stock["price"] = lookup(stock["symbol"])["price"]
            stock["total"] = stock["price"] * stock["shares"]
            total = total + stock["total"]
        cash = db.execute("SELECT * FROM users WHERE id = :userID", userID=session["user_id"])[0]["cash"]
        
        return render_template("sell.html", stocks=stocks, cash=cash)
        
@app.route("/special", methods=["GET", "POST"])
@login_required
def special():
    if request.method == "GET":
        return render_template("special.html")    
        
@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    if request.method == "POST":
        if not request.form.get("password"):
            return apology("must provide old password")
            
        if not request.form.get("password_confirm"):
            return apology("must provide password confirmation")
            
        if not request.form.get("password_new"):
            return apology("must provide new password")
            
        if request.form.get("password") != request.form.get("password_confirm"):
            return apology("password and confirmation must be equal")
            
        if request.form.get("password") == request.form.get("password_new"):
            return apology("old and new password cannot be equal")
            
        rows = db.execute("SELECT * FROM users WHERE id = :userID", userID=session["user_id"])
            
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid old password")
            
        hash=pwd_context.encrypt(request.form.get("password_new"))
            
        db.execute("UPDATE users SET hash = :hash WHERE id = :userID", hash=hash, userID=session["user_id"])
            
        return render_template("password.html", message="The password has been successfully changed")  
        
    if request.method == "GET":
        return render_template("password.html")  
        
@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():
    if request.method == "POST":
        if request.form.get("cash") == "":
            return apology("Need mone")
        if int(request.form.get("cash")) <= 0:
            return apology("Need moar mone")
        moarCash = int(request.form.get("cash"))
        cash = db.execute("SELECT * FROM users WHERE id = :userID", userID=session["user_id"])[0]["cash"]
        newCash = cash + moarCash
        db.execute("UPDATE users SET cash = :newCash WHERE id = :userID", newCash=newCash, userID=session["user_id"])
        return render_template("cash.html", cash=newCash, moarCash=moarCash, message="Moni haz been aquired")  
        
        
    if request.method == "GET":
        cash = db.execute("SELECT * FROM users WHERE id = :userID", userID=session["user_id"])[0]["cash"]
        return render_template("cash.html", cash=cash)  