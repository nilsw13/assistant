import tkinter as tk
import datetime
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import wikipedia

wikipedia.set_lang('fr')

root = tk.Tk()
root.config(bg='#046285')
root.title('Assistant Vocal')
root.minsize(560, 360)


frame = tk.Frame(root, bg='#046285')
frame.pack(expand=True)

width = 500
height = 480
image = tk.PhotoImage(file="assistant-vocal.png")
canvas = tk.Canvas(frame, height=height, width=width, bg='#046285', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=True)



prise_audio = sr.Recognizer()
engine = ttx.init()
voix_assistant = engine.getProperty('voices')
voix_assistant = engine.setProperty('voice', 'french')


def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voix = prise_audio.listen(source)
            prise_audio.adjust_for_ambient_noise(source)
            command = prise_audio.recognize_google(voix, language='fr-FR',)
            return command
    except:
        return ''


def lancer_assistant():
    while True:
        command = ecouter()

        if "arrête" in command or "quitte" in command:
            break

        if 'poto' in command:
            text = "Bonjour que puis-je faire pour vous ?"
            parler(text)
        else:
            pass

        if "joue la musique" in command:
            text = "ok! je"
            musique = command.replace('', "")
            print(musique)
            pywhatkit.playonyt(musique)
            parler(text)
            parler(musique)
        else:
            pass

        if "heure" in command:
            heure = datetime.datetime.now().strftime("%H/%M")
            parler("il est" + heure)
        else:
            pass

        if "cherche" in command:
            text = "ok, je cherche un résumé de "
            recherche = command.replace('cherche', '').strip()
            parler(text + recherche)
            result = wikipedia.summary(recherche, sentences=5)
            parler(result)
        else:
            pass


label_title = tk.Label(frame, text='Bievenue sur vôtre assistant vocal', font=('Courrier', 20), fg='white', bg='#046285')
label_title.pack()

button_start = tk.Button(frame, bg='#046285', text='Démarrer', fg='black', pady=10, padx=250, command=lancer_assistant)
button_start.pack()

root.mainloop()
