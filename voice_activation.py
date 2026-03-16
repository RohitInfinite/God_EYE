import speech_recognition as sr
import time

start_callback = None
stop_callback = None


def set_callbacks(start_fn, stop_fn):

    global start_callback, stop_callback

    start_callback = start_fn
    stop_callback = stop_fn


def listen():

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:

        try:

            with mic as source:

                recognizer.adjust_for_ambient_noise(source)

                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio).lower()

            print("Heard:", text)

            if "hey god" in text:

                if start_callback:
                    start_callback()

            if "stop navigation" in text:

                if stop_callback:
                    stop_callback()

        except:
            pass

        time.sleep(1)