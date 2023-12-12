from tkinter import *

class Files:
    def __init__(self, tk):
        self.root = tk

#create a function if it is not yet created or oper the existed one
    def OpenOrCreate(self):
        try:
            with open("document.txt", "r") as fl:
                content = fl.read()
                self.root.entry.delete("1.0", END)
                self.root.entry.insert("1.0", content)

                self.root.bBin.config(state=NORMAL)
                self.root.bOct.config(state=NORMAL)
                self.root.bHex.config(state=NORMAL)
                self.root.Alert("Now you see a normal string")

        except FileNotFoundError:
            self.root.Alert("File not found! Enter something to the Text field to create a new file and click again")

            newString = str(self.root.entry.get("1.0", END))
            if len(newString) >= 5:
                with open("document.txt", "w") as fl:
                    fl.write(newString)
                    self.root.Alert("Press 'Read' to continue")

            self.root.entry.delete("1.0", END)

#convert file to binary format
    def ToBin(self):
        try:
            with open("document.txt", "r+") as fl:
                newString = ''.join(format(i, '08b') for i in bytearray(fl.read(), encoding='utf-8'))
                self.root.entry.delete("1.0", END)
                self.root.entry.insert("1.0", newString)
                self.root.Alert("Now you see the bin string")
        except Exception as e:
            print("An error:", str(e))

# convert file to octave format
    def ToOct(self):
        try:
            with open("document.txt", "r+") as fl:
                content = fl.read()
                newString = ''.join(format(ord(char), 'o') for char in content)
                self.root.entry.delete("1.0", END)
                self.root.entry.insert("1.0", newString)
                self.root.Alert("Now you see the string in oct format")
        except Exception as e:
            print("An error:", str(e))

# convert file to hexadecimal format
    def ToHex(self):
        try:
            with open("document.txt", "r+") as fl:
                content = fl.read()
                newString = ''.join(format(ord(char), 'x') for char in content)
                self.root.entry.delete("1.0", END)
                self.root.entry.insert("1.0", newString)
                self.root.Alert("Now you see the string in hex format")
        except Exception as e:
            print("An error:", str(e))

