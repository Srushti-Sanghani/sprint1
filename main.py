def main():
    # The app's internal (predefined) question and answer
    internal_question = "What is the capital of France?"
    internal_answer = "The capital of France is Paris."

    # Opening prompt
    print("Welcome! Ask me a question:")

    # Get user input
    user_question = input("> ").strip()

    # Compare user question to internal question
    if user_question.lower() == internal_question.lower():
        print(internal_answer)
    else:
        print("Sorry, I don’t recognize that question. Please ask another one.")


if __name__ == "__main__":
    main()
	
	