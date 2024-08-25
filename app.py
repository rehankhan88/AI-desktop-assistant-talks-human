
import speech_recognition as sr
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        r.pause_threshold = 1  # Pause threshold before assuming user is done speaking
        print("Listening...")
        try:
            audio_data = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio_data, language="en-PK")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am AI")
    print("Listening...")
    text = takeCommand()
    if text:
        say(text)
