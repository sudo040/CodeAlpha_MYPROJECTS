def get_response(user_input):
    """Return a reply based on the user's input using if-elif rules."""
    message = user_input.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message in ("how are you", "how are you?", "how r u"):
        return "I'm fine, thanks!"
    elif message in ("bye", "goodbye", "see you"):
        return "Goodbye!"
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple rule-based chatbot."
    else:
        return "Sorry, I don't understand that yet."


def run_chatbot():
    """Main loop: read input, respond, and stop when the user says goodbye."""
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.strip().lower() in ("bye", "goodbye", "see you"):
            break


if __name__ == "__main__":
    run_chatbot()