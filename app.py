from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    message = request.args.get("message")
    if message is None:
        return render_template("main.html")
    else:
        output = []
        text = split(message)
        for text in text:
            code = translate(text)
            output.append(code)
        return f"{escape(message)} in morse code= {''.join(output)}"


def split(message):
    return [char for char in message]


def translate(text):
    if text == "A":  # Dictionary of translations for capital letters
        morse = ".- "
    elif text == "B":
        morse = "-... "
    elif text == "C":
        morse = "-.-. "
    elif text == "D":
        morse = "-.. "
    elif text == "E":
        morse = ". "
    elif text == "F":
        morse = "..-. "
    elif text == "G":
        morse = "--. "
    elif text == "H":
        morse = ".... "
    elif text == "I":
        morse = ".. "
    elif text == "J":
        morse = ".--- "
    elif text == "K":
        morse = "-.- "
    elif text == "L":
        morse = ".-.. "
    elif text == "M":
        morse = "-- "
    elif text == "N":
        morse = "-. "
    elif text == "O":
        morse = "--- "
    elif text == "P":
        morse = ".--. "
    elif text == "Q":
        morse = "--.- "
    elif text == "R":
        morse = ".-. "
    elif text == "S":
        morse = "... "
    elif text == "T":
        morse = "- "
    elif text == "U":
        morse = "..- "
    elif text == "V":
        morse = "...- "
    elif text == "W":
        morse = ".-- "
    elif text == "X":
        morse = "-..- "
    elif text == "Y":
        morse = "-.-- "
    elif text == "Z":
        morse = "--.. "
    elif text == "a":  # Dictionary of translations for non-capital letters
        morse = ".- "
    elif text == "b":
        morse = "-... "
    elif text == "c":
        morse = "-.-. "
    elif text == "d":
        morse = "-.. "
    elif text == "e":
        morse = ". "
    elif text == "f":
        morse = "..-. "
    elif text == "g":
        morse = "--. "
    elif text == "h":
        morse = ".... "
    elif text == "i":
        morse = ".. "
    elif text == "j":
        morse = ".--- "
    elif text == "k":
        morse = "-.- "
    elif text == "l":
        morse = ".-.. "
    elif text == "m":
        morse = "--"
    elif text == "n":
        morse = "-. "
    elif text == "o":
        morse = "--- "
    elif text == "p":
        morse = ".--. "
    elif text == "q":
        morse = "--.- "
    elif text == "r":
        morse = ".-. "
    elif text == "s":
        morse = "... "
    elif text == "t":
        morse = "- "
    elif text == "u":
        morse = "..- "
    elif text == "v":
        morse = "...- "
    elif text == "w":
        morse = ".-- "
    elif text == "x":
        morse = "-..- "
    elif text == "y":
        morse = "-.-- "
    elif text == "z":
        morse = "--.. "
    elif text == "0":  # Dictionary of translations for numbers
        morse = "----- "
    elif text == "1":
        morse = ".---- "
    elif text == "2":
        morse = "..--- "
    elif text == "3":
        morse = "...-- "
    elif text == "4":
        morse = "....- "
    elif text == "5":
        morse = "..... "
    elif text == "6":
        morse = "-.... "
    elif text == "7":
        morse = "--... "
    elif text == "8":
        morse = "---.. "
    elif text == "9":
        morse = "----. "
    elif text == " ":  # Dictionary of translations for other charaters
        morse = "    "
    elif text == "?":
        morse = "..--.. "
    elif text == ".":
        morse = ".-.-.- "
    elif text == ",":
        morse = "--..-- "
    else:
        morse = "Character(s) not availabe"
    return morse
