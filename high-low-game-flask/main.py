from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)


@app.route("/")
def index():
    global random_number
    random_number = randint(0, 9)
    return "<h1>Guess the number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:num>")
def guess(num):
    response = ""
    if num < random_number:
        response = """
            <h1>This is too low.</h1>
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>
        """
    elif num > random_number:
        response = """
                    <h1>This is too high.</h1>
                    <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>
                """
    else:
        response = """
                    <h1>Yeah! You got it.</h1>
                    <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>
                """
    return response


if __name__ == "__main__":
    app.run(debug=True, port=3000)
