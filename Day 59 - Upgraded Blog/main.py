from flask import Flask, render_template
import requests

blog_data = requests.get("https://api.npoint.io/b55b8d1b724ea2ead604").json()


app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def get_all_posts():
    return render_template("index.html", all_posts=blog_data)


@app.route('/post.html/<int:index>')
def go_to_post(index):
    requested_post = None
    for blog_post in blog_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about.html')
def go_to_about():
    return render_template("about.html")


@app.route('/contact.html')
def go_to_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)