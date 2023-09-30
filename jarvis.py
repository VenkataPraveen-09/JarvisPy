from platform import release
from re import search
from time import sleep
from numpy.core.fromnumeric import take
import pyttsx3
import datetime
from playsound import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import speedtest
import instaloader
import pywhatkit
import webbrowser as web
import time
import keyboard
from pywhatkit import sendwhatmsg
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from pywikihow import search_wikihow 
from bs4 import BeautifulSoup



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour< 12:
        print("Good Morning sir!")
        speak("Good Morning sir!")
    elif hour>=12 and hour< 18:
        print("Good afternoon sir!")
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        print("good Evening sir")
        speak("good Evening sir")
    else:
        print("Good Night sir!")
        speak("Good Night sir!")

    speak("Jarvis at your service. Please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"User said: {query}")
                               
    except Exception as e:
        #print(e)
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query
   
#pywhatkit.sendwhatmsg('+918639438394','Hello this is jarvis',1,22)           
def whatsapp(number,message):
    number = '+91' + int(num)
    message = message
    open_chat = "https://web.whatsapp.com/send?photo=" + number + "&text=" + message
    web.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')

def whatsapp_grp(group_id, message):
    open_chat = "https://web.whatsapp.com/accept?code=" + group_id
    web.open(open_chat)
    time.sleep(10)
    click(x=739, y=1044)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')

def YoutubeAuto(command):
    query = str(command)

    if 'pause' in query:
        press('space bar')

    elif 'resume' in query:
        press('space bar')

    elif 'full screen' in query:
        press('f')

    elif 'film screen' in query:
        press('t')

    elif 'skip 10 seconds' in query:
        press('l')
    
    elif 'back 10 seconds' in query:
        press('j')

    elif 'mute' in query or 'unmute' in query:
        press('m')

    elif 'increase' in query:
        press_and_release('shift + .')

    elif 'decrease' in query:
        press_and_release('shift + ,')

    elif 'previous' in query:
        press_and_release('shift + p')

    elif 'next' in query:
        press_and_release('shift + n')

    elif 'search' in query:
        click(x=567, y=556)
        speak("what to search ?")
        search = takeCommand()
        write(search)
        sleep(0.8)
        press('enter')
sleep(2)
YoutubeAuto('')

##def YoutubeSearch(term):
    #result = "https://www.youtube.com/results?search_query=" + term
    #web.open(result)
    #speak("This is what i found for your search sir")
    #pywhatkit.playonyt(term)
    #speak("This may also help you sir")
#YoutubeSearch('mr mowa bro')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gopthreya123@gmail.com', 'gopthreya45321gmail')
    server.sendmail('gopthreya123@gmail.com', to, content)
    server.close()
   
if __name__ == "__main__": 
    wishMe()
      
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            sleep(10)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube...") 
            print("Opening Youtube...")
            sleep(10)
      
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening google...")
            print("Opening Google...")
            sleep(10)

        elif 'search stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            print("opening stackoverflow")
            speak("Opening stackoverflow")
            sleep(10)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\S GOPTHREYA KUMAR\\Music' 
            songs = os.listdir(music_dir)
            speak("playing Music")
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))        
            print("\nplaying Music...")
            sleep(10)
                          
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir, the time is {strTime}")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\S GOPTHREYA KUMAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Code")
            print("Opening code...")
            sleep(10)

        elif 'open powerpoint' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)
            speak("Opening powerpoint")
            print("Opening powerpoint...")
            sleep(10) 

        elif 'open word office' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
            print("Opening word office...") 
            speak("Opening word office")
            sleep(10)
            
        elif 'open python ide' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)
            print("Opening pycharm...")
            speak("Opening pycharm")
            sleep(10)
            
        elif 'open outlook' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe" 
            os.startfile(codePath)
            speak("Opening outlook")
            print("Opening outlook...")

        elif 'open edge' in query:
            codePath = "C:\\Program Files (x86)\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
            print("Opening edge...")
            speak("Opening edge")
            sleep(10)

        elif 'youtube search' in query :
            print("what to search")
            speak("what to search")
            result = "https://www.youtube.com/results?search_query=" + takeCommand()
            web.open(result)
            speak("This is what i found for your search sir")
            sleep(10)
            speak("Next command sir...")
            
        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            print(f"Sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
           # try:
            #    os.system('cmd /k "speedtest"')
            #except:
             #   speak("there is no internet connection")

        elif 'alarm' in query:
            speak("Say the time: ")
            time = takeCommand() 
            speak("Alarm has been set sir")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H%M")

                if now == time:
                    speak("Time to Wake Up sir")
                    #playsound("C:\\Users\\S GOPTHREYA KUMAR\\Arjun Reddy.mp3")
                    speak("Alarm Closed!")
                elif now>time:
                    break
                else:
                    print("Next command...")
                    speak("Next command...")

        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gopthreya000@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Hello Gopthreya how r u, Iam 5n, this is from Jarvis")
                sleep(10)
    
        elif "temperature" in query:
            search = "Temperature in Hyderabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"current {search} is {temp}")
            speak(f"current {search} is {temp}")
            sleep(5)

        elif "instagram profile" in query:
            print("If you want to speak! say yes, or you want to give input! say no")
            speak("If you want to speak! say yes, or you want to give input! say no")
            condition1 = takeCommand().lower()
            if 'yes' in condition1:
                print("Please say the User name...")
                speak("Please say the User name...")
                name = takeCommand().lower()
            else:
                speak("Enter Username here")
                name = input("Enter Username here:")   

            webbrowser.open(f"www.instagram.com/{name}")
            sleep(10)          
            speak("Sir would you like to download profile picture of this account.")
            condition2 = takeCommand().lower()
            if 'yes' in condition2:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only = True)
                print('I am done sir, profile picture is saved in our main folder...')
                speak('I am done sir, profile picture is saved in our main folder...')
            else:
                pass
            sleep(10)

        elif 'google search ' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This is what i found on web!")
            pywhatkit.search(query)
            try:               
                result = googleScrap.summary(query,3)
                print(result)
                speak(result)
                sleep(10)
            except:
                speak("No Speakable data Available!")

        elif 'whatsapp message' in query:
            query = query.replace("jarvis","")
            query = query.replace("send","")
            query = query.replace("whatsapp message","")
            query = query.replace("to","")
            name = query
            
            if 'best friend' in name:
                num = "6303 177 679"
                speak("what message should i sent for {name}")
                message = takeCommand()
                whatsapp.whatsapp(num,message)

            elif 'dad' in name:
                num = "8688023233"
                speak("what message should i sent for {name}")
                message = takeCommand()
                whatsapp(num,message)

            elif 'friends' in name:
                group = "JOZ3yPo3Qiz0GN1YREggty"
                speak(f"what message should i sent for {name}")
                message = takeCommand()
                whatsapp_grp(group,message)
                
        elif 'search on chrome' in query:
            speak("what should i search sir")
            search = takeCommand()
            chromepath =  "C://Program Files//Google//Chrome//Application//chrome.exe %s"
            webbrowser.get(chromepath).open_new_tab(search) 
            print("\nopening "+search)
            speak("opening "+search)
            sleep(10)
            speak("next command")

        elif 'enter the meeting' in query:
             Link = "https://meet.google.com/fum-qokb-uhm"
             print(Link)
             web.open(Link)
             sleep(5)

             click(x=433, y=608)
             sleep(2)

             click(x=534, y=613)
             sleep(2)

             click(x=362, y=899)
             print("Class joined sir")
             speak("Class joined sir")

        elif 'where i am' in query or 'where we are' in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
               # print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                print(f'sir iam not sure, but i think we are in {city} in {country} country')
                speak(f'sir iam not sure, but i think we are in {city} in {country} country')
            except Exception as e:
                print("sorry sir, due to network issue i am not able to find where we are...")
                speak("sorry sir, due to network issue i am not able to find where we are...")
                pass 

        elif "open how to do mode" in query:
            print("Opening how to do mode, Tell me what you want to know")
            speak("Opening how to do mode, Tell me what you want to know")
            how = takeCommand()
            try:
                if "exit" in how or "close" in how:
                    speak("okay sir, how to do mode is closed")
                    break
                else:
                     max_results = 1
                     how_to = search_wikihow(how, max_results)
                     assert len(how_to) == 1
                     how_to[0].print()
                     speak(how_to[0].summary) 
            except Exception as e:
                print("sorry sir, i am not able to find this...")
                speak("sorry sir, i am not able to find this...")

        elif 'you can sleep' in query or 'sleep now' in query:
            print("okay sir, i am going to sleep you can call me anytime...")
            speak("okay sir, i am going to sleep you can call me anytime...")
            break
        
        elif "stop" in query:
            print("okay sir")
            speak("okay sir")
            break


                     
           

            
        


      

   

    



       




