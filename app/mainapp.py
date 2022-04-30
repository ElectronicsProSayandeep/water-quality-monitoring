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


listcsv = [[0,7.25,212,700,20],
[1,7.69,212,800,22],
[2,7.04,204,900,24],
[3,7.88,176,900,22],
[4,8.44,128,950,22],
[5,8.56,128,1000,25],
[6,8.88,117,1200,24],
[7,7.83,136,1200,26],
[8,7.33,120,1400,27],
[9,8.09,148,1400,28],
[10,7.78,156,1500,30],
[11,7.33,141,1600,31],
[12,7.73,132,1600,31],
[13,7.99,120,1600,34],
[14,8.5,140,1700,32],
[15,8.03,150,1700,32],
[16,7.8,163,1800,30],
[17,7.17,176,1600,27],
[18,8.03,190,1500,27],
[19,7.9,180,1600,25],
[20,8.6,165,1300,25],
[21,7.67,170,1500,25],
[22,8.7,179,1500,24],
[23,8.7,160,1200,21]
]