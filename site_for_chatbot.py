from flask import Flask, render_template, request
import chatbot as mymodule

app = Flask(__name__)
#app.static_folder='static'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get')
def get_bot_response():
    userAnswer = request.args.get('msg')
    chat = mymodule.ChatBot(userAnswer)
    #print(str(chat.check_answer()))
    return str(chat.check_answer())


if __name__ == '__main__':
    app.run()
