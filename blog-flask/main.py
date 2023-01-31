import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    posts = requests.get("https://api.npoint.io/a7823889ab46b7412ea8").json()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = requests.get(f"https://api.npoint.io/a7823889ab46b7412ea8/{post_id - 1}").json()
    print(post)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
