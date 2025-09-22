import webview
import pyautogui as py
import keyboard as kb
from pyttsx3 import speak
from time import sleep

class APP:
    is_running = False
    def start(self):
        self.is_running = True
        while self.is_running:
            sleep(0.06)
            if kb.is_pressed('x') and self.is_running == True:
                delay = 0.45
                py.press('g')
                sleep(delay)
                py.press('3')
                sleep(delay)
                py.press('4')
                sleep(delay)
                py.press('8')


    def stop(self):
        self.is_running = False
        while self.is_running == False:
            sleep(0.05)
            if kb.is_pressed('x') and self.is_running == False:
                speak('Start the collector bot first')


if __name__ == "__main__":
    api = APP()
    webview.create_window('Debt-Collector Bot','src/index.html',js_api=api,width=400,height=220,resizable=False)
    webview.start()