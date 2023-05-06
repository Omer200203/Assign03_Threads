import matplotlib.pyplot as plt

Threads = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Time = [0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.010,0.011,0.012,0.013,0.014,0.015]

plt.plot(Threads,Time, '-X')

plt.title('Conway Game Of Life')
plt.xlabel('Number Of Threads')
plt.ylabel('Time Per/Sec')

plt.show()
