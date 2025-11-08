import sqlite3
import time
import sys

# ------------------------------
# Utility functions
# ------------------------------
def timestamp():
    """Return the current time formatted as HH:MM:SS"""
    return time.strftime("%H:%M:%S")

def print_message(message):
    """Print a message in the format HH:MM:SS Message"""
    print(f"{timestamp()} {message}")

def get_answer(user_question):
    """Retrieve answer from the SQLite database"""
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute("SELECT answer FROM qa_pairs WHERE question = ?", (user_question.lower(),))
    row = c.fetchone()
    conn.close()
    if row:
        return row[0]
    return None

# ------------------------------
# Main chatbot program
# ------------------------------
def main():
    # Greeting messages
    print_message("Hello!")
    time.sleep(1)
    print_message("How can I help you?")

    while True:
        # Get user input
        user_input = input("> ").strip()

        # Exit condition
        if user_input.lower() == "bye":
            print_message("Goodbye!")
            sys.exit()

        # Repeat user's message
        print_message(user_input)

        # Check for a matching answer
        answer = get_answer(user_input)
        if answer:
            time.sleep(1)
            print_message(answer)
        else:
            time.sleep(1)
            print_message("I don’t recognize that question. Please ask another one.")

if __name__ == "__main__":
    main()