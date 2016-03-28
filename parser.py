from pylab import*
from scipy.io import wavfile
import matplotlib.pyplot as plt

frequency, sound = wavfile.read('wavfiles/testFile.wav')

# get the first channel
channel1 = sound[:,0] 
# x axis - all the frames
#timeArray = arange(0, channel1.shape[0], 1)
#timeArray = timeArray / frequency
#print timeArray
#timeArray = timeArray * 1000  #scale to milliseconds

#plt.plot(timeArray, channel1, color='k')
#ylabel('Amplitude')
#xlabel('Time (ms)')

#plt.show()

