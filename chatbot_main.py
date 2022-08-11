#Building the actual chatbot
import json
import pickle
import numpy as np
import sys
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import actions
from dictionaries import cybersecurity, ccna
import random

subject = ""
function = "chat"

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
    global subject
    global function
    
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    
    for i in list_of_intents:
        #Is the tag a subject?
        if i["tag"] == tag:
            if i["tag"] == "cyber":
                subject = cybersecurity
            elif i["tag"] == "ccna":
                subject = ccna
              
        #Is the tag an action & has a subject been chosen?
            if ((i["tag"] == "flashcard") or (i["tag"] == "lookup")) and (subject == ""):
                result = "You haven't told me which subject you'd like to revise yet."
                break
        
            elif (i["tag"] == "lookup") and (subject != ""):
                result = "lookup"
                function = "action"
                break
        
            elif (i["tag"] == "flashcard") and (subject != ""):
                result = "flashcard"
                function = "action"
                break
        
        
        #Is the tag a normal response?
            else:
                result = random.choice(i['responses'])
                function = "chat"
                break
            
    return result

print("Violet is running. Say hello!")

while True:
    #chat mode
    while function == "chat":
        message = input("")
        ints = predict_class(message)
        res = get_response(ints, intents)
        if (res != "lookup") and (res != "flashcard"):
            print(f"\n{res}\n")
        break
        
    #action mode
    while function == "action":    
        if res == "lookup":
            actions.lookup(subject)
            function = "chat"
            break
            
        elif res == "flashcard":
            actions.flashcard(subject)
            function = "chat"
            break

