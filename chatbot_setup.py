import sqlite3

def setup_database():
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS qa_pairs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT UNIQUE,
            answer TEXT
        )
    """)

    qa_data = [
        ("what is your name?", "I’m Chatbot, your friendly assistant!"),
        ("how are you?", "I’m doing great, thanks for asking!"),
        ("what time is it?", "I don’t have a watch, but it’s always chat time!"),
        ("who created you?", "I was created by a Python developer."),
        ("what is python?", "Python is a programming language known for simplicity."),
        ("what can you do?", "I can answer simple questions and chat with you."),
        ("where are you from?", "I live inside your computer!"),
        ("what is your favorite color?", "I like blue — it reminds me of the sky."),
        ("tell me a joke", "Why did the developer go broke? Because he used up all his cache!"),
        ("help", "Try asking: 'What is Python?', 'Tell me a joke', or 'Who created you?'.")
    ]

    for q, a in qa_data:
        try:
            c.execute("INSERT INTO qa_pairs (question, answer) VALUES (?, ?)", (q, a))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()
    print("✅ Database setup complete — chatbot.db created successfully.")

if __name__ == "__main__":
    setup_database()