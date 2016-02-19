import speech_recognition as sr
import pyttsx


engine = pyttsx.init()
engine.setProperty('rate', 70)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("V�r stille")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Sett energi grense til {}".format(r.energy_threshold))
    while True:
        print("Si noe!")
        with m as source: audio = r.listen(source)
        print("Vent litt")
        try:
            # Bruk google for � kjenne igjen lyden
            value = r.recognize_google(audio)

            # Omgj�r og printer utf kode til output
            if str is bytes:
                print(u"You said {}".format(value).encode("utf-8"))
                engine.say('Hello Sjur, how are you today?')
                engine.runAndWait()
            else:
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Si det igjen")
        except sr.RequestError as e:
            print("Oi, kan ikke kontakte google, pr�v igjen; {0}".format(e))
    
except KeyboardInterrupt:
    pass