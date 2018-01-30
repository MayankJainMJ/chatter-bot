#coding=utf-8
from flask import Flask, render_template, request, jsonify
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

app = Flask(__name__)
os.chdir('/Users/mayan/Desktop/CHATBOT/chatter bot/')
bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train("chatterbot.corpus.english")
# bot.train("chatterbot.corpus.hindi")
bot.set_trainer(ListTrainer)
conv = open('/Users/mayan/Desktop/CHATBOT/chatter bot/Chats/course.txt','r').readlines()
bot.train(conv)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    userText = str(request.form['messageText'])   
    return jsonify({'status':'OK','answer':str(bot.get_response(userText))})

if __name__ == "__main__":
    app.run(debug=True)
#    app.run(debug=True, host='0.0.0.0', port=15555)


#logging.basicConfig(level=logging.INFO)
