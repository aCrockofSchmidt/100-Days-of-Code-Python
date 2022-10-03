from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create database to store books

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# create table in database
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)


db.create_all()

# create routes

#all_books = []


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = request.form
        # above is not needed if
        # using this instead: new_book = Books(title=request.form["title"] etc
        add_book = Books(title=new_book["title"], author=new_book["author"], rating=new_book["rating"])
        db.session.add(add_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        chosen_book_id = request.form["id"]
        chosen_book = Books.query.get(chosen_book_id)
        chosen_book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    chosen_book_id = request.args.get("id")
    chosen_book = Books.query.get(chosen_book_id)
    db.session.delete(chosen_book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

