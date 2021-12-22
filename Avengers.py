#!/usr/bin/env python
# coding: utf-8

# In[1]:


QuestionsData = {'Questions':{1:'Are you from earth?', 
                          2:'Are you male?', 
                          3:'Are you with the avengers', 
                          4:'Do you have superpowers?',
                          5:'Are you a god?'},
             'Points':[1,2,4,8,16]
            }


# In[2]:


CharactersData = {'Characters':['Hulk', 'Groot', 'Thanos', 'Natasha', 'Odin'],
         'Scores':[15, 12, 2, 5, 30]}


# In[3]:


Answers = ['Yes', 'Yes', 'Yes', 'No', 'No']


# In[4]:


def Calculate(Answers, CharactersData, QuestionsData):
    score = 0
    for i in range(0,len(Answers)):
        if Answers[i] == 'Yes':
            score = score + QuestionsData['Points'][i]
    checker = 0
    for i in range(0, len(CharactersData['Scores'])):
        if CharactersData['Scores'][i] == score:
            checker = 1 
            return(CharactersData['Characters'][i])
    if checker == 0:
        return("No character found")


# In[5]:


Calculate(Answers, CharactersData, QuestionsData)

