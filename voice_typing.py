import datetime
import speech_recognition as sr
import pyttsx3, sys

def speak():
    robot = pyttsx3.init()
    robot.say("Welcome to voice typing. You will say & I will recognize it & save it to a file name activity.txt. So, let's get started")
    robot.setProperty('rate', 180)
    robot.setProperty('voice', 0.9)
    robot.runAndWait()
    
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Didn't hear properly :(" )
    return said


def save_file(user_input):
    with open("activity.txt", mode="a") as activity_file:
        activity_file.write(user_input + ". ")
        activity_file.close()
       


speak()
while True:
    user_input = get_audio()
    if user_input == "stop":
        sys.exit()
    save_file(user_input)
