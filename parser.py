from scipy.io import wavfile
from jsonpickle import encode

wavFilesPath = 'wavfiles/'


class Sound(object):
    def __init__(self, filename):
        self.filename = filename
        self.frequency, self.sound = wavfile.read(wavFilesPath + filename)
        self.channel1 = self.sound[:, 0]
        self.channel2 = self.sound[:, 1]
        self.duration = len(self.sound) / self.frequency


class ResultFile(object):
    def __init__(self, soundfile):
        self.filename = soundfile.filename
        self.frequency = soundfile.frequency
        self.duration = soundfile.duration


soundFile = Sound('classic.wav')
resultFile = ResultFile(soundFile)
print(encode(resultFile))
