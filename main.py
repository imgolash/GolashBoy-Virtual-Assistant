import os
import pyautogui as him2
import pyttsx3 
import pywhatkit as him
import speech_recognition as him1
import wikipedia 
import webbrowser
import smtplib
import datetime
import folium  
import cv2
import pytube  
from pytube import YouTube  
import numpy as np


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Himanshu Sir, Have Your Tea Or Coffee!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Himanshu Sir, Have Your Lunch or not!")   

    else:
        speak("Good Evening Himanshu Sir ,Have Your Snacks or not!")  

    speak("I am MALGO Your Personal Assistant Sir. How may I help you")       

def Command():
    

    r = him1.Recognizer()
    with him1.Microphone() as source:
       r.adjust_for_ambient_noise(source,duration=4)
       print("Listening You Sir......")
       speak("Listening You Sir......")
       r.pause_threshold = 0.6
       audio = r.listen(source)

    try:
        print("Trying to understand...")
        speak("Trying to understand...")    
        query = r.recognize_google(audio, language='en-in').lower()
        print("Ok Sir :-)\n")
        speak("Ok Sir \n")

    except Exception as e:
        
        print(e)
        print("Please Say That Again Sir...")
        speak("Please Say That Again Sir...")  
        return "None"
    return query

def Email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('golashhimanshu4@gmail.com', 'password')
    server.sendmail('golashhimanshu4@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    greet()
    while (True):

        query = Command().lower()
       
        if 'Tell Me About ' in query:
            speak('Searching From Internet...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("As Internet Says...")
            print(results)
            speak(results)

        elif 'open my google' in query:
            webbrowser.open("www.google.com")
            print("Opening Google")
            speak("Opening Google")
           
            
            
        elif 'send whatsapp to me' in query:
            him.sendwhatmsg("+919634470602","Hi sir how are you?",17,40)
            print("Sending Whatsapp Message")
            speak("Sending Whatsapp Message")
            
         
        elif 'Map current location' in query:
            curr_map=folium.Map(location=[27.1843328,77.98784]).save("E:\\TEST\\him.html")
            webbrowser.open("E:\\TEST\\him.html")
            print("Done Sir")
            speak("Done Sir")
                          
        elif 'open my youtube' in query:
            webbrowser.open("www.youtube.com")
            print("Done Sir")
            speak("Done Sir")
            

        elif 'open my github ' in query:
            webbrowser.open("www.github.com")  
            print("Done Sir")
            speak("Done Sir") 

        elif 'open image MALGO' in query:
            image_dir = "C:\\Users\\GOLASHBOY\\Pictures\\Camera Roll"
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))
            print("Done Sir")
            speak("Done Sir")

        elif 'Tell me the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

        elif 'email to Sir' in query:
            try:
                speak("What should be in email Sir ?")
                content = Command()
                to = "golashhimanshu4@gmail.com"    
                Email(to, content)
                speak("Email has been sent Successfully to You Sir!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email to anyone.")  
