from subprocess import call
from yaafelib import *
from numpy import *
import os

genresFolder = '/app/genres'

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

num_classes = 10

def extract(filename):
    root = os.path.splitext(os.path.splitext(filename)[0])[0]  # remove .tar.gz
    if os.path.isdir(root):
        print('File %s already extracted' % (root))
    else:
        print('Extracting %s ' % filename)
        tar = tarfile.open(filename)
        sys.stdout.flush()
        tar.extractall()
        tar.close()
    data_folders = [os.path.join(root, d) for d in sorted(os.listdir(root))
                    if os.path.isdir(os.path.join(root, d))]
    if len(data_folders) != num_classes:
        raise Exception('Expected %d folders not found.' % (num_classes))
    print(data_folders)
    return data_folders

def get_features(audio_file):
    if os.path.exists(audio_file):
        print('Getting features from ' + audio_file)
    else:
        raise Exception('File ' + audio_file + ' not found')
    fp = FeaturePlan(sample_rate=22050, normalize=1)
    # Features that seems to be most often used, so they are good to start with.
    fp.addFeature('mfcc: MFCC')
    fp.addFeature('zcr: ZCR')
    fp.addFeature('spectral_shape: SpectralShapeStatistics')
    fp.addFeature('magnitude_spectrum: MagnitudeSpectrum')
    df = fp.getDataFlow()
    engine = Engine()
    engine.load(df)
    afp = AudioFileProcessor()
    afp.setOutputFormat('csv', 'features', {'Precision': '8', 'Metadata': 'False'})
    afp.processFile(engine, audio_file)
    engine.flush()
    feats = engine.readAllOutputs()
    return feats

def load_genre(folder):
    print('Loading genre from folder ' + folder)
    samples = os.listdir(folder)
    dataset =[]
    for sample in os.listdir(folder):
        sample_file = os.path.join(folder, sample)
        if sample.endswith('.au'):
            features = get_features(sample_file)
            dataset.append(features)
    return dataset

def pickle(data_folders):
    dataset_names = []
    for folder in data_folders:
        set_filename = folder + '.pickle'
        dataset_names.append(set_filename)
        if os.path.exists(set_filename):
            print('%s already pickled' % set_filename)
        else:
            print('Pickling %s.' % set_filename)
            dataset = load_genre(folder)
            with open(set_filename, 'wb') as f:
                pickle.dump(dataset, f, pickle.HIGHEST_PROTOCOL)
    return dataset_names

def getDataFolders():
    content_list = []
    for dirname, dirnames, filenames in os.walk(genresFolder):
        for subdirname in dirnames:
            content_list.append(os.path.join(dirname, subdirname))
    return content_list

# pickled_datasets = pickle(getDataFolders())
dataset_names = pickle(getDataFolders())
print(dataset_names)
