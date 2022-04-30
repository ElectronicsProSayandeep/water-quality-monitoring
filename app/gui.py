from tkinter import *
from pathlib import Path
from datetime import date
from PIL import ImageTk,Image
import os
import csv
import time
import numpy
import serial
import shutil
import tkinter
import matplotlib.pyplot as plt

today = date.today()
hourprev = today.strftime("%H") #use %H for hour, %M for min
arduino = serial.Serial(port="COM6", baudrate=115200, timeout=1) #change port everytime reconnect

def mainscreen(csvlist):
    #initialise window
    window = Tk()
    window.geometry("1280x720")
    window.configure(bg = "#3A7FF6")


    #current values
    currdegc = StringVar()
    currph = StringVar()
    currppm = StringVar()
    currntu = StringVar()
    currdegc = str(csvlist[23][0])
    currph = str(csvlist[23][1])
    currppm = str(csvlist[23][2])
    currntu = str(int(float(csvlist[23][3])))


    #csv lists of temp, ph, tds, ntu
    degclist = []
    for i in csvlist:
        degclist.append(float(i[0]))

    phlist = []
    for i in csvlist:
        phlist.append(float(i[1]))

    ppmlist = []
    for i in csvlist:
        ppmlist.append(float(i[2]))

    ntulist = []
    for i in csvlist:
        ntulist.append(float(i[3]))

    hourlist = [23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]


    #predictions
    preddegc = StringVar()
    predph = StringVar()
    predppm = StringVar()
    predntu = StringVar()

    moddegc = numpy.poly1d(numpy.polyfit(hourlist, degclist, 3))
    modph = numpy.poly1d(numpy.polyfit(hourlist, phlist, 3))
    modppm = numpy.poly1d(numpy.polyfit(hourlist, ppmlist, 3))
    modntu = numpy.poly1d(numpy.polyfit(hourlist, ntulist, 3))

    preddegc = round(moddegc(24),2)
    predph = round(modph(24),2)
    predppm = round(modppm(24),2)
    predntu = int(modntu(24))


    #anomalous value lists
    anodegc = []
    for i in degclist:
        anodegc.append(round(abs(i-27),2))

    anoph = []
    for i in phlist:
        anoph.append(round(abs(i-7.5),2))

    anoppm = []
    for i in ppmlist:
        anoppm.append(round(abs(i-100),2))

    anontu = []
    for i in ntulist:
        anontu.append(round(abs(i-25),2))


    #plot graphs
    def phgraph(x,y1,y2):
        fig,ax1 = plt.subplots()
        ax1.set_xlabel('Time(Hrs)')
        ax1.set_ylabel('Parameters(unit)')
        plot_1 = ax1.plot(x, y1)
        ax1.tick_params(axis='y')
        ax2 = ax1.twinx()
        ax2.set_ylabel('Anomality')
        plot_2 = ax2.plot(x, y2, color = 'red')
        ax2.tick_params(axis='y')
        plt.show()

    def ppmgraph(x,y1,y2):
        fig,ax1 = plt.subplots()
        ax1.set_xlabel('Time(Hrs)')
        ax1.set_ylabel('Parameters(unit)')
        plot_1 = ax1.plot(x, y1)
        ax1.tick_params(axis='y')
        ax2 = ax1.twinx()
        ax2.set_ylabel('Anomality')
        plot_2 = ax2.plot(x, y2, color = 'red')
        ax2.tick_params(axis='y')
        plt.show()

    def ntugraph(x,y1,y2):
        fig,ax1 = plt.subplots()
        ax1.set_xlabel('Time(Hrs)')
        ax1.set_ylabel('Parameters(unit)')
        plot_1 = ax1.plot(x, y1)
        ax1.tick_params(axis='y')
        ax2 = ax1.twinx()
        ax2.set_ylabel('Anomality')
        plot_2 = ax2.plot(x, y2, color = 'red')
        ax2.tick_params(axis='y')
        plt.show()

    def degcgraph(x,y1,y2):
        fig,ax1 = plt.subplots()
        ax1.set_xlabel('Time(Hrs)')
        ax1.set_ylabel('Parameters(unit)')
        plot_1 = ax1.plot(x, y1)
        ax1.tick_params(axis='y')
        ax2 = ax1.twinx()
        ax2.set_ylabel('Anomality')
        plot_2 = ax2.plot(x, y2, color = 'red')
        ax2.tick_params(axis='y')
        plt.show()


    #GUI
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg = "#3A7FF6",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    bgimg = tkinter.PhotoImage(file="assets/clean.gif")
    canvas.create_image(
        640.0,
        360.0,
        image = bgimg)

    canvas.create_rectangle(
        576.9999999999999,
        40.00000000000001,
        1237.0,
        680.0,
        fill="#FCFCFC",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: degcgraph(hourlist,degclist,anodegc),
        relief="flat"
    )
    button_1.place(
        x=929.9999999999999,
        y=394.0,
        width=210.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ntugraph(hourlist,ntulist,anontu),
        relief="flat"
    )
    button_2.place(
        x=929.9999999999999,
        y=511.0,
        width=210.0,
        height=55.0
    )

    canvas.create_text(
        704.9999999999999,
        230.0,
        anchor="nw",
        text="TDS",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_text(
        1028.0,
        230.0,
        anchor="nw",
        text="TDS",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_rectangle(
        13.0,
        290.0,
        533.0,
        416.0,
        fill="#121212",
        outline="")

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ppmgraph(hourlist,ppmlist,anoppm),
        relief="flat"
    )
    button_3.place(
        x=660.9999999999999,
        y=511.0,
        width=180.0,
        height=55.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: phgraph(hourlist,phlist,anoph),
        relief="flat"
    )
    button_4.place(
        x=659.9999999999999,
        y=394.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        39.999999999999886,
        300.0,
        anchor="nw",
        text="Water Quality System",
        fill="#FCFCFC",
        font=("Roboto Bold", 48 * -1)
    )

    canvas.create_text(
        679.9999999999999,
        78.0,
        anchor="nw",
        text="Parameters",
        fill="#505485",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_text(
        718.9999999999999,
        130.0,
        anchor="nw",
        text="pH",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_text(
        779.9999999999999,
        125.0,
        anchor="nw",
        text=currph,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        126.0,
        anchor="nw",
        text=predph,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        175.0,
        anchor="nw",
        text=predntu,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        225.0,
        anchor="nw",
        text=predppm,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        275.0,
        anchor="nw",
        text=preddegc,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        779.9999999999999,
        175.0,
        anchor="nw",
        text=currntu,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        779.9999999999999,
        225.0,
        anchor="nw",
        text=currppm,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        779.9999999999999,
        275.0,
        anchor="nw",
        text=currdegc,
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1042.0,
        130.0,
        anchor="nw",
        text="pH",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_text(
        1019.9999999999999,
        78.0,
        anchor="nw",
        text="Predicted",
        fill="#505485",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_rectangle(
        39.999999999999886,
        362.0,
        369.9999999999999,
        364.0,
        fill="#FCFCFC",
        outline="")

    canvas.create_text(
        39.999999999999886,
        372.0,
        anchor="nw",
        text="Water: A Way of Life",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_text(
        656.9999999999999,
        180.0,
        anchor="nw",
        text="Turbidity",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_text(
        979.9999999999999,
        180.0,
        anchor="nw",
        text="Turbidity",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_text(
        613.9999999999999,
        280.0,
        anchor="nw",
        text="Temperature",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )

    canvas.create_text(
        936.9999999999999,
        280.0,
        anchor="nw",
        text="Temperature",
        fill="#505485",
        font=("RobotoRoman Regular", 24 * -1)
    )
    window.resizable(False, False)
    window.mainloop()



while 1:
    #read arduino readings
    while True:
        data = arduino.readline()[:-2]
        if data:
            break
    strcsv = str(data)[2:-1]
    datacsv = list(map(float,strcsv.split(',')))
    
    #prepare csv
    shutil.copyfile("blank.csv","tempread24.csv")
    with open('read24.csv','r') as csvread:
        with open('tempread24.csv','w',newline='\n') as csvwrite:
            next(csvread)
            for line in csvread:
                csvwrite.write(line)
            writecsv = csv.writer(csvwrite)
            writecsv.writerow(datacsv)
    
    os.unlink("read24.csv")
    os.rename("tempread24.csv","read24.csv")

    #read csv
    listcsv = []
    with open('read24.csv','r') as csvread:
        csv_reader = csv.reader(csvread)
        listcsv = list(csv_reader)

    #print(listcsv)
    mainscreen(listcsv)

    #wait for next hour before taking next reading
    while 1:
        hourcurr = today.strftime("%H") #use %H for hour, %M for min
        if hourcurr > hourprev:
            hourprev = hourcurr
            print("updating...")
            break
        else:
            time.sleep(30)
