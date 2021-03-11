from nltk.chat.util import Chat,reflections
from trainer import responsepair as pairs
def chatbot():
    print("Hi, I am your first chatbot ,pretty basic one!")
    chat=Chat(pairs,reflections)
    chat.converse()

if __name__ == '__main__':
    chatbot()