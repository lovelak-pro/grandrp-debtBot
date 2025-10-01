import webview as ui
from pyautogui import press
from keyboard import is_pressed
from pyttsx3 import speak
from time import sleep

class APP:
    is_running = False
    def start(self,Speed):
        self.is_running = True
        while self.is_running:
            sleep(0.06)
            if is_pressed('x') and self.is_running == True:
                press('g')
                sleep(Speed/10)
                press('3')
                sleep(Speed/10)
                press('4')
                sleep(Speed/10)
                press('8')

        
    def stop(self):
        self.is_running = False
        while self.is_running == False:
            sleep(0.05)
            if is_pressed('x') and self.is_running == False:
                speak('Start the collector bot first')


if __name__ == "__main__":
    api = APP()
    ui.create_window('Debt-Collector Bot v1.2','src/index.html',js_api=api,width=400,height=270,resizable=False)
    ui.start()