from PIL import ImageTk,Image
from tkinter import *
from datetime import date
import os
import csv
import time

prodir = "C:\\Users\\Sayandeep\\Software_Development\\python\\water_ml\\water-quality-system\\app"

def mainscreen(ph, turb, tds, temp):
    mainscrn = Tk()
    mainscrn.grab_set()
    mainscrn.focus_force()
    mainscrn.geometry("1280x720+320+180")
    mainscrn.title("Water Health Sensor")
    mainscrn.iconbitmap('assets/icon.ico')

    mainscrn.mainloop()

while 1:
    today = date.today()
    d1 = today.strftime("%Y")
    d2 = today.strftime("%B")
    try:
        fpath = os.path.join(prodir, "data")
        ypath = os.path.join(fpath, str(d1))
        os.mkdir(ypath)
        mpath = os.path.join(ypath, d2)
        os.mkdir(mpath)
    except:
        pass

    #read arduino csv
    ph = 0
    turb = 0
    tds = 0
    temp = 0


    mainscreen(ph, turb, tds, temp)
    time.sleep(3600)