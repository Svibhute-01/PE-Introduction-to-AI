from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_response
import sqlite3

app = Flask(__name__)

# Save each message and reply to chat_history
def save_chat(user_msg, bot_reply):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (user_msg, bot_reply) VALUES (?, ?)", (user_msg, bot_reply))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # Load previous chat history
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT user_msg, bot_reply FROM chat_history ORDER BY id DESC LIMIT 10")
    chats = c.fetchall()
    conn.close()
    chats.reverse()  # to show in order
    return render_template('index.html', chats=chats)

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_msg = request.form['msg']
    bot_reply = get_response(user_msg)
    save_chat(user_msg, bot_reply)
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
