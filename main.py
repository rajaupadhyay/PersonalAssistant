import speech_recognition as sr
import nltk
import subprocess

# This is so much simpler
def active_listen():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        audio = r.listen(src)
    msg = ''
    try:
        msg = r.recognize_google(audio)
        print(msg.lower())
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google STT; {0}".format(e))
    except:
        print("Dude you messed up!")
    finally:
        return msg.lower()


message = active_listen()
print(message)

tokens = nltk.word_tokenize(message)
print(tokens)

if "open" and "chrome" in tokens:
    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Google Chrome.app"])

