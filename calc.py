from flask import Flask, render_template, request
from string import ascii_uppercase as alphabet


def generateKey(string, key):
    key = list(key)
    string = string.upper()
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return "" . join(key)


def cipherText(string, key):
    cipher_text = []
    string = string.upper()
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "" . join(cipher_text)


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "" . join(orig_text)


def codes_table(char):
    table = {
        "A": 11, "B": 21, "C": 31, "D": 41, "E": 51,
        "F": 12, "G": 22, "H": 32, "I": 42, "K": 52,
        "L": 13, "M": 23, "N": 33, "O": 43, "P": 53,
        "Q": 14, "R": 24, "S": 34, "T": 44, "U": 54,
        "V": 15, "W": 25, "X": 35, "Y": 45, "Z": 55, "J": 0,

        11: "A", 21: "B", 31: "C", 41: "D", 51: "E",
        12: "F", 22: "G", 32: "H", 42: "I", 52: "K",
        13: "L", 23: "M", 33: "N", 43: "O", 53: "P",
        14: "Q", 24: "R", 34: "S", 44: "T", 54: "U",
        15: "V", 25: "W", 35: "X", 45: "Y", 55: "Z", 0: "J"
    }

    return table[char]


def encoding(text):
    text, finished_text = text.upper(), ""
    for symbol in text:
        if symbol in alphabet:
            finished_text += str(codes_table(symbol)) + "_"

    return finished_text[:-1]


def decoding(text):
    text, finished_text = text.upper(), ""
    for symbol in list(map(int, text.split(sep="_"))):
        finished_text += codes_table(symbol)

    return finished_text


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result():
    string = request.form.get("string", type=str, default=0)
    keyword = request.form.get("keyword", type=str, default=0)
    operation = request.form.get("operation")
    key = generateKey(string, keyword)
    if operation == 'Encrypt':
        simple2vigenere = cipherText(string, key)
        vigenere2polybius = encoding(simple2vigenere)
        output_1 = simple2vigenere
        output_2 = vigenere2polybius

    elif operation == 'Decrypt':
        polybius2vigenere = decoding(string)
        vigenere2simple = originalText(polybius2vigenere, key)
        output_1 = polybius2vigenere
        output_2 = vigenere2simple

    else:
        output_1 = 'Error'
        output_2 = 'Error'
    return render_template('form.html', entry=output_1, entry_1=output_2)


if __name__ == '__main__':
    app.run(debug=True)
