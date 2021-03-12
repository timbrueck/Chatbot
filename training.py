import numpy as np
import json
import pickle
import random

import nltk 
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.kear.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizer import SGD

lemmatizer = WordNetLemmatizer

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.tokenize(pattern)
        words.append(word_list)
        documents.append((word_list), intent['tag'])
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)

