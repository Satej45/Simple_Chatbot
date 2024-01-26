import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you", ["I'm doing well, thank you!", "I'm fine, how about you?"]),
    (r"what is your name", ["I am a chatbot.", "You can call me ChatGPT."]),
    (r"quit|exit|bye", ["Goodbye!", "See you later!"]),
    (r"what is your purpose", ["I'm here to assist and chat with you.", "My purpose is to help and provide information."]),
    (r"who created you", ["I was created by Satej Sawant.", "I'm a product of Satej Sawant technology."]),
    (r"tell me a joke|say something funny", ["Why don't scientists trust atoms? Because they make up everything!"]),
    (r"weather in (.*)", ["I'm sorry, I don't have real-time weather information. You can use a weather API for that."]),
    (r"define (.*)", ["I can provide simple definitions, but for detailed information, you might want to use a dictionary."]),
    (r"how old are you", ["I don't have an age as I am just a computer program."]),
    (r"favorite color", ["I don't have preferences as I am not a person."]),
    (r"tell me about yourself", ["I am a chatbot designed to assist and engage in conversations.", "I am a computer program created to interact with users."]),
    (r"where are you from", ["I don't have a specific origin as I am a software program.", "I exist in the digital world."]),
    (r"can you help me with (.*)", ["I'll do my best to help you. Please provide more details."]),
    (r"favorite book|recommend a book", ["I don't have personal preferences, but '1984' by George Orwell is a classic."]),
    (r"how do you do", ["I'm just a computer program, but I'm doing well. How about you?"]),
    (r"who is your favorite superhero", ["I don't have personal preferences, but superheroes like Batman and Superman are popular."]),
    (r"tell me a fun fact", ["The honeybee is the only insect that produces food eaten by humans."]),
    (r"movie recommendations", ["I don't watch movies, but 'The Shawshank Redemption' is highly recommended."]),
    (r"what is the meaning of life", ["The meaning of life is a philosophical question. Different people have different perspectives."]),
    (r"tell me about artificial intelligence", ["Artificial intelligence involves creating machines that can perform tasks that typically require human intelligence."]),
    (r"do you believe in ghosts", ["I don't have beliefs or opinions as I am a computer program."]),
    (r"tell me a riddle", ["I can't think of one off the top of my head, but here's a classic: What has keys but can't d locks?"]),
    (r"how much wood would a woodchuck chuck", ["A woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could chuck wood."]),
]

# Create a chatbot using the Chat class
chatbot = Chat(patterns, reflections)

# Function to start and run the chatbot
def run_chatbot():
    print("Chatbot: Hello! I'm here to help. Type 'quit' to exit.")
    
    # Run the chatbot in a loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download("punkt")  # Download the punkt tokenizer if not already downloaded
    run_chatbot()
