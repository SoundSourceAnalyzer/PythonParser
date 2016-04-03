from scipy.io import wavfile

frequency, sound = wavfile.read('wavfiles/classic.wav')

#each sound consists of 2 channels

#in order to compute some of the properties, we need to perform
#sound normalization - convert each frame into the range of [-1,1]

# get the first channel
channel1 = sound[:,0] 

print frequency
