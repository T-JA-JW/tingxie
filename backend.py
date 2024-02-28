from flask import Flask, render_template, request, jsonify, session
from flask_session import Session  # Flask-Session for server-side session management
import random

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['words']
        words = text.split('\n')
        words = [word.strip() for word in words if word.strip() != '']  # Remove empty lines
        session['words'] = words  # Store the words in the session
        return render_template('index.html', words=words)
    return render_template('index.html', words=[])

@app.route('/get-word')
def get_word():
    words = session.get('words', [])
    if not words:
        return jsonify(word="No words provided."), 400
    word = random.choice(words)
    return jsonify(word=word)

if __name__ == '__main__':
    app.run(debug=True)
