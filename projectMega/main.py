import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open github" in c:
        webbrowser.open("https://github.com")
    else:
        speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    speak("Initializing jarvis................. ")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                command = r.recognize_google(audio)
                print(f"You said: {command}")
                if command.lower() == "jarvis":
                    speak("Ya")
                    print("Listening for your command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    user_command = r.recognize_google(audio)
                    print(f"Command: {user_command}")
                    processCommand(user_command)
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

















































