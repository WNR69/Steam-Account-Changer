from configparser import ConfigParser
import webbrowser
import PySimpleGUI as sg
import psutil
import subprocess


config = ConfigParser()
config.read("config.cfg")
keyboard_key = config["settings"]["keyboard_key"]
now_account = config["temp"]["temp"]
file_location = config["settings"]["file_location"]
process_name = config["settings"]["process_name"]
process_location = config["settings"]["process_location"]
font = ('Courier New', 11, 'underline')
sg.theme("Dark")

layout = [[sg.Push(), sg.Text("Steam Account Changer", font='Any 15', ), sg.Push()],
          [sg.Text("Account Text File"),
           sg.In(file_location, size=(100, 1), enable_events=True, key="TXT"),
           sg.FileBrowse("Browse", file_types=(('Text Files', '*.txt'),))],
           [sg.Push(), sg.Text("Steam.exe"),
           sg.In(process_location, size=(100, 1), enable_events=True, key="STEAM"),
           sg.FileBrowse("Browse", file_types=(('Exe Files', '*.exe'),))],
          [sg.Text("Change Key"), sg.In(keyboard_key, key="KEYCHANGE"), sg.Text(("Click to Key name list"), enable_events=True, key="KEYWEBSITE", font=font)],
          [sg.Text(" ")],
          [sg.Button(("Click to Start"), key="START"), sg.Button("QUIT"),
           sg.Text(("Now: " + now_account), (50, 1), justification='right')]]

window = sg.Window('Steam Account Changer V1', icon="icon_eg.ico").Layout(layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "QUIT":
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                proc.kill()
        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                proc.kill()
        config["temp"] = {"temp": ""}
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)
        break
    if event == "START":
        file_location_get = window["TXT"].get()
        process_location_get = window["STEAM"].get()
        config["settings"] = {"file_location": file_location_get, "keyboard_key": keyboard_key, "process_name":process_name, "process_location":process_location_get}
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)
        subprocess.Popen(['python.exe', 'login.pyw'])
    if event == "KEYWEBSITE":
        webbrowser.open(r'https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys')

window.close()
# By EdekGame
