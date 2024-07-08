import wave

import ggwave
import pyaudio
import wave
import numpy as np

FRAMERATE = 48000


def play_bytes(data: bytes):
    p = pyaudio.PyAudio()

    # generate audio waveform for string "hello python"
    waveform = ggwave.encode(data.decode(), protocolId=1, volume=20)
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=48000, output=True, frames_per_buffer=4096)
    stream.write(waveform, len(waveform) // 4)
    stream.stop_stream()
    stream.close()

    p.terminate()


def listen_to_bytes():
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=48000, input=True, frames_per_buffer=1024)

    print('Listening ... Press Ctrl+C to stop')
    instance = ggwave.init()

    try:
        while True:
            data = stream.read(1024, exception_on_overflow=False)
            res = ggwave.decode(instance, data)
            if (not res is None):
                try:
                    print('Received text: ' + res.decode("utf-8"))
                except:
                    pass
    except KeyboardInterrupt:
        pass

    ggwave.free(instance)

    stream.stop_stream()
    stream.close()

    p.terminate()


# Load audio data from a file
def load_audio(filename):
    wf = wave.open(filename, 'rb')
    sample_rate = wf.getframerate()
    num_channels = wf.getnchannels()
    num_frames = wf.getnframes()
    audio_data = wf.readframes(num_frames)
    wf.close()
    return audio_data


def decode_to_file(filename):
    data = load_audio(filename)
    instance = ggwave.init()
    res = ggwave.decode(instance, data)
    if not res is None:
        try:
            print('Received text: ' + res.decode("utf-8"))
        except:
            pass


def main():
    decode_to_file('untitled.wav')


if __name__ == '__main__':
    main()
