import pyttsx3
import threading


def speak(text):

    def run():

        try:
            engine = pyttsx3.init()

            engine.setProperty("rate", 170)

            engine.say(text)

            engine.runAndWait()

            engine.stop()

        except:
            pass

    threading.Thread(target=run, daemon=True).start()