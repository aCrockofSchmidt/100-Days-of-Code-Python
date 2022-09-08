from flask import Flask, render_template
import requests

app = Flask(__name__)

# retrieve all blog data from api
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_data = response.json()
print(blog_data[0])


@app.route('/')
def home():
    return render_template("index.html", data=blog_data)


@app.route('/post/<int:postnum>')
def full_post(postnum):
    return render_template(
        "post.html",
        title=blog_data[postnum - 1]['title'],
        subtitle=blog_data[postnum - 1]['subtitle'],
        body=blog_data[postnum - 1]['body']
    )


if __name__ == "__main__":
    app.run(debug=True)
