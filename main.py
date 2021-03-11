from nltk.chat.util import Chat,reflections
pairs=[
    ['my name is (.*)',['hello %1 , how are you doing today?']],
    ['bye',['Bye,It was nice conversing with you']],
]
def chatbot():
    print("Hi, I am your first chatbot ,pretty basic one!")
    chat=Chat(pairs,reflections)
    chat.converse()

if __name__ == '__main__':
    chatbot()