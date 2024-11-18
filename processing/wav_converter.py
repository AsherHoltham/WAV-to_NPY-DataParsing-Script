import librosa
import numpy as np

def converter(ifile, sr=22050, n_fft=2048, hop_length=512, use_log_scale=True):
    audio, sr = librosa.load(ifile, sr=sr)
    stft = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    
    if use_log_scale:
        output = librosa.amplitude_to_db(magnitude, ref=np.max)
    else:
        output = magnitude

    return output



    


    