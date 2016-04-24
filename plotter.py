# x axis - all the frames
#timeArray = arange(0, channel1.shape[0], 1)
#timeArray = timeArray / frequency
#print timeArray
#timeArray = timeArray * 1000  #scale to milliseconds

#plt.plot(timeArray, channel1, color='k')
#ylabel('Amplitude')
#xlabel('Time (ms)')

#plt.show()

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('mfcc.csv','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()



Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.show()