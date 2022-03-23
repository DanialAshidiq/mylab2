from flask import Flask, request, jsonify

from learning import chatWithBot
import unicodedata

app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    # unicodedata.normalize('NFKD', chatInput).encode('ascii', 'ignore')
    return jsonify(chatBotReply=chatWithBot(chatInput))


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True)
