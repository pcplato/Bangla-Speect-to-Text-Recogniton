import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("শুনছি...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("অনুমান করছি...")
        query = r.recognize_google(audio, language='BN')
        print(f"তুমি বলেছিলে: {query}\n")

    except Exception as e:
        print(e)
        print("দুঃখিত আমি বুঝতে পারছি না")
        return "None"

    return query

if __name__ == '__main__':
    while True:
        query = takeCommand()

