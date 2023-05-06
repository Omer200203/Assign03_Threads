import matplotlib.pyplot as plt

Threads = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Time = [0.00010,0.00020,0.00038,0.00046,0.00059,0.00062,0.00078,0.00083,0.00090,0.00106,0.00111,0.00129,0.00131,0.00149,0.00152]

plt.plot(Threads,Time, '-X')

plt.title('Conway Game Of Life')
plt.xlabel('Number Of Threads')
plt.ylabel('Time Per/Sec')

plt.show()
