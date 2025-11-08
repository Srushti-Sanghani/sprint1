from datetime import datetime

def print_with_time(sender, message):
    """Prints messages with the current time and sender label."""
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"{current_time} {sender}: {message}")

INTERNAL_QA = {
    "what is your name": "I am Chatbot 3000.",
    "how are you": "I'm doing great, thank you!",
    "what is python": "Python is a powerful and easy-to-learn programming language.",
    "what is the capital of france": "The capital of France is Paris.",
    "who created you": "I was created by a developer using Python.",
    "what can you do": "I can answer basic questions and chat with you!",
    "what is 2 plus 2": "2 plus 2 equals 4.",
    "what is the largest planet": "Jupiter is the largest planet in our solar system.",
    "who is the president of the usa": "As of 2025, the President of the USA is Joe Biden.",
    "what is the tallest mountain": "Mount Everest is the tallest mountain in the world.",
}

def get_answer(user_input):
    """Return the answer if the question matches internal Q&A."""
    return INTERNAL_QA.get(user_input.strip().lower(), None)

def main():
    """Main chatbot logic."""
    print_with_time("Chatbot", "Hello!")
    print_with_time("Chatbot", "How can I help you?")

    while True:
        user_input = input()
        print_with_time("User", user_input)

        if user_input.lower() in ["bye", "exit", "quit"]:
            print_with_time("Chatbot", "Goodbye! Have a great day!")
            break

        answer = get_answer(user_input)

        if answer:
            print_with_time("Chatbot", answer)
            print_with_time("Chatbot", "What else would you like to know?")
        else:
            print_with_time("Chatbot", "Sorry, I don’t recognize that question.")
            print_with_time("Chatbot", "How can I help you?")

if __name__ == "__main__":
    main()