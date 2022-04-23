import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import request

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("What's up, it's your assistant, Peepeepoopoo")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language = "en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def send_email(content, to = "receiver_email_id"):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.startls()
    s.login("sender_email_id", "sender_email_id_password")
    message = content
    s.sendmail("sender_email_id", to, message)
    s.quit()

def news():
    x = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=122ff683cc0b4ff4a48a8c8718b11919").text
    y = json.loads(x)
    z = y.get("articles")
    for headlines in range(0,2):
        audio = z[headlines].get("descrpition")
        speak(audio)

if __name__ == "__main__":
    # speak("How may i help u?")
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching....")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia ")
            print(result)
            speak(result)

        elif "open google" in query:
            speak("Wait for a while...")
            webbrowser.open("https://google.com")

        elif "open youtube" in query:
            speak("Wait for a while...")
            webbrowser.open("https://youtube.com")

        elif "open stackoverflow" in query:
            speak("Wait for a while...")
            webbrowser.open("https://stackoverflow.com")

        elif "open code" in query:
            speak("Wait for a while...")
            path = "C:\\Users\\SHREYASH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "play music" in query:
            path = "C:\\shreyash\\"                                            #add directory of music
            music = os.listdir(path)
            os.startfile(os.path.join(path, music[0]))
            # mixer.init()
            # mixer.music.load("Song name")                                      # add song name
            # mixer.music.play()
            # takeCommand()
            # if takeCommand().lower()=="stop":
            #     mixer.music.stop()
            #     break

        elif "the time" in query:
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            speak(datetime.datetime.now().strftime("%H:%M:%S"))

        elif "send email" in query:                                                             # you have to allow less secure apps of gmail first
            try:
                speak("What's the message")
                content = takeCommand()
                send_email(content, to)
                speak("Your email has been sent successfully")
            except:
                speak("Sorry, email can not be sent due to some error")

        elif "read news" in query:
            speak("Today's headlines are")
            news()

        elif "exit" in query:
            speak("adios amigos, signing off")
            break

