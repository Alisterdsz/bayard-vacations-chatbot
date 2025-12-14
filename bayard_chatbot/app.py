from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)
last_topic = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global last_topic
    user_message = request.json.get("message")

    reply, topic = get_response(user_message, last_topic)
    last_topic = topic

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
