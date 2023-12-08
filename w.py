from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def openWhatsapp():
    startfile("C:\\Users\\Prathamesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)

def closeWhatsapp():
    startfile("C:\\Users\\Prathamesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    click(x=1889, y=25)

def openChat(name):
    startfile("C:\\Users\\Prathamesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(1)
    click(x=491, y=129)
    sleep(1)
    click(x=375, y=136)
    sleep(1)
    write(name)
    sleep(1)
    click(x=237, y=264)
    sleep(1)

def sendMsg(message):
    startfile("C:\\Users\\Prathamesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(1)
    click(x=1036, y=970)
    sleep(1)
    write(message)
    press("enter")

def call(name):
    startfile("C:\\Users\\Prathamesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(1)
    click(x=491, y=129)
    sleep(1)
    click(x=375, y=136)
    sleep(1)
    write(name)
    sleep(1)
    click(x=237, y=264)
    sleep(1)
    click(x=1719, y=68)
    
def videoCall(name):
    startfile("C:\\Users\\Prathamesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(1)
    click(x=491, y=129)
    sleep(1)
    click(x=375, y=136)
    sleep(1)
    write(name)
    sleep(1)
    click(x=237, y=264)
    sleep(1)
    click(x=1647, y=70)
