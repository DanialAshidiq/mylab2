from flask import Flask , request , jsonify
from learning import chatWithBot
app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    # unicodedata.normalize('NFKD', chatInput).encode('ascii', 'ignore')
    return jsonify(chatBotReply=chatWithBot(chatInput))


@app.route('/index')
def index():
    return '<h1> HEROKU </h1>'

if __name__ == '__main__':
    app.run(debug=True)