from flask import Flask , request , jsonify
from learning import chatWithBot
app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
     chatInput = request.form['chatInput']
     return jsonify(chatBotReply=chatWithBot(chatInput))


@app.route('/index')
def index():
    return '<h1> HEROKU </h1>'

if __name__ == '__main__':
    app.run(debug=True)