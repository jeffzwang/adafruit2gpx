import serial
import time
import sys
import math
import tkinter as tk

port = sys.argv[1]
ser = serial.Serial(port, 115200)

root = tk.Tk()
root.title("Welcome to your GPS!")
root.geometry("300x200")
frame = tk.Frame(root)
frame.pack()

def dump():
    ser.write(str.encode('d'))
    shit = ser.read_until(str.encode("$PMTK001,622,3*36\r\n"))
    print(shit)

def erase():
    ser.write(str.encode('e'))
    print("erased all parses")

dump_button = tk.Button(frame, text="dump", command=dump)
dump_button.pack(side=tk.LEFT)

erase_button = tk.Button(frame, text="erase all", command=erase)
erase_button.pack(side = tk.RIGHT)
root.mainloop()
