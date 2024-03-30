import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi",
        ["Hello :)"],
    ],
    [
        r"hi my name is (.*)",
        ["Hello :) %1! How can I help you?", "Hi %1! What can I do for you?", "Hey %1! What is today's task?"],
    ],
    [
        r"what is your name?",
        ["I am a chatbot based on Python programming language. I don't have any particular name, but you can call me Jarvis Jr."],
    ],
    [
        r"how are you",
        ["I am good. Thanks for asking."],
    ],
    [
        r"what is your age?",
        ["I don't have an age. I'm just a computer program based on Python programming language."],
    ],
    [
        r"what can you do",
        ["I can help you with some general queries."],
    ],
    [
        r"what is your favorite song",
        ["I don't listen songs"],
    ],
    [
        r"what would you prefer android or ios",
        ["Depends on your requirements. If I had an option to choose between them I would choose iOS because of it's secure ecosystem"],
    ],
    [
        r"bye",
        ["Goodbye! Feel free to ask more queries."],
    ],
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello, I am Jarvis Jr. chatbot. Type 'adios' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'adios':
            print("Chatbot: adios amigo! Take care.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download("punkt")
    chat()