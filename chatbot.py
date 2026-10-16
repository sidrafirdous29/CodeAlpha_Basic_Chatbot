import random

print("===== MY PYTHON CHATBOT =====")
print("Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if "hello" in user or "hi" in user:
        replies = ["Hello!", "Hi there!", "Hey! 😊"]
        print("Bot:", random.choice(replies))

    elif "how are you" in user:
        print("Bot: I'm fine! How are you?")

    elif "your name" in user:
        print("Bot: I am a Python chatbot!")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
