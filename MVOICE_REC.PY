import speech_recognition as sr
#import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("inisialization of Ninaja :")
    while True:
    
            #listen for the wake up my dear "ninja "
            # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognization....")
        try:
            with sr.Microphone() as source:
                print("keltide broo")
                audio = r.listen(source,)
            command  =r.recognize_google(audio)
            if(command.lower() =="jarvis"):
                speak("ya")
            #listen for command 
        except Exception as e:
                print(" error; {0}".format(e))