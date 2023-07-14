from newspaper import Article
import random
import string

import nltk
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')
nltk.download('punkt', quiet=True)
myArticle=Article('https://my.clevelandclinic.org/health/diseases/21214-coronavirus-covid-19')

myArticle.download()
myArticle.parse()
myArticle.nlp()
myCorpus=myArticle.text

##print(myCorpus)
#Tokenization
my_text=myCorpus
my_sentence_list=nltk.sent_tokenize(my_text)


#A customer function for to return a random greetings response from the users greetings
#print(my_sentence_list)
def greeting_response(my_text: str):
    my_text=my_text.lower()
    
    #Bot greetings response
    my_bot_greetings=['Hello', 'Hi', 'Hey', 'Hola']
    #user greetings
    my_greetings=['Hi', 'Hello', 'Greetings', 'Whatup', 'Hi there']
    
    for word in my_text.split():
        if word in my_greetings:
            return random.choice(my_bot_greetings)
        
        
def index_sort(list_var):
    length=len(list_var)
    list_index=list(range(0, length))
    
    x=list_var
    
    for i in range(length):
        for j in range(length):
            if x[list_index[i] > x[list_index][j]]:
                #swap
                temp=list_index[i]
                list_index[i]=list_index[j]
                list_index[j]=temp
        
        return list_index
#my bot response
def bot_response(user_input: str):
    user_input = user_input.lower()
    my_sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(my_sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    
    index = index[1:]
    response_flag = 0
    
    k = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + my_sentence_list[index[i]]
            response_flag = 1
            i = i + 1
            
        if k > 2:
            break
    
    if response_flag == 0:
        bot_response = bot_response + " I apologize, I don't understand."
       
    my_sentence_list.remove(user_input)
    
    return bot_response  # Add this line to ensure a string is always returned




print('Dr Bot : I am Bot or Doc Bot for short. I will answer your queries about Kidney Disease.\nMay you want to exit, type bye')

exit_list=['exit', 'see you later', 'bye', 'quit', 'break']
while (True):
    user_input=str(input())
    if user_input.lower() in exit_list:
        print('Dr Bot: Chat you later!')
        break
    
    else:
        
     if greeting_response(user_input) != None:
        print('Dr Bot: ' + greeting_response(user_input))
     else:
         print('Dr Bot: ' + bot_response(user_input))
         
    