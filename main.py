import webview as ui
from pyautogui import press
from keyboard import is_pressed
from pyttsx3 import speak
from time import sleep

class APP:
    is_running = False
    def start(self):
        self.is_running = True
        while self.is_running:
            sleep(0.06)
            if is_pressed('x') and self.is_running == True:
                delay = 0.45
                press('g')
                sleep(delay)
                press('3')
                sleep(delay)
                press('4')
                sleep(delay)
                press('8')

                
    def stop(self):
        self.is_running = False
        while self.is_running == False:
            sleep(0.05)
            if is_pressed('x') and self.is_running == False:
                speak('Start the collector bot first')


if __name__ == "__main__":
    api = APP()
    ui.create_window('Debt-Collector Bot v1.1','src/index.html',js_api=api,width=400,height=220,resizable=False)
    ui.start()