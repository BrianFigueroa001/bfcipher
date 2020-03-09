#cipherserver.py
from flask import Flask, render_template, url_for, request, redirect
import os
import CipherKey

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
#Code goes into this function.
def index():
    output = "Test"

    if request.method == 'GET':    
        key = CipherKey.SymmetricKey()

        message = request.args.get('userMessage')

        if str(request.args.get('SubmitButton')) == "Encrypt":
            output = key.encrypt(message)

        elif str(request.args.get("SubmitButton")) == "Decrypt":
            output = key.decrypt(message)
        else:
            output = "Oopsie!"

    return render_template('index.html', output = output)

if __name__ == "__main__":
    #Required hostname and port to be hosted on Heroku.
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)