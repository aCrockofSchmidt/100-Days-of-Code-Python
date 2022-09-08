from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<some_name>')
def get_api_results(some_name):
    agify_url = f"https://api.agify.io?name={some_name}"
    genderize_url = f"https://api.genderize.io?name={some_name}"
    age_response = requests.get(agify_url)
    gender_response = requests.get(genderize_url)
    return render_template(
        "guess.html",
        age=age_response.json(),
        gen=gender_response.json(),
    )


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)