from PIL import ImageTk,Image
from tkinter import *
from datetime import date
import os
import csv
import time
import shutil

prodir = "C:\\Users\\Sayandeep\\Software_Development\\python\\water_ml\\water-quality-system\\app"

today = date.today()
hourprev = today.strftime("%M") #use %H for hour, %M for min

def mainscreen(ph, turb, tds, temp):
    mainscrn = Tk()
    mainscrn.grab_set()
    mainscrn.focus_force()
    mainscrn.geometry("1280x720+320+180")
    mainscrn.title("Water Health Sensor")
    mainscrn.iconbitmap('assets/icon.ico')

    mainscrn.mainloop()

while 1:
    #create directory for current month (if req.)
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

    #read arduino readings
    ph = 0
    tds = 0
    turb = 0
    temp = 0

    #create csv (if req.)
    daydate = today.strftime("%d")
    try:
        shutil.copyfile("C:\\Users\\Sayandeep\\Software_Development\\python\\water_ml\\water-quality-system\\app\\data\\blank.csv",mpath + "\\{}".format(str(daydate) + ".csv"))
    except:
        pass

    #add new values to csv
    headcsv = ['hour','ph','tds','turb','temp']
    datacsv = [hourcurr,ph,tds,turb,temp]
    with open(daydate + ".csv", 'w', encoding='UTF8') as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(headcsv)
        writecsv.writerow(datacsv)

    #read last 24 values and store in list


    #mainscreen(currval) #display values on gui
    while 1:
        hourcurr = today.strftime("%M") #use %H for hour, %M for min
        if hourcurr > hourprev:
            hourprev = hourcurr
            print("updating...")
            break
        else:
            time.sleep(30)
