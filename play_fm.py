import time

import pyaudio
import numpy as np

def play_frequency(frequency, amplitude=1.0, duration=1.0, sample_rate=44100):
    p = pyaudio.PyAudio()

    # Generate samples
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    samples = (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.float32)

    # Open stream
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Play samples
    stream.write(samples.tobytes())

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio interface
    p.terminate()

if __name__ == "__main__":
    data = '011001'
    freq = 19000

    for bit in data:
        if bit == '0':
            time.sleep(1.0)
        elif bit == '1':
            play_frequency(freq, 1, 1.0)
