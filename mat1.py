import matplotlib.pyplot as plt
  
# create data
x = [100,20,330,40,550]
y2 = [30,308,30,340,3078]
y1=[500,550,600,650,700]
  
# plot lines
plt.plot(x, y1, label = "Actual")
plt.plot(x, y2, label = "Anomalous")
plt.xlabel("Time(Hrs)")
plt.ylabel("Parameters(unit)")

plt.legend()
plt.show()