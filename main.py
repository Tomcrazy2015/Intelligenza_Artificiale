import random
import os.path
import datetime
import wikipedia
import pyautogui
from os import path
import webbrowser as wb
from requests import get
from module import volume
import speech_recognition as sr
from module import notifica as nof
from module import messaggio_whatsapp as mw

paths = {
    'opera': "C:\\Users\\aless\\AppData\\Local\\Programs\\Opera GX\\launcher.exe",
    'steam': "C:\\Steam\\Steam.exe",
    'pycharm': "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe",
    'multimc': "C:\\Users\\aless\Desktop\\Giochi Secondari\\MC\MultiMC\\MultiMC.exe",
    'bo3': "F:\\SteamLibrary\\steamapps\\common\\Call of Duty Black Ops III\\BlackOps3.exe",
    'new_world': "F:\\SteamLibrary\\steamapps\\common\\New World\\NewWorldLauncher.exe",
    'krunker': "C:\\KRUNKER\\Official Krunker.io Client\\Official Krunker.io Client.exe",
    'wallpaper_engine': "F:\\SteamLibrary\\steamapps\\common\\wallpaper_engine\\wallpaper64.exe",
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\aless\\AppData\\Local\\Discord\\Discord.exe",
    'calcolatrice': "C:\\Windows\\System32\\calc.exe"
}

##########Microfono###########
mic = sr.Recognizer()
##############################

def apri_opera():
    os.startfile(paths['opera'])
    nof("OPERA", "Apertura in corso di opera.")

def apri_steam():
    os.startfile(paths['steam'])
    nof("steam", "Apertura in corso di steam.")

def apri_pycharm():
    os.startfile(paths['pycharm'])
    nof("pycharm", "Apertura in corso di pycharm.")

def apri_multimc():
    os.startfile(paths['multimc'])
    nof("multimc", "Apertura in corso di multimc.")

def apri_bo3():
    os.startfile(paths['bo3'])
    nof("bo3", "Apertura in corso di bo3.")

def apri_new_world():
    os.startfile(paths['new_world'])
    nof("new_world", "Apertura in corso di new_world.")

def apri_krunker():
    os.startfile(paths['krunker'])
    nof("krunker", "Apertura in corso di krunker.")

def apri_wallpaper_engine():
    os.startfile(paths['wallpaper_engine'])
    nof("wallpaper_engine", "Apertura in corso di wallpaper_engine.")

def apri_notepad():
    os.startfile(paths['notepad'])
    nof("notepad", "Apertura in corso di notepad.")

def apri_discord():
    os.startfile(paths['discord'])
    nof("discord", "Apertura in corso di discord.")

def apri_calcolatrice():
    os.startfile(paths['calcolatrice'])
    nof("calcolatrice", "Apertura in corso di calcolatrice.")

def pausa():
    while True:
        nof("PAUSA","Sono in pausa")
        frase = comandi().lower()
        if "jarvis" in frase:
            break

def vol():
    quanto = volume()
    print("VOL")

    if "minimo" in voce:
        quanto.minimo()
        nof("Volume","Volume impostato al minimo.")

    elif "massimo" in voce:
        quanto.massimo()
        nof("Volume", "Volume impostato al massimo.")

    elif "alza" in voce:
        quanto.alza()
        nof("Volume", "Volume alzato.")

    elif "abbassa" in voce:
        quanto.abbassa()
        nof("Volume", "Volume abbassato.")

    elif "muta" in voce or "muto" in voce:
        quanto.muta()
        nof("Volume", "Volume mutato.")

    elif "smuta" in voce or "smuto" in voce:
        quanto.smuta()
        nof("Volume", "Volume smutato.")

    elif "normale" in voce:
        quanto.normale()
        nof("Volume", "Volume impostato al valore normale.")

def screenshots():
    i = 0
    if path.exists("C:\\Users\\aless\\Desktop\\PYTHON\\Intelligenza_Artificiale\\screen0.png"):
        for filea in os.listdir('C:\\Users\\aless\\Desktop\\PYTHON\\Intelligenza_Artificiale'):
            if filea.endswith(f'{i}.png'):
                if int(filea[-5]) == int(i):
                    i = i + 1
        print(i)
        image = pyautogui.screenshot()
        image.save(f"C:\\Users\\aless\\Desktop\\PYTHON\\Intelligenza_Artificiale\\screen{i}.png")
        nof("Screenshot", "Screenshot fatto.")
    else:
        image = pyautogui.screenshot()
        image.save("C:\\Users\\aless\\Desktop\\PYTHON\\Intelligenza_Artificiale\\screen0.png")
        nof("Screenshot", "Screenshot 0 fatto.")

def ora_attuale():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    nof("current_time", "")

def meteo():
    voce = None
    nof("Meteo", "Apertura in corso del meteo di Angera")
    wb.open_new_tab('https://www.ilmeteo.it/meteo/Angera')

def cmd():
    os.system("start cmd")
    nof("CMD", "Apertura in corso di CMD")

def mess_whatsapp():
    numw = voce[21:31]
    messw = voce[44:]
    nof(f'Invio messaggio al numero {numw}',f' Messaggio: {messw}')
    mess = mw(numw,messw)

    # manda un messaggio a sara con scritto ciao come stai

def comandi():
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source, duration=0.5)
        print("...")
        audio = mic.listen(source, phrase_time_limit=5)
    try:
        print("..")
        voce = mic.recognize_google(audio, language="it-IT")
    except Exception as e:
        print(".")
        return "None"
    return voce

i = 1
buongiorno_out = ["Buongiorno signore", "Buon pomeriggio signore", "Buona sera signore"]

while True:

    if i == 1:
        i = i + 1
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            buongiorno_out.remove("Buon pomeriggio signore")
            buongiorno_out.remove("Buona sera signore")
        elif hour >= 12 and hour < 17:
            buongiorno_out.remove("Buongiorno signore")
            buongiorno_out.remove("Buona sera signore")
        else:
            buongiorno_out.remove("Buongiorno signore")
            buongiorno_out.remove("Buon pomeriggio signore")
        print(random.choice(buongiorno_out))

    voce = None
    voce = input(":                 ").lower()
    print(voce)

    if "wikipedia" in voce and "jarvis" in voce:
        voce = voce.replace("jarvis", '')
        voce = voce.strip()
        print(voce)
        wikipedia.set_lang("it")
        print('Cerco su wikipedia...')
        voce = voce.replace("cerca su wikipedia", "")
        results = wikipedia.summary(voce, sentences=2)
        print("Questo è quello che sono riuscito a trovare su wikipedia..")
        print(results)
        voce = None

    elif "pausa" in voce and "jarvis" in voce:
        pausa()

    elif "volume" in voce or "muto" in voce or "smuta" in voce or "audio" in voce and "jarvis" in voce:
        vol()

    elif "meteo" in voce and "jarvis" in voce:
        meteo()

    elif "stop" in voce and "jarvis" in voce:
        exit()

    elif "apri" in voce and "jarvis" in voce:
        if "opera" in voce:
            apri_opera()
        elif "cmd" in voce:
            cmd()
        elif "steam" in voce:
            apri_steam()
        elif "pycharm" in voce:
            apri_pycharm()
        elif "multimc" in voce:
            apri_multimc()
        elif "bo3" in voce:
            apri_bo3()
        elif "new_world" in voce:
            apri_new_world()
        elif "krunker" in voce:
            apri_krunker()
        elif "wallpaper_engine" in voce:
            apri_wallpaper_engine()
        elif "notepad" in voce:
            apri_notepad()
        elif "discord" in voce:
            apri_discord()
        elif "calcolatrice" in voce:
            apri_calcolatrice()

    elif "che ore sono" in voce or "che ora è" in voce and "jarvis" in voce:
        ora_attuale()

    elif "screenshot" in voce or "screen" in voce and "jarvis" in voce:
        screenshots()

    elif "manda un messaggio" in voce and "jarvis" in voce:

        voce = voce.replace("jarvis", '')
        voce = voce.strip()

        if "richi" in voce:
            voce = voce.replace("richi", "3807883835")
            print(voce)

        elif "bonfo" in voce:
            voce = voce.replace("bonfo", "3802658021")
            print(voce)

        elif "cate" in voce:
            voce = voce.replace("cate", "3802323179")
            print(voce)

        elif "sara" in voce:
            voce = voce.replace("sara", "3713406245")
            print(voce)

        elif "anna" in voce:
            voce = voce.replace("anna", "3886443336")
            print(voce)

        mess_whatsapp()

    elif "ip" in voce and "jarvis" in voce:
        ip = get('https://api.ipify.org').text
        print(f"Questo è il tuo ip: {ip}")

