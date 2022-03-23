from flask import Flask , request , jsonify
from main import chatWithBot

app = Flask(__name__)

@app.route('/chat')
def chat():
    chatInput = request.form['chatInput']
    # unicodedata.normalize('NFKD', chatInput).encode('ascii', 'ignore')
    return '<h1>' + jsonify(chatBotReply=chatWithBot(chatInput))  + '</h1>'
@app.route('/index')
def index():
    return '<h1> HEROKU </h1>'

if __name__ == '__main__':
    app.run(debug=True)