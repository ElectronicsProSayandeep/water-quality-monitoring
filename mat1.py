import matplotlib.pyplot as plt
  
# create data
x = [100,20,330,40,550]
y2 = [30,308,30,340,3078]
y1=[500,550,600,650,700]
  
# plot lines
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