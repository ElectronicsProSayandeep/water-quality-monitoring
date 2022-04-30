from tkinter import*
import tkinter.messagebox 
from tkinter import ttk
import random
import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from datetime import datetime
from datetime import datetime, timedelta
from tkinter import*
from PIL import ImageTk,Image




def main():
    root = Tk()
    app = Window1(root)
   



class Window1:
        def __init__(self,master):
            self.master=master
            self.master.title("WATER QUALITY SYSTEM")
            self.master.geometry('1350x750+0+0')
            self.master.config(bg ='#003B46')

            self.frame = Frame(self.master, bg='#003B46')
            self.frame.pack()
            #==============================================================declaring variables============================================================
            self.v1 = IntVar()
            self.v2 = IntVar()
            self.v3 = IntVar()
            self.v4 = IntVar()
            self.pv1 = IntVar()
            self.pv2 = IntVar()
            self.pv3 = IntVar()
            self.pv4 = IntVar()
            
            self.v1=10
            self.v2=4
            self.v3=7
            self.v4=12

            self.pv1=13
            self.pv2=5
            self.pv3=8
            self.pv4=19

            obg = '#2C698D'
            ibg = '#BAE8E8'
            textc = '#E3F6F5'

            font ='Baskerville Old Face'
            fonth= 'Times New Roman'
            #=============================frames============================================================================================================================================
            self.LeftFrame= LabelFrame(self.frame, width=1354, height=754,font=(font,50,'roman'), relief= RIDGE, bg= obg, bd =13)
            self.LeftFrame.grid(row=0, column=0)
            
            self.ParameterFrame=LabelFrame(self.LeftFrame, width=330, height=300,font=(font,50,'roman'), relief=RIDGE, bg= ibg, bd =6)
            self.ParameterFrame.grid(row=2, column=0,padx=206,pady=6)

            self.ChartFrame=LabelFrame(self.LeftFrame, width=330, height=300,font=(font,50,'roman'), relief=RIDGE, bg= ibg, bd =6)
            self.ChartFrame.grid(row=2, column=1,padx=206,pady=6)
            
            self.BottomFrame1=LabelFrame(self.LeftFrame, width=330, height=300,font=(font,50,'roman'), relief=RIDGE, bg= ibg, bd =6)
            self.BottomFrame1.grid(row=7, column=0,padx=206,pady=6)
            
            self.BottomFrame2=LabelFrame(self.LeftFrame, width=330, height=250,font=(font,50,'roman'), relief=RIDGE, bg= ibg, bd =6)
            self.BottomFrame2.grid(row=7, column=1,padx=206,pady=6)
            #============================================================title===========================================================================================================
            self.lblTitle = Label(self.LeftFrame, text = 'WATER QUALITY SYSTEM', font=(fonth,30,'roman'),bg=obg,fg=textc)
            self.lblTitle.grid(row=0, column=0,columnspan=2)

            self.lbltitle = Label(self.LeftFrame, text = 'Parameters-', font=(fonth,30,'roman'),bg=obg,fg=textc)
            self.lbltitle.grid(row=1, column=0)

            self.lbltitle = Label(self.LeftFrame, text = 'Prediction-', font=(fonth,30,'roman'),bg=obg,fg=textc)
            self.lbltitle.grid(row=1, column=1)

            self.lbltitle = Label(self.LeftFrame, text = 'Graphs-', font=(fonth,30,'roman'),bg=obg,fg=textc)
            self.lbltitle.grid(row=6, column=0)

            self.lbltitle = Label(self.LeftFrame, text = 'Other-', font=(fonth,30,'roman'),bg=obg,fg=textc)
            self.lbltitle.grid(row=6, column=1)
           
            #============================================================labels===========================================================================================================
            self.lbl1 = Label(self.ParameterFrame,text = 'pH:', width = 10,font=(fonth,20,'italic'), fg=obg,bg=ibg)
            self.lbl1.grid(row=2,column=0)

            self.lbl2 = Label(self.ParameterFrame,text = 'TDS:', width = 10,font=(fonth,20,'italic'),  fg=obg,bg=ibg)                                                           
            self.lbl2.grid(row=3,column=0)

            self.lbl3 = Label(self.ParameterFrame,text = 'Turbidity:', width = 10,font=(fonth,20,'italic'),  fg=obg,bg=ibg)                            
            self.lbl3.grid(row=4,column=0)
            
            self.lbl4 = Label(self.ParameterFrame,text = 'Temp:', width = 10,font=(fonth,20,'italic'),  fg=obg,bg=ibg)                            
            self.lbl4.grid(row=5,column=0,columnspan=1)

            self.lblp1=Label(self.ParameterFrame,font=(fonth,20,'italic'),text=self.v1,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp1.grid(row=2,column=1)
            
            self.lblp2=Label(self.ParameterFrame,font=(fonth,20,'italic'),text=self.v2,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp2.grid(row=3,column=1)
            
            self.lblp3=Label(self.ParameterFrame,font=(fonth,20,'italic'),text=self.v3,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp3.grid(row=4,column=1)
            
            self.lblp4=Label(self.ParameterFrame,font=(fonth,20,'italic'),text=self.v4,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp4.grid(row=5,column=1)
            
                
                        
            #===================================================buttons====================================================================================================================
            self.btnp1 = Button(self.BottomFrame1,text = 'pH', width = 15,font=(fonth,20,'italic'), command = self.new_window , fg=obg,bg=textc)
            self.btnp1.grid(row=8,column=0)

            self.btnp2 = Button(self.BottomFrame1,text = 'Turbidity', width = 15,font=(fonth,20,'italic'), fg=obg,bg=textc)                                                           
            self.btnp2.grid(row=9,column=0)

            self.btnp3 = Button(self.BottomFrame1,text = 'TDS', width = 15,font=(fonth,20,'italic'), fg=obg,bg=textc)                            
            self.btnp3.grid(row=10,column=0)

            self.btnp4 = Button(self.BottomFrame1,text = 'Temp', width = 15,font=(fonth,20,'italic'), fg=obg,bg=textc)
            self.btnp4.grid(row=11,column=0)
            #==============================================================================================================================================
            self.lbl1 = Label(self.ChartFrame,text = 'pH:', width = 10,font=(fonth,20,'italic'), fg=obg,bg=ibg)
            self.lbl1.grid(row=2,column=0)

            self.lbl2 = Label(self.ChartFrame,text = 'TDS:', width = 10,font=(fonth,20,'italic'),  fg=obg,bg=ibg)                                                           
            self.lbl2.grid(row=3,column=0)

            self.lbl3 = Label(self.ChartFrame,text = 'Turbidity:', width = 10,font=(fonth,20,'italic'),  fg=obg,bg=ibg)                            
            self.lbl3.grid(row=4,column=0)
            
            self.lbl4 = Label(self.ChartFrame,text = 'Temp:', width = 10,font=(fonth,20,'italic'),  fg=obg,bg=ibg)                            
            self.lbl4.grid(row=5,column=0)

            self.lblp1=Label(self.ChartFrame,font=(fonth,20,'italic'),text=self.pv1,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp1.grid(row=2,column=1)
            
            self.lblp2=Label(self.ChartFrame,font=(fonth,20,'italic'),text=self.pv2,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp2.grid(row=3,column=1)
            
            self.lblp3=Label(self.ChartFrame,font=(fonth,20,'italic'),text=self.pv3,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp3.grid(row=4,column=1)
            
            self.lblp4=Label(self.ChartFrame,font=(fonth,20,'italic'),text=self.pv4,bd=22, bg=ibg, fg=obg, borderwidth=10)                                                                               
            self.lblp4.grid(row=5,column=1)

        #===========================defining===========================================================================================================
        def new_window(self):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
                 

class Window2:
        def __init__(self,master):
            self.master=master
            self.master.title("HEHEHAHAHHAA")
            self.master.geometry('1350x750+0+0')
            self.master.config(bg =obg)

            self.frame = Frame(self.master, bg=obg)
            self.frame.pack()            
            
#================================================================================================================================================================================================    
           

    
if __name__ == '__main__':
    main()
    
