#Building the actual chatbot
import random
import json
import pickle
import numpy as np

#These imports were for troubleshooting, ignore them
#from keras import backend as K
#from numpy import reshape

#Hope I'm not too late to answer.. But you can just create a new tag,
#such as "noanswer", have the patterns array empty, and then populate
#the responses array however you want.
import sys
import tensorflow as tf

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

model = load_model("chatbotmodel.h5")

def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    #changed to word.lower() here and in train.py for better efficiency
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)
    bag = [tf.convert_to_tensor(0, dtype=tf.float32)] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = tf.convert_to_tensor(1, dtype=tf.float32) #ints must be converted like this
    
    return bag #this originally was return np.array

def predict_class(sentence):
    bow = bag_of_words(sentence)
    
    #troubleshooting
    #bow = np.array(bow)
    #bow = bow.reshape(-1, -1)
    
    res = model.predict(np.array([bow]), verbose=0)[0] #had to change this to
                                                    #verbose=0 to disable prog bar
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability" : str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    
    for i in list_of_intents:
        #function code here probably?
        #if i["tag"] == the tag which triggers the function
            #execute function
            #function = "func"
            #break
        if i["tag"] == tag:
            result = random.choice(i['responses'])
            #function = "chat"
            break
    return result

print("Chatbot is running")

while True:
    #will need to switch between while loops for
    #function mode vs chat bot mode??
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
    




"""
while True:
    while Function == "chat":
        message = input("")
        ints = predict_class(message)
        res = get_response(ints, intents)
        print(res)
        break

    while Function == "txtbox":
        execute function
        break
"""
