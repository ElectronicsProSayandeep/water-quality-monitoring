import matplotlib
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure


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

hours = []
for i in listcsv:
    hours.append(i[0])

ph = []
for i in listcsv:
    ph.append(i[1])

tds = []
for i in listcsv:
    tds.append(i[2])

turbidity = []
for i in listcsv:
    turbidity.append(i[3])

temperature = []
for i in listcsv:
    temperature.append(i[4])

def phgraph():

    figure(figsize=(13,6))
    plt.xticks(hours)
    plt.plot(hours,ph)
    plt.show()

def tdsgraph():
    figure(figsize=(13,6))
    plt.xticks(hours)
    plt.plot(hours,tds)
    plt.show()

def turbiditygraph():
    figure(figsize=(13,6))
    plt.xticks(hours)
    plt.plot(hours,turbidity)
    plt.show()


def temperaturegraph():
    figure(figsize=(13,6))
    plt.xticks(hours)
    plt.plot(hours,temperature)
    plt.show()
    