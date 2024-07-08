import ggwave
import wave


SAMPLE_RATE = 44100


def bytes_to_wave(data, filename):
    # Encode data into GGWave waveform
    waveform = ggwave.encode(data.decode())

    # Save waveform to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # mono
        wf.setsampwidth(2)  # 16-bit samples
        wf.setframerate(SAMPLE_RATE)  # 44.1kHz sample rate
        wf.writeframes(waveform)


def wave_to_bytes(filename):
    # Read waveform from a WAV file
    with wave.open(filename, 'rb') as wf:
        waveform = wf.readframes(wf.getnframes())

    # Decode the waveform into data
    instance = ggwave.init()
    data = ggwave.decode(instance, waveform)
    return data


# Example usage
print(wave_to_bytes('untitled.wav'))
