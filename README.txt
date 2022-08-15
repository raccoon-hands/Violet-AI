VIOLET CHATBOT

Violet is a simple chatbot which uses neural networks and natural language processing
to try and return appropriate responses to natural speech, the way someone might over an
instant messenger. She was made using Neural Nine's tutorial [https://youtu.be/1lwddP0KUEg]
and then modified to work with up to date libraries, and execute certain functions.

For more information on neural networks and natural language processing, Neural Nine also has
some good videos introducing machine learning theory.

***Customising Violet's Responses***

The file "intents.json" contains everything that Violet is trained to respond to,
and every response that she can make, in the format of a dictionary.
"tag" refers to the topic of conversation- for example, greetings, or goodbyes.
"patterns" is where you can type examples of every phrase that you can think of
that falls into this "tag", and "responses" is where you enter the 
phrases that Violet should use to reply. You can add your own as long as you
pay attention to the dictionary format. You must run the file "train.py" before the
changes will take effect.

***Teaching Violet New Subjects***

New subjects can be added to Violet's repertoire in the form of python dictionaries,
in the file "dictionaries.py". 

1. Open dictionaries.py, and create a dictionary who's name is the name of the subject you want to add,
and then add as many entries as you like.
 
2. Open "chatbot-main.py" and find the function called
get_response(). Within this function there is a place to add your subject, just replace "subjectname"
with the name of your subject.

3. Open "intents.json" and add a new entry following the structure of the others. Make sure
you call the tag the same thing you replaced "subjectname" with in step 2. In "patterns", enter all the ways
you can think of to ask Violet to study your subject; use the "ccna" and "cyber" entries as templates.
You may enter a response similarly.

4. Open "train.py" and run it. Wait until it prints "done". It should now be ready!

Have fun playing around and don't be discouraged if it doesn't work straight away. Try adding your own functionalities to Violet! (Functions can be added to the file "actions.py". Examine the While loop at the end of chatbot_main.py
and see if you can figure out how to make her execute your functions.)

