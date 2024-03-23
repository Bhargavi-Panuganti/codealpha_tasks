import nltk
from nltk.chat.util import Chat,reflections
pairs=[
    [
        r"hello|hi|hey",
        ["Hello , How are you today?"]
    ],
    [
        r"I'm fine",
        ["Glad to hear that,how can I help you?"]
    ]
    [
        r"who are you",
        ["well I'm a chat Bot"]
    ],
    [
        r"ok",
        ["Is there anything you want to ask"]
    ],
    [
        r"no",
        ["it's fine"]
    ],
    [
        r"what is your name?",
        ["My name is AI assistant"]
    ]
]
print(reflections)
print("You can Start.....")
chat=Chat(pairs)
chat.converse(quit=quit)