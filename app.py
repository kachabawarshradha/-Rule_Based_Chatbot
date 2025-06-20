
from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based chatbot responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "what is your name": "I'm your AI assistant chatbot.",
    "help": "You can ask me about anything like greetings, help, or basic questions."
}

def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I didn't understand that.")

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        bot_response = get_response(user_input)
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
