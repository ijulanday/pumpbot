import tkinter as tk
from functools import partial
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)

def run_pump(pump):
    mstr = "deploying pump " + str(pump)
    print(mstr)

root = tk.Tk()
root.title('Pump Control!')
root.geometry('400x200')
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)

button.pack(side=tk.LEFT)

for i in range(8,13):
    button = tk.Button(frame,
                    text="Pump " + str(i),
                    command=partial(run_pump, i))
    button.pack(side=tk.LEFT)

root.mainloop()