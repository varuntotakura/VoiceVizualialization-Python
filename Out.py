import os
import pandas as pd
import librosa
import glob 
import matplotlib.pyplot as plt
import librosa.display

data, sampling_rate = librosa.load('output.wav')
plt.figure(figsize=(12, 4))
librosa.display.waveplot(data, sr=sampling_rate)
plt.title('Monophonic')
plt.show()