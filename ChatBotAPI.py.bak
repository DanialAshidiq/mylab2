from flask import Flask, request, jsonify

from main import chatWithBot
import unicodedata

app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    # unicodedata.normalize('NFKD', chatInput).encode('ascii', 'ignore')
    return jsonify(chatBotReply=chatWithBot(chatInput))


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="192.168.1.116", debug=True)
