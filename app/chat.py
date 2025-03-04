# chat.py
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Simple response for now, you can enhance it as needed
    bot_response = f"Bot says: You said '{user_message}'"
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
