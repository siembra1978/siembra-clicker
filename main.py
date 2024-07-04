from pynput.mouse import Button as msButton, Controller
from pynput import keyboard
from tkinter import *
import time
import threading
    
class clickerUI:
    
    def __init__(self, master):
        
        self.running = True
        self.clicking = False
        
        self.master = master
        self.master.geometry("320x212")
        
        master.title("siembra's PyClicker")
        master.configure(bg="gray9")
        
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        self.cps = 15
        
        self.generateUI()
        self.initClick()
        self.listener = keyboard.Listener(on_press=self.onKeyPress)
        self.listener.start()
        
    def generateUI(self):
        self.window = Frame(self.master, bg="gray9")
        self.window.grid(row=0,column=0)
        
        self.cpsLabel = Label(self.window, text="CPS:", bg="gray9", fg="white")
        self.cpsLabel.grid(row=0,column=0)
        
        self.cpsEntry = Entry(self.window, bg="gray9", fg="white")
        self.cpsEntry.grid(row=0,column=1)
        
        #self.startBtn = Button(self.window, text="Start Clicking", bg="gray9", fg="white", command=self.initClick)
        #self.startBtn.grid(row=2,column=1)
        
    def onKeyPress(self, key):
        try:
            if key.char == 'h':
                self.resumeClick()
            elif key.char == 'g':
                self.haltClick()
        except AttributeError:
            pass
        
    def initClick(self):
        clickThread = threading.Thread(target=self.autoClick)
        clickThread.daemon = True
        clickThread.start()
        
    def resumeClick(self):
        try:
            self.cps = int(self.cpsEntry.get())
        except ValueError:
            self.cps = 15
        self.clicking = True
        
    def haltClick(self):
        self.clicking = False
    
    def onClose(self):
        self.listener.stop()
        self.master.destroy()

    def autoClick(self):
        
        mouse = Controller()
        
        while self.running:
            while self.clicking:
                mouse.click(msButton.left, 1)
                time.sleep(1/self.cps)
        time.sleep(.1)

if __name__ == "__main__":    
    root = Tk()
    app = clickerUI(root)
    root.protocol("WM_DELETE_WINDOW", app.onClose)
    root.mainloop()

