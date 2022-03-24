import time
import pyautogui as pg
import webbrowser as web
from urllib.parse import quote
from plyer import notification
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pynput.keyboard import Key, Controller
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



class persone():
    def __init__(self,id):
        self.id = id

class notifica():
    def __init__(self,titolo_funzione,funzione):
        self.funzione = funzione
        self.titolo_funzione = titolo_funzione
        notification.notify(
            title = self.titolo_funzione,
            message = self.funzione,
            app_icon = None,
            timeout = 5,
        )

class volume():
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

    def minimo(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        quanto = -37
        volume.SetMasterVolumeLevel(quanto, None)

    def massimo(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        quanto = 0
        volume.SetMasterVolumeLevel(quanto, None)

    def alza(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        quanto = volume.GetMasterVolumeLevel()
        if quanto == 0:
            pass
        else:
            quanto = quanto + 1
            volume.SetMasterVolumeLevel(quanto, None)

    def abbassa(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        quanto = volume.GetMasterVolumeLevel()
        if quanto == -37:
            pass
        else:
            quanto = quanto - 1
            volume.SetMasterVolumeLevel(quanto, None)

    def muta(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(1, None)

    def smuta(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None)

    def normale(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(-19, None)

    def alza_20(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        quanto = volume.GetMasterVolumeLevel()
        if quanto > -8:
            pass
        else:
            quanto = quanto + 1
            volume.SetMasterVolumeLevel(quanto, None)

    def abbassa_20(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        quanto = volume.GetMasterVolumeLevel()
        if quanto < -29:
            pass
        else:
            quanto = quanto - 1
            volume.SetMasterVolumeLevel(quanto, None)



class messaggio_whatsapp():
    def __init__(self,id,messaggio):

        keyboard = Controller()

        self.id = id
        self.messaggio = messaggio

        web.open(f"https://web.whatsapp.com/send?phone=+39{id}&text={quote(messaggio)}")
        time.sleep(7)
        pg.click(-582, 1000)
        pg.press("enter")


