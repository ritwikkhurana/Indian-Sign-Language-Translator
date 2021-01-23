# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:52:05 2019

@author: ritwi
"""

import speech_recognition as sr
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pyglet 


arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']

gif = ['address','all', 'any questions', 'are you angry', 'are you hungry', 'assam','august','banana','banaras','banglore','be careful','bridge',
              'cat','christmas','church','cilinic','dasara','december', 'did you finish homework', 'do you have money',
                'do you want something to drink', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good morning', 'good question','grapes',
                'hindu','i am a clerk', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i go to a theatre',
                'i had to say something but i forgot',  'i like pink colour', 'i love to shop','job','krishna','lets go for lunch', 'mango', 'mile', 
                'nice to meet you',  'open the door',  'please call me later', 'police station','post office',
                'shall I help you',
                'shall we go together tommorow', 'shop','sign language interpreter', 'sit down', 'stand up', 'take care', 'temple', 'there was traffic jam', 'toilet','tomato','village',
                 'what is the problem', 'what is todays date', 'what is your father do', 
                 'what is your name', 'whats up',
                'where is the bathroom', 'where is the police station', 'you are wrong']
        

m = sr.Recognizer()

i = int(input('press 1 if you want to give live speech and 2 if you want to upload an audio file : '))

get = []
text = []

if (i == 1) :
    with sr.Microphone() as source:
      m.adjust_for_ambient_noise(source)
      print('Say Something')
      get = m.listen(source)
    try:
      text = m.recognize_google(get)
      print('you said ' + text)
           
    except Exception:
        print('Could not recognise')
        
   
     
        
elif (i == 2):
    audio  = input('Write the name of the audio fle you want to upload with extension : ')
    location = 'C:\\Users\\ritwi\\Documents\\Python' + audio 
    
    with sr.AudioFile(location) as source:
      get = m.record(source)
    try:
      text = m.recognize_google(get)
      print(text)
        
    except Exception:
      print('Something went wrong')
      
else:
    print('incorrect input')      
        
if(text in gif):
  add = 'ISL_Gifs\\' + text + '.gif'
  animation = pyglet.image.load_animation(add)
  sprite = pyglet.sprite.Sprite(animation)

  w = sprite.width
  h = sprite.height

  window = pyglet.window.Window(width=w,height=h)

  @window.event
  def on_draw():
    sprite.draw()

  pyglet.app.run()

else:
  for i in range(len(text)):
          if (text[i] in arr):
            address = 'letters\\' + text[i] + '.jpg'
            try:
               Img = Image.open(address)
               Img1 = np.asarray(Img)
               plt.imshow(Img1)
               plt.pause(0.1)
               
            except Exception as e:
                print(e)
          elif (text[i] == ' '):
              plt.close()
              plt.pause(0.2)
          else:
              continue
             
