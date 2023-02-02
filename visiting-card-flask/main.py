from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", data={
        "name": "Ripul Chhabra",
        "profession": "Software Engineer",
        "year": datetime.datetime.now().year,
        "twitter": "https://twitter.com/ripulchhabra",
        "github": "https://github.com/iRipul"
    })


if __name__ == "__main__":
    app.run(debug=True, port=3000)
