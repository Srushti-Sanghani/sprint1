import time
import sys

def timestamp():
    """Return the current time formatted as HH:MM:SS"""
    return time.strftime("%H:%M:%S")

def print_message(message):
    """Print a message with timestamp in the format HH:MM:SS Message"""
    print(f"{timestamp()} {message}")

def main():
    qa_pairs = {
        "what is your name?": "I’m Chatbot, your friendly assistant!",
        "how are you?": "I’m doing great, thanks for asking!",
        "what time is it?": lambda: f"The current time is {timestamp()}",
        "who created you?": "I was created by a developer who loves Python.",
        "what is python?": "Python is a programming language known for simplicity and versatility.",
        "what can you do?": "I can answer basic questions and chat with you!",
        "where are you from?": "I live inside your computer!",
        "tell me a joke": "Why did the programmer quit his job? Because he didn’t get arrays!",
        "what is your favorite color?": "I like blue — it reminds me of calm skies and clean code.",
        "how old are you?": "I don’t age — I’m as old as the moment you run me!",
        "help": "You can ask me things like 'What is Python?', 'Tell me a joke', or type 'bye' to exit."
    }

    print_message("Hello!")
    time.sleep(1)
    print_message("How can I help you?")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "bye":
            print_message("Goodbye!")
            sys.exit()

        print_message(user_input)

        response = qa_pairs.get(user_input.lower())

        if response:
            if callable(response):
                response = response()
            time.sleep(1)
            print_message(response)
        else:
            time.sleep(1)
            print_message("I don’t recognize that question. Please ask another one.")

if __name__ == "__main__":
    main()