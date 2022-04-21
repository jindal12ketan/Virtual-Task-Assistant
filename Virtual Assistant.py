import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pandas as pd
import webbrowser
import os
import random as r
import smtplib
import requests
from bs4 import BeautifulSoup
import subprocess
import vlc
import weather_forecast as wf
from covid import Covid
from num2words import num2words as n2w
#===================Convert Number To Words=======================
def Words(num):
    words = n2w(num, lang='en_IN')
    return words
#===================Genrate State Data============================
def get_statedata(state):
    url = "https://www.mygov.in/covid-19"
    r = requests.get(url)
    web_cont = BeautifulSoup(r.text, 'lxml')
    web_cont = web_cont.find('div', {"class":"marquee_data view-content"})
    state_data = web_cont.find_all('div', {"class":"st_all_counts"})
    state_name = web_cont.find_all('span',{"class":"st_name"})
    All_state_data = []
    All_state_name = []
    for x in state_data:
        All_state_data.append(x.text.split())
    for x in state_name:
        All_state_name.append(x.text.lower())
    result = All_state_data[All_state_name.index(state)]
    dic = {'confirmed case' : Words(result[1].replace(',',"")),
    'active case' : Words(result[3].replace(',',"")),
    'recovered case' : Words(result[5].replace(',',"")),
    'dead case' : Words(result[7].replace(',',"")),
    'vaccination' : Words(result[9].replace(',',""))}
    return dic
#============================================================================================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)
#==========================================
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#==========================================
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me How may I help you")
#=================================================================
def takeCommand():
    #it take voice from the user and return the string output to the user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 1200
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"Sir, said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        return "None"
    return query
#==============================================================
password = 'ketan@123jindal'
#==============================================================
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jindal.2002ketan@gmail.com',password)
    server.sendmail('jindal.2002ketan@gmail.com', to, content)
    server.close()
#==============================================================
my_dict = {"ketan" : "jindal.2002ketan@gmail.com" , "papa" : "manojjindal2000@gmail.com", "aman patiyale" : "amanpatyal79@gmail.com"}

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        #Logic of tasks based on query
        if "wikipedia" in query:
            speak('Searching wikiedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 6)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        #================================
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        #================================
        elif "open google" in query:
            webbrowser.open("google.com")
        #================================
        elif "play" and "music" in query:
            speak("Sir, Any Random or yours Favorite")
            if ("random") in takeCommand().lower():
                try:
                    music_dir = 'F:\songs'
                    songs = os.listdir(music_dir)
                    #os.startfile(os.path.join(music_dir, songs[r.randrange(0,len(songs))]))
                    p = vlc.MediaPlayer("F:\\songs\\" + songs[r.randrange(0,len(songs))])
                    p.play()
                    if "play" in query:
                        p.play()
                    elif "pause" in query:
                        p.pause()
                    elif "stop" in query:
                        p.pause()               

                except Exception as e:
                    print(e)
                    speak("Sorry Sir. I am not able to find result")
            else:
                try:
                    speak('which song sir?')
                    play = takeCommand().lower()
                    p = vlc.MediaPlayer("F:\\songs\\" + play + ".mp3")
                    p.play()
                except Exception as e:
                    print(e)
                    speak("Sorry Sir. I am not able to play")
        #================================
        elif "play my favourite song" in query:
            music_dir = 'E:\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[47]))
        #================================
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        #================================
        elif "open code" in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        #================================
        elif "open firefox" in query:
            codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePath)
        #================================
        elif "send email" in query:
            try:
                speak("To whom sir?")
                to = my_dict[takeCommand().lower()] 
                speak("What should I say ?")
                content = takeCommand()
                speak(f"Email is sending to {to}")
                sendEmail(to,content)
                speak("Email has been sent!, Sir")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send Email")
        #================================
        elif "open calculator" in query:
            codePath = "C:\\Windows\\System32\\calc.exe"
            subprocess.Popen(codePath)
        #================================
        elif "open microsoft apps" in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
            os.startfile(codePath)
        #================================
        elif "open camera" in query:
            subprocess.run("start microsoft.windows.camera:", shell=True)
        #================================
        elif "covid" in query:
            speak("Sir, Country Or State")
            if "country" in takeCommand().lower().split():
                try:
                    speak("Which Country sir?")
                    country = takeCommand().lower()
                    covid = Covid()
                    cases = covid.get_status_by_country_name(country)
                    dic1 = {"Confirmed case" : Words(cases["confirmed"]), "Active case" : Words(cases["active"]), "Recovered cases" : Words(cases["recovered"]),"Death case" : Words(cases["deaths"])}
                    dic1 = str(dic1)
                    print(dic1)
                    speak("In" + country + "..." + dic1)

                except Exception as e:
                    print(e)
                    speak("Sorry Sir. I am not able to find result")
            else:
                try:
                    speak("Which State sir?")
                    state = takeCommand().lower()
                    cases = get_statedata(state)
                    print(cases)
                    speak("In" + state + "..." + str(cases))

                except Exception as e:
                    print(e)
                    speak("Sorry Sir. I am not able to find result")
        #================================
        elif "weather" in query:
            try:
                speak('weather of which place sir?')
                place1 = takeCommand().lower()
                d = wf.forecast(place = place1)
                dayt = str(d['day']['temperature'])
                nightt = str(d['night']['temperature'])
                place = d['place']
                speak(f"in {place} day's temprature is {dayt} degree celcius and night's temprature is {nightt} degree celcius")

            except Exception as e:
                print(e)
                speak("Sorry Sir,I am not able to tell")
        #================================
        elif "play my movie" in query:
            try:
                speak('which movie sir?')
                play = takeCommand().lower()
                p = vlc.MediaPlayer("C:\\Users\\HP\\Desktop\\movies\\" + play + ".mkv")
                p.play()

            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to play")
        #================================
        # elif "play" in query:
        #     p.play()
        # #================================
        # elif "pause" in query:
        #     p.pause()
        # #================================
        # elif "stop" in query:
        #     p.stop()
        #================================
        elif "quit" or "exit" in query:
            speak("Thankyou Sir,") 
            quit()     