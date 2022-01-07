from model import SobrietyClassifier
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
import os
import sys
import xgboost as xgb
from sklearn.model_selection import train_test_split
sys.path.insert(0, "../preprocessing")
from audio_preprocessing import AudioPreprocessing


def main():
    
    ''' Below is an example how to run the model'''
    
    '''
    # Initializes the class instance
    data = AudioPreprocessing() 
    
    
    # Imports all the "../preprocessing""../preprocessing" files contained in the folder specified by the path (converts non .wav to .wav too)
    
    data.import_audio(PATH_TO_AUDIO) 

    # Extracts all the features from the loaded audio files and stores them in a .csv where each loaded file has its own row with data
    # If a file from a given row didn't have "sober" or "unsober" in the filename, the label for that row will be "unknown"
    
    data.save_csv(SAVE_PATH_WITH_FILENAME) 

    Performs a train-test split on the data from the specified .csv file - data ready to be fed to the model
    
    X_train, X_test, y_train, y_test = data.model_data_split(test_set_size, random_state, PATH_TO_CSV_FEATURES)
    
    model = SobrietyClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print('Accuracy: %.2f' % (accuracy*100))
    
    '''
    
if __name__ == '__main__':
    main()