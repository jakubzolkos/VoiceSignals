'''
This program should contains class methods responsible for following steps (from main.py file):
1. Load files [check]
2. Check if they are already converted to .wav extension if they are not --> convert them [check]
3. Make a .csv file [check]
5. Save features to a csv file [check]
9. Save the results of machine learning algorithm and find different solutions of data preprocessing (so back to step 6.)
'''
import csv
import os.path
import librosa
import collections
import numpy as np
from pydub import AudioSegment
from data_features import Data_features

class Data_operator(object):

    def __init__(self, rootdir):

        self.rootdir = rootdir
        self.data = collections.defaultdict(list)

    def make_csv_file(self):
        header = 'chroma_stft spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
        for i in range(1, 21):
            header += f' mfcc{i}'
        header += ' label'
        header = header.split()

        file = open('dataset.csv', 'w', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(header)


    def save_features_to_csv(self):
        
        for i in range(len(self.data['sobriety'])):

            audio_object = Data_features(self.data['audio_data'][i], self.data['sample_rate'][i])
            chroma_stft, spec_cent, spec_bw, rolloff, zcr, mfcc = audio_object.features()
            
            
            to_append = f'{np.mean(chroma_stft)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
            for e in mfcc:
                to_append += f' {np.mean(e)}'
            to_append += " {}".format(self.data['sobriety'][i])
            file = open('dataset.csv', 'a', newline='')
            with file:
                writer = csv.writer(file)
                writer.writerow(to_append.split())

    
    def converter(self):
        for subdir, dirs, files in os.walk(self.rootdir):
            for filename in files:
                if filename.endswith('.wav'):
                    continue
                else:
                    AudioSegment.from_file(os.path.join(subdir, filename), os.path.splitext(filename)[1][1:]).export(os.path.join(subdir
                    , filename.split(".")[0] + '.wav'), format = 'wav')
                    os.remove((os.path.join(subdir, filename)))
        
    
    def import_audio(self):
        for subdir, dirs, files in os.walk(self.rootdir):
            for filename in files:
                audio_data, sample_rate = librosa.load(os.path.join(subdir, filename))
                self.data["audio_data"].append(audio_data)
                self.data["sample_rate"].append(sample_rate)
                self.data["sobriety"].append(subdir.split('\\')[-1])
        
        self.make_csv_file()
        self.save_features_to_csv()
        
    def save_results(self):
        pass