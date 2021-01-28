import pickle

import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
from tensorflow.python.framework import ops
import numpy
import tflearn
import tensorflow
import random

import json

with open('chatbot.json') as file:
    data = json.load(file)
# Now our json data will be stored in the variable data.
print(data)
# EXTRACTING DATA
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    print("1. !!! EXTRACTING DATA !!!")
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data['chatbot']:
        for pattern in intent['patterns']:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])
    print("words from patterns: ", words)
    print(docs_x)
    print(docs_y)
    print("tags: ", labels)

    # WORD STEMMING
    print("2. !!! WORD STEMMING !!!")
    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))
    print("sorted words: ", words)
    labels = sorted(labels)
    print("sorted labels: ", labels)

    # We need some way to represent our sentences with numbers and this is where a bag of words comes in
    # BAG OF WORDS
    # Each position in the list will represent a word from our vocabulary.
    # If the position in the list is a 1 then that will mean that the word exists in our sentence, if it is a 0 then the word is nor present
    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    print("training: ", training)
    print("output: ", output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# DEVELOPING A MODEL
print("3. !!! DEVELOPING A MODEL !!!")

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

# model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
# model.save("model.tflearn")

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

# LOADING A MODEL
print("4. !!! LOADING A MODEL !!!")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["chatbot"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))


chat()
