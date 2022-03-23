from flask import Flask , request , jsonify
from main import chatWithBot
app = Flask(__name__)

@app.route('/index')
def index():
    chatInput = request.form['chatInput']
    # unicodedata.normalize('NFKD', chatInput).encode('ascii', 'ignore')
    return '<h1>' + jsonify(chatBotReply=chatWithBot(chatInput))  + '<h1>'

if __name__ == '__main__':
    app.run(debug=True)