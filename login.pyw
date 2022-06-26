import subprocess
import keyboard
import psutil as psutil
from configparser import ConfigParser

config = ConfigParser()
config.read("config.cfg")
key = config["settings"]["keyboard_key"]
file_location = config["settings"]["file_location"]
process_location = config["settings"]["process_location"]
procname = config["settings"]["process_name"]
f = open(file_location, 'r').readlines()
a = []


def login():
    for line in f:
        b = line.strip().split(':')
        c = (' '.join(b))
        config["temp"] = {"temp": c}
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)
        subprocess.Popen([process_location, '-login', c.split()[0], c.split()[1]])
        keyboard.wait(key)
        for proc in psutil.process_iter():
            if proc.name() == procname:
                proc.kill()


login()
