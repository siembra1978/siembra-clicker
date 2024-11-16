#written by siembra

from pynput.mouse import Button as msButton, Controller
from pynput import keyboard
from tkinter import *
import time
import random
import threading
#from playsound import playsound
    
class clickerUI:
    
    def __init__(self, master):
        
        self.running = True
        self.clicking = False
        
        self.master = master
        self.master.geometry("384x128")
        
        master.title("siembra's autoclicker")
        master.configure(bg="gray9")
        
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        self.cps = 15
        
        self.generateUI()
        self.initClick()
        self.listener = keyboard.Listener(on_press=self.onKeyPress)
        self.listener.start()
        print("Listening...")
        
    def generateUI(self):
        print("Building UI")
        self.window = Frame(self.master, bg="gray9")
        self.window.grid(row=0,column=0)
        
        self.cpsLabel = Label(self.window, text="CPS:", bg="gray9", fg="white")
        self.cpsLabel.grid(row=0,column=0)
        
        self.cpsEntry = Entry(self.window, bg="gray9", fg="white")
        self.cpsEntry.grid(row=0,column=1)
        self.cpsEntry.insert(0, str(self.cps))

        self.yipeeButton = Button(self.window, bg="gray9", fg="white", text="yipee!!!", command=self.yipee)
        self.yipeeButton.grid(row=1,column=1)

    def onKeyPress(self, key):
        try:
            if key.char == 'g' and not self.clicking:
                self.resumeClick()
            elif key.char == 'g' and self.clicking:
                self.haltClick()
        except AttributeError:
            pass

    def yipee(self):
        threading.Thread(target=playsound, args=('C:/Users/chedd/Desktop/GitProjects/siembra-clicker/yip.mp3',)).start()
        #playsound('C:/Users/chedd/Desktop/GitProjects/siembra-clicker/yip.mp3')
    def initClick(self):
        print("Initiating click thread loop")
        clickThread = threading.Thread(target=self.autoClick)
        clickThread.daemon = True
        clickThread.start()
        
    def resumeClick(self):
        print("Resume clicking")
        try:
            self.cps = int(self.cpsEntry.get())
        except ValueError:
            self.cps = 15
        self.clicking = True
        
    def haltClick(self):
        print("Stop clicking")
        self.clicking = False
    
    def onClose(self):
        print("Bye bye")
        self.listener.stop()
        self.running = False
        self.master.destroy()

    def autoClick(self):
        
        mouse = Controller()
        
        while self.running:
            while self.clicking:
                mouse.click(msButton.left, 1)
                #threading.Thread(target=playsound, args=('C:/Users/chedd/Desktop/GitProjects/siembra-clicker/yip.mp3',)).start()
                time.sleep((1/self.cps)*random.random())
        time.sleep(.1)

if __name__ == "__main__":    
    root = Tk()
    app = clickerUI(root)
    root.protocol("WM_DELETE_WINDOW", app.onClose)
    root.mainloop()

