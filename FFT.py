import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Step 1: Load the WAV file
file_path = '17000.wav'
y, sr = librosa.load(file_path, sr=None)  # y is the audio time series, sr is the sample rate

# Step 2: Compute the STFT
stft_result = librosa.stft(y, n_fft=2048, hop_length=512)

# Step 3: Convert the STFT result to decibels (for better visualization)
stft_db = librosa.amplitude_to_db(np.abs(stft_result), ref=np.max)

# Step 4: Plot the STFT
plt.figure(figsize=(12, 6))
librosa.display.specshow(stft_db, sr=sr, hop_length=512, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('STFT of the WAV file')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()
