import pandas as pd
import pydub
from preprocess import dataset


from sklearn.model_selection import train_test_split

train,test = train_test_split(dataset, test_size=0.1,random_state=0)
dev,test = train_test_split(test, test_size=0.5,random_state=0)

print(train.shape ,dev.shape,test.shape)
train.to_csv('train.csv', index=False)
dev.to_csv('dev.csv', index=False)
test.to_csv('test.csv', index=False)

import soundfile

def convert(wavfile_name):
    data, samplerate = soundfile.read(wavfile_name)
    soundfile.write(wavfile_name,data,samplerate,subtype='PCM_16')
    return wavfile_name
train['wav_filename'] = train['wav_filename'].apply(convert)
dev['wav_filename'] = dev['wav_filename'].apply(convert)
test['wav_filename'] = test['wav_filename'].apply(convert)

print(dev['wav_filename'][1])
train = pd.read_csv("train.csv")
dev = pd.read_csv("dev.csv")
test = pd.read_csv("test.csv")