import os
from pathlib import Path
import pandas as pd

wav_file_name = []
wav_file_size = []
wav_transcript = []

print(os.path)
path = Path('wav')

#print(path)
dir = list(path.glob('*.wav'))

#print(dir)
a = os.chdir(path)
#print(a)

for i in dir:
    wav_file_name.append(str(i))

#print(wav_file_name)

# print(path(wav_file_name[0]).stat().st_size())
#print(list(path.glob('*.wav')))
name =[]
for i in dir:
    i = str(i)
    #print(i)
    split = i.split('\\')
    name.append(split[1])

print(name)
"""
for i in name:
    wav_file_size.append(path(i).stat().st_size)
"""
print(os.getcwd())

print(os.path.getsize('0000003b8fd9bc22877135b42b04c49d4860312b001be688723ecc5d.wav'))
# print(path('0000003b8fd9bc22877135b42b04c49d4860312b001be688723ecc5d.wav').stat().st_size())
for i in name:
    wav_file_size.append(os.path.getsize(i))

#print(wav_file_size)
#print(wav_file_name)

path1 = Path('C:\\Users\\Suvetha Devi\\PycharmProjects\\PythonCodes\\DL-TRIZ\\nptel-pure\corrected_txt')
print(path1.cwd())

file = list(path1.glob('*.txt'))
#print(file)
files =[]
for i in file:
    files.append(str(i))

#print(files)

name_conversion = []
for i in name:
    name_conversion.append(i.replace('.wav', '.txt'))

#print(name_conversion)

for i in file:
    with open(i) as f:
        content = f.read()
        wav_transcript.append(content)
    f.close()

#print(wav_transcript)

dataset = pd.DataFrame(zip(wav_file_name, wav_file_size, wav_transcript), columns=['wav_filename', 'wav_filesize', 'transcript'])

print(dataset.head())

path2 = Path('C:\\Users\\Suvetha Devi\\PycharmProjects\\PythonCodes\\DL-TRIZ')
os.chdir(path2)

dataset.to_csv('deepspeech1.csv', index=False)


