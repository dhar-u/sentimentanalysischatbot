from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

greetings = ['hi', 'hello', 'hey', 'howdy']
farewells = ['bye', 'goodbye', 'see you', 'take care']
positive_words = ['good', 'great', 'awesome', 'happy', 'love', 'fantastic', 'excellent', 'amazing', 'wonderful', 'joyful']
negative_words = ['bad', 'sad', 'hate', 'angry', 'terrible', 'horrible', 'awful', 'disappointing', 'frustrating', 'unhappy']

def analyze_sentiment(user_input):
    score = 0
    user_words = user_input.lower().split()

    for word in user_words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    return score

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']
    bot_response = ""

    # Check for greetings
    if any(greet in user_input.lower() for greet in greetings):
        bot_response = "Hello! How can I assist you today?"
    # Check for farewells
    elif any(farewell in user_input.lower() for farewell in farewells):
        bot_response = "Goodbye! Have a great day!"
    # Simple sentiment analysis
    else:
        score = analyze_sentiment(user_input)

        if score > 2:
            bot_response = "That's wonderful to hear! Keep spreading the positivity!"
        elif score > 0:
            bot_response = "I'm glad to hear you're feeling positive!"
        elif score < -2:
            bot_response = "I'm really sorry to hear you're feeling that way. It's okay to feel down sometimes."
        elif score < 0:
            bot_response = "I'm sorry to hear you're feeling negative. If you want to talk about it, I'm here!"
        else:
            bot_response = "It seems like you have mixed feelings. Would you like to share more?"

    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)



