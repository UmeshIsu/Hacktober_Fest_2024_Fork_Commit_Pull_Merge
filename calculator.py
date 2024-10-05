import tkinter as tk

class CalculatorGUI:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.geometry("200x200")
        self.mw.resizable(0, 0)
        self.mw.title("Calculator")
        self.mw.configure(bg="#67bad1")
        
        self.topFrame = tk.Frame(self.mw, bg="#69bad1")
        self.midFrame = tk.Frame(self.mw)
        self.botFrame = tk.Frame(self.mw)
        self.botFrame2 = tk.Frame(self.mw)
        
        self.topFrame.pack(side="top", fill="both", expand=True)
        self.midFrame.pack(side="top", fill="both", expand=True)
        self.botFrame.pack(side="top", fill="both", expand=True)
        self.botFrame2.pack(side="top", fill="both", expand=True)
        
        self.result = 0
        self.resultDisp = tk.StringVar()
        self.resultDisp.set("0")
        
        self.totalLabel = tk.Label(self.topFrame, text="Value: ", bg="#69bad1")
        self.totalNumb = tk.Label(self.topFrame, textvariable=self.resultDisp, bg="#69bad1")
        self.totalLabel.pack(side="left", padx=5, pady=5)
        self.totalNumb.pack(side="right", padx=5, pady=5)
        
        self.enterBox = tk.Entry(self.midFrame, width=12, bg="#84cce0")
        self.enterBox.pack(side="top", padx=10, pady=10)
        
        self.addButton = tk.Button(self.botFrame, text="+", command=self.addition, bg="#4f8b9c")
        self.subButton = tk.Button(self.botFrame, text="-", command=self.subtraction, bg="#4f8b9c")
        self.multButton = tk.Button(self.botFrame2, text="*", command=self.multiplication, bg="#4f8b9c")
        self.divButton = tk.Button(self.botFrame2, text="/", command=self.division, bg="#4f8b9c")
        self.resetButton = tk.Button(self.botFrame, text="Reset", command=self.reset, bg="#4f8b9c")
        self.exitButton = tk.Button(self.botFrame2, text="Quit", command=self.quitProgram, bg="#ff2121")
        
        self.addButton.pack(side="left", padx=5, pady=5)
        self.subButton.pack(side="left", padx=5, pady=5)
        self.multButton.pack(side="left", padx=5, pady=5)
        self.divButton.pack(side="left", padx=5, pady=5)
        self.resetButton.pack(side="right", padx=5, pady=5)
        self.exitButton.pack(side="right", padx=5, pady=5)
        
        tk.mainloop()

    def addition(self):
        try:
            self.result += float(self.enterBox.get())
        except ValueError:
            pass
        self.resultDisp.set(round(self.result, 4))

    def subtraction(self):
        try:
            self.result -= float(self.enterBox.get())
        except ValueError:
            pass
        self.resultDisp.set(round(self.result, 4))

    def multiplication(self):
        try:
            self.result *= float(self.enterBox.get())
        except ValueError:
            pass
        self.resultDisp.set(round(self.result, 4))

    def division(self):
        try:
            divisor = float(self.enterBox.get())
            if divisor != 0:
                self.result /= divisor
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        self.resultDisp.set(round(self.result, 4))

    def reset(self):
        self.result = 0
        self.resultDisp.set(self.result)

    def quitProgram(self):
        self.mw.destroy()

def main():
    gui = CalculatorGUI()
    return gui

if __name__ == "__main__":
    gui = main()
