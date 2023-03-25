# A.I.D.A Project

import os
import pyttsx3
import speech_recognition as sr
import openai
import env

#Key for OpenAI
openai.api_key = env.OPEN_AI_KEY

# init for the speech engine

engine = pyttsx3.init()

def speak(word):
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 0.8)
    
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    
    engine.say(str(word))
    engine.runAndWait()
    engine.stop()
    
#init for the speech recon

rec = sr.Recognizer()
speak('Hello sir, I am at your disposal')
with sr.Microphone() as src:
    audio = rec.listen(src)
    speak('Just a moment sir')
    
text = rec.recognize_google(audio)
disc = openai.Completion.create(prompt=text, engine='text-davinci-003', max_tokens=1000,)

answer = disc.choices[0].text

if answer:
    speak(answer)









