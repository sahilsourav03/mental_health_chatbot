from chatbot import get_response
from sentiment_analysis import analyze_sentiment

def main():
    print("🧠 Mental Health Chatbot (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Take care! Remember, you're not alone. 💙")
            break

        # Sentiment analysis
        sentiment = analyze_sentiment(user_input)
        print(f"[Detected Sentiment: {sentiment}]")

        # Chatbot response
        response = get_response(user_input, sentiment)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
