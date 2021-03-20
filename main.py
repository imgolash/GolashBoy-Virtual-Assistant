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
import requests
import rotatescreen
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Himanshu Sir, Did You Have Your Tea Or Coffee!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Himanshu Sir, Did You Have Your Lunch!")   

    else:
        speak("Good Evening Himanshu Sir, Did You Have Your Snacks!")  

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

       
        if 'wikipedia' in query:
            speak('What do you want to search from Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("As Internet Says...")
            print(results)
            speak(results)

        elif 'open my google' in query:
            webbrowser.open("www.google.com")
            
        elif 'take screenshot'in query:
            SS = him2.screenshot()
            SS.save(r'D:\test\pic2.png')
            print("Screenshot Saved Himanshu Sir")
            speak("Screenshot Saved Himanshu Sir")   
            
        elif 'send whatsapp to me' in query:
            him.sendwhatmsg("+919634470602","Hi Sir Good Afternoon?",14,23)
        
        elif 'rotate' in query:
            print("I am rotating your screen")
            speak("I am rotating your screen")
            screen = rotatescreen.get_primary_display()
            for i in range(100):
                time.sleep(1)
                screen.rotate_to(i*90%360)
        
         
        elif 'Map current location' in query:
            curr_map=folium.Map(location=[27.1843328,77.98784]).save("him.html")
            webbrowser.open("him.html")
        
        elif 'My state cases' in query:
            state = 'Uttar Pradesh'.upper()
            api_used = "https://api.covid19india.org/data.json"
            json_data = requests.get(api_used).json()
            
            arr = range(0,30)
            for n in arr:
                if state == json_data['statewise'][n]['state'].upper():
                    Total_Case = json_data['statewise'][n]['confirmed']
                    n+= 1
                    print(f"Active Case in {state} is {Total_Case}")
                    speak(f"Active Case in {state} is {Total_Case}")

                          
        elif 'open my youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open my github ' in query:
            webbrowser.open("www.github.com")   


        elif 'open image' in query:
            image_dir = "D:\\test\\pic1.png"
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))

        elif 'time' in query:
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
