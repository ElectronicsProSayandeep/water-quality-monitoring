from tkinter import *
from pathlib import Path
from datetime import date
from PIL import ImageTk,Image
import os
import csv
import time
import serial
import shutil
import tkinter

today = date.today()
hourprev = today.strftime("%H") #use %H for hour, %M for min
arduino = serial.Serial(port="COM6", baudrate=115200, timeout=1) #change port everytime reconnect

def mainscreen(csvlist):
    #current values
    currdegc = csvlist[23][0]
    currph = csvlist[23][1]
    currppm = csvlist[23][2]
    currntu = csvlist[23][3]

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

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()
    window.geometry("1280x720")
    window.configure(bg = "#3A7FF6")

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
        command=lambda: print("button_1 clicked"),
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
        command=lambda: print("button_2 clicked"),
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
        12.999999999999886,
        296.0,
        532.9999999999999,
        416.0,
        fill="#000000",
        outline="")

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
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
        command=lambda: print("button_4 clicked"),
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
        text="1",
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        126.0,
        anchor="nw",
        text="2",
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        175.0,
        anchor="nw",
        text="3",
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        225.0,
        anchor="nw",
        text="4",
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        1100.0,
        275.0,
        anchor="nw",
        text="5",
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        779.9999999999999,
        175.0,
        anchor="nw",
        text="6",
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        779.9999999999999,
        225.0,
        anchor="nw",
        text="7",
        fill="#505485",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        779.9999999999999,
        275.0,
        anchor="nw",
        text="8",
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
        text="Water: a way of life",
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
            #print(str(data)[2:-1])
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

    while 1:
        hourcurr = today.strftime("%H") #use %H for hour, %M for min
        if hourcurr > hourprev:
            hourprev = hourcurr
            print("updating...")
            break
        else:
            time.sleep(30)
