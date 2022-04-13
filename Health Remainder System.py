
from pygame import mixer
from time import time
import datetime

def playmusic(alarm, stop):
    mixer.init()
    mixer.music.load(alarm)
    mixer.music.play()
    while True:
        inp = input(f"Enter {stop} to stop the alarm")
        if inp == f"{stop}":
            mixer.music.stop()
            break

def log_details(text):
    with open("log.txt", "a") as f:
        f.write(f"{text} {datetime.datetime.now()}\n")

if __name__ == '__main__':
    eyetime = time()
    watertime = time()
    exercise = time()
    water_break = 13    #40*60
    eye_break = 23  #30*60
    exercise_break = 29 #50*60
    a = datetime.datetime.now()
    print("------------Health Remainder System----------")
    while True:#a.hour>9 and a.hour<17:
        if time()-eyetime>eye_break:
            print("It's time to give eyes some rest")
            playmusic("mixkit-facility-alarm-sound-999.wav", "eyedone")
            eyetime = time()
            log_details("Relaxed eyes at")

        if time()-watertime>water_break:
            print("It's time to drink water and stay hydrated")
            playmusic("mixkit-morning-clock-alarm-1003.wav", "waterdone")
            watertime = time()
            log_details("Drank water at ")

        if time()-exercise>exercise_break:
            print("It's time for you to exercise and stay fit")
            playmusic("mixkit-warning-alarm-buzzer-991.wav", "pydone")
            exercise = time()
            log_details("Did exercise at ")

