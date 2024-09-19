# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:42:44 2024

@author: sanih
"""

from openai import OpenAI
client = OpenAI() 

messages = [ {'role':'system', 'content':"You are a Math Tutor"}]
user_messages = ['Explain what is PI', 'Summarize this in two bullet points']

for each_message in user_messages:
    user_dict = {'role': 'user', 'content':[{'type': 'text', 'text': each_message}]}
    messages.append(user_dict)
    
    response = client.chat.completions.create(
               model="gpt-3.5-turbo",
    messages=messages)
    
    assist_dict ={'role':'assistant', 'content': [{'type': 'text', 'text': response.choices[0].message.content}]}
    messages.append(assist_dict)
    
    print(response.choices[0].message.content)
