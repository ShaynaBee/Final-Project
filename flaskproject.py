from flask import Flask, render_template, request

app = Flask(__name__)

from MLmodelscript import *

def generate_tweet(word):
    generated_text = generate_text(model,num_generate=260,temperature=1,start_string=word)
    return generated_text

@app.route("/home", methods=['GET', 'POST'])
def home():
    print(request.method)
    tweet = ''
    if request.method == 'POST':
        word = request.form["word"]
        tweet = generate_tweet(word)
    return render_template("index.html", tweet=tweet)

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=8888)