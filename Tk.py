from tkinter import *
from Files import Files

class Tkinter:
    def __init__(self):
        self.files = Files(self)
        self._SetUp()
        self._CreateElements()

#private function for a gasic setup
    def _SetUp(self):
        self.tk = Tk()
        self.tk.configure(bg="gray")
        self.tk.geometry("800x500")
        self.tk.minsize(800, 500)
        self.tk.maxsize(800, 500)
        self.tk.title("Files")

#create a lebel to print all the user information
    def Alert(self, text):
        Label(text=text, fg="black", bg="gray", width="100", height="1").place(x = 50, y = 50)

#private function to create basic elements
    def _CreateElements(self):
        Label(text="Use buttons to convert text", fg="black", bg="gray", width="25", height="1").pack()
        self.bRead = Button(self.tk, text="Read", width="5", bg="gray", command=self.files.OpenOrCreate)
        self.bBin = Button(self.tk, text="bin", width="5", bg="gray", command=self.files.ToBin)
        self.bOct = Button(self.tk, text="oct", width="5", bg="gray", command=self.files.ToOct)
        self.bHex = Button(self.tk, text="hex", width="5", bg="gray", command=self.files.ToHex)
        self.bRead.place(x=100, y=100)
        self.bBin.place(x=180, y=100)
        self.bOct.place(x=260, y=100)
        self.bHex.place(x=340, y=100)
        self.bRead.config(state=NORMAL)
        self.bBin.config(state=DISABLED)
        self.bOct.config(state=DISABLED)
        self.bHex.config(state=DISABLED)


        self.entry = Text(self.tk, width = 70, height = 20)
        self.entry.place(x = 100, y = 150)

#run the program
    def run(self):
        self.tk.mainloop()
