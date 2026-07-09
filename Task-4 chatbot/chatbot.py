def chatbot():
    print(" ===================================")
    print("      Welcome to Simple Chatbot")
    print(" ===================================")
    print(" Type 'bye' to exit.\n")

    while True:
        user = input(" You: ").lower()

        if user == "hello":
            print(" Bot: Hi! Nice to meet you.")

        elif user == "hi" or user == "hey" or user=="hii":
            print(" Bot: Hello! How can I help you?")

        elif user == "how are you?":
            print(" Bot: I'm fine, thanks! How about you?")

        elif user == "i am fine":
            print(" Bot: That's great to hear!")

        elif user == "what is your name?":
            print(" Bot: My name is SimpleBot.")

        elif user == "who created you?":
            print(" Bot: I was created using Python.")

        elif user == "thank you" or user == "ok" or user == "thanks" or user == "okay":
            print(" Bot: You're welcome!")

        elif user == "bye":
            print(" Bot: Goodbye! Have a nice day.")
            break

        else:
            print(" Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()