def chatbot():
    print("🤖 Chatbot: Hello! I am a simple chatbot. Type something (or type 'exit' to quit).")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
        elif user_input == "exit":
            print("🤖 Chatbot: Exiting chat. Have a nice day!")
            break
        else:
            print("🤖 Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()