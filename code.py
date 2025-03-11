from multiprocessing.forkserver import main
from multiprocessing.spawn import _main
from threading import main_thread
from unittest.main import MAIN_EXAMPLES
import pyttsx3
from regex import W
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir')
    elif hour>=12 and hour<16:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')

    speak('I am JARVIS . An advance AI software system. PLease tell how may I help you')    

def takeCommand():     
     #it takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1  #seconds of non-speaking audio before a phrase is considered complete.
        audio = r.listen(source)


    try:
        print('Recognising...')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said:{query}\n')

    except Exception as e:
        #print(e)

        print('say that again please...')
        return 'None'    
        return query      

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')  #insert ur email_id and password here.
    server.sendmail('abc@gmail',to,content)     # inert the email of whome you have to send.        
    server.close()
if __name__ == "__main__":
    wishMe()
while True:
#if 1:
    query = takeCommand().lower()
        
    #logic for executing tasks based on query.
       
    if 'Wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query, sentences=2)
        speak('According to Wikipedia')
        print(results)
        speak(results) 
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'open github' in query:
        webbrowser.open('github.com')

    elif 'the time' in query:
        strline = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Sir,the time is{strline}')
    elif 'open code' in query:
        codePath = "<code path>"
        os.startfile(codePath)
    elif 'email to user' in query:
        try:
            speak('what should I say?')
            content = takeCommand()
            to = "abc@gmail.com"   #email_id of whome you have to send.
            sendEmail(to,content)
            speak('email has been sent')
        except Exception as e:
            print(e)
            speak('Sorry sir...unable to send email')
            

         
