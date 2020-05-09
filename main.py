import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir Have Your Tea Or Coffee!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir Have Your Lunch!")   

    else:
        speak("Good Evening Sir,Have Your Snacks or not!")  

    speak("I am Your Personal Assistant Himanshu sir. How may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening You Sir......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Tyr To Gotting...")    
        query = r.recognize_google(audio, language='en-in')
        print("Himanshu Sir said: {query}\n")

    except Exception as e:
          
        print("Please Say That Again Sir...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('golashhimanshu4@gmail.com', 'password')
    server.sendmail('golashhimanshu4@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching From Very Intelligent Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("As  Wiki Says...")
            print(results)
            speak(results)

        elif 'open my google' in query:
            webbrowser.open("www.google.com")

        elif 'open my youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open my hackerrank profile ' in query:
            webbrowser.open("www.hackerrank.com/golashhimanshu4")   


        elif 'play music  My PA' in query:
            music_dir = 'C:\Users\Public\Music\Sample Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'Tell me the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Himanshu Sir, the time is {strTime}")

        elif 'email to Himanshu' in query:
            try:
                speak("What should be in email Sir ?")
                content = takeCommand()
                to = "golashhimanshu4@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent Successfully to You Sir!")
            except Exception as e:
                print(e)
                speak("Sorry Himanshu Sir. I am not able to send this email to anyone.")  