from datetime import datetime

# Define the chatbot function
def chatBot(n):
    n = n.lower()  # Convert user input to lowercase for case-insensitive matching
    
    # Defining responses for various inputs(rules)
    if "hello" in n or "hi" in n:
        return "Hi there! How are you?"
    elif "how are you" in n:
        return "I'm here and ready to help you! How about you?"
    elif "your name" in n:
        return "I'm ChatBot, your friendly assistant."
    elif "time" in n:
        time = datetime.now()
        current_time = time.strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "date" in n:
        date = datetime.today().strftime('%Y-%m-%d')
        return f"Today's date is {date}."
    elif "thank you" in n or "thanks" in n:
        return "You're welcome! Is there anything else I can help with?"
    elif "help" in n:
        return "Sure! I'm here to help. What do you need assistance with?"
    elif "weather" in n:
        return "I'm sorry, I can't provide weather updates at the moment. Please check your local weather service."
    elif "joke" in n:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "who are you" in n:
        return "I'm ChatGPT, an AI developed by OpenAI to assist with your queries."
    elif "what can you do" in n:
        return "I can chat with you, answer questions, tell jokes, and provide information on various topics."
    elif "where are you from" in n:
        return "I'm from the cloud, hosted by OpenAI."
    elif "how old are you" in n:
        return "I don't have a physical form or age in the way humans do. I'm an artificial intelligence, so I don't experience time or aging as you do."
    elif "favorite color" in n:
        return "As an AI, I don't have preferences, but I think blue is quite nice!"
    elif "favorite food" in n:
        return "Since I don't have a physical form or the ability to taste, I don't have favorite foods like humans do. But I can help you with information or recommendations about different types of food if you'd like!"
    elif "bye" in n or "goodbye" in n:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Example of interacting with the chatbot
while True:
    #n is a variable used to take input from the user.
    n = input("You: ")
    if "bye" in n.lower() or "goodbye" in n.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    res = chatBot(n)
    print(f"Chatbot: {res}")
