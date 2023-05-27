from flask import Flask, render_template, request


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return "" . join(key)


def cipherText(string, key):
    cipher_text = []
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
        cipher_text = cipherText(string, key)
        output = cipher_text
    elif operation == 'Decrypt':
        orignal_text = originalText(string, key)
        output = orignal_text
    else:
        output = 'None'
    entry = output
    return render_template('form.html', entry=entry)


if __name__ == '__main__':
    app.run(debug=True)
