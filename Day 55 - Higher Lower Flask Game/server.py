import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Choose a number between 0 and 9</h1>" \
           "<img src= 'https://media.giphy.com/media/tBvPFCFQHSpEI/giphy.gif'>"


number_to_guess = random.randint(0, 9)
print(number_to_guess)

@app.route('/<int:number_guessed>')
def compare_numbers(number_guessed):
    if number_guessed < number_to_guess:
        return "<h1 style='color: blue'>too low<br>try again</h1>" \
               "<img src='https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif'>"
    elif number_guessed > number_to_guess:
        return "<h1 style='color: orange'>too high<br>try again</h1>" \
               "<img src='https://media.giphy.com/media/KiYH45XAQe59K/giphy.gif'>"
    else:
        return "<h1 style='color: green'>YOU GOT IT!</h1>" \
               "<img src='https://media.giphy.com/media/ZXHLEcFUFzjwXb5UBw/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)