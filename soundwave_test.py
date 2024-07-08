import ggwave
import pyaudio


def play_bytes(data: bytes):
    p = pyaudio.PyAudio()

    # generate audio waveform for string "hello python"
    waveform = ggwave.encode(data.decode(), protocolId=1, volume=20)

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=48000, output=True, frames_per_buffer=4096)
    stream.write(waveform, len(waveform) // 4)
    stream.stop_stream()
    stream.close()

    p.terminate()


def decode_audio():
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


def main():
    decode_audio()


if __name__ == '__main__':
    main()
