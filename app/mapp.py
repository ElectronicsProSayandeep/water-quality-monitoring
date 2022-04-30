from PIL import ImageTk,Image
from tkinter import *
from datetime import date
import os
import csv
import time
import serial
import shutil

prodir = "C:\\Users\\Sayandeep\\Software_Development\\python\\water_ml\\water-quality-system\\app"

today = date.today()
hourprev = today.strftime("%H") #use %H for hour, %M for min
arduino = serial.Serial(port="COM6", baudrate=115200, timeout=1) #change port everytime reconnect

def mainscreen(ph, turb, tds, temp):
    mainscrn = Tk()
    mainscrn.grab_set()
    mainscrn.focus_force()
    mainscrn.geometry("1280x720+320+180")
    mainscrn.title("Water Health Sensor")
    mainscrn.iconbitmap('assets/icon.ico')

    mainscrn.mainloop()

while 1:
    #read arduino readings
    while True:
        data = arduino.readline()[:-2]
        if data:
            #print(str(data)[2:-1])
            break

    #add new values to csv
    datacsv = [str(data)[2:-1]]
    print(datacsv)
    with open('read24.csv', 'w', encoding='UTF8') as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(datacsv)

    #read csv


    #mainscreen(currval) #display values on gui
    while 1:
        hourcurr = today.strftime("%H") #use %H for hour, %M for min
        if hourcurr > hourprev:
            hourprev = hourcurr
            print("updating...")
            break
        else:
            time.sleep(30)
