from speak import  speak
import webbrowser
import pyautogui as gui
import time

def open_youtube():
    url = "https://www.youtube.com"
    speak("opening..")
    webbrowser.open(url)
    speak("done sir")

def open_telegram():
    gui.press('winleft')
    time.sleep(1)
    gui.write('telegram')
    time.sleep(1)
    gui.press('enter')
    speak('check screen sir')

def chatgpt():
    webbrowser.open("https://openai.com/blog/chatgpt")
    speak("click try free for use")

def open_chrome():
    gui.press('winleft')
    time.sleep(1)
    gui.write('chrome')
    time.sleep(1)
    gui.press('enter')
    speak('done sir')



def open_code():
    gui.press('winleft')
    time.sleep(1)
    gui.write('vscode')
    time.sleep(1)
    gui.press('enter')
    speak('now you can start sir')



def open_whatsapp():
    gui.press('winleft')
    time.sleep(1)
    gui.write('whatsapp')
    time.sleep(1)
    gui.press('enter')
    speak('exicution done sir')

def open_insta():
    gui.press('winleft')
    time.sleep(1)
    gui.write('instagram')
    time.sleep(1)
    gui.press('enter')
    speak('here we go')


