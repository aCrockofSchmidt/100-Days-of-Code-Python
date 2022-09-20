from flask import Flask, render_template, request
import requests
import smtplib
import os

EMAIL_PASS = os.environ.get("GMAIL_PASSWORD")

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


@app.route('/contact.html', methods=["GET", "POST"])
def go_to_contact():
    if request.method == "POST":
        user_input = request.form
        print(user_input["name"])
        print(user_input["email"])
        print(user_input["phone"])
        print(user_input["message"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="the.legendary.flush@gmail.com", password=EMAIL_PASS)
            connection.sendmail(
                from_addr="the.legendary.flush@gmail.com",
                to_addrs=user_input['email'],
                msg=f"Subject:  Form Submission\n\n{user_input['message']}"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)