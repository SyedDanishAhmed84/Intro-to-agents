class Agent:
    def __init__(self):
        print("Chat Agent is online")
        print("Type 'Bye' to exit.\n")
    
    def response(self,message):
        message=message.lower()

        if "hello" in message or "hi" in message:
            return "Hey, how I can help you?"
        elif "how are you" in message:
            return "I'm good, how are you?"
        elif "your name" in message:
            return "I'm a simple chatbot agent"    
        elif "help" in message:
            return "Which type of help you need?"
        elif "bye" in message:
            return "Goodbye"
        
        else:
            return "Sorry I didn't understand this"
        

agent=Agent()
while True:
    user_input=input("You: ")
    reply=agent.response(user_input)
    print("Agent: ",reply)

    if "bye" in user_input.lower():
        break

