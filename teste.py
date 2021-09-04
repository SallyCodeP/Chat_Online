import wave
import pyaudio
from threading import Thread







class Record:
    def __init__(self):
        self.number = 0
        self.stop = False
        
        self.audio = pyaudio.PyAudio()
        self.midia = self.audio.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True,frames_per_buffer=1024)
        
        Thread(target=self.stopfn).start()
        
        final_bytes = self.read_audio()
        self.read_audio(final_bytes)
        

    def record_audio(self):
        final_audio = []
        while True:
            data = self.midia.read(1024)
            self.final_audio.append(data)
            if self.stop:
                self.midia.stop_stream()
                self.midia.close()
                self.audio.terminate()
                return final_audio

    def stopfn(self):
        global stop
        while True:
            if not input('Press Enter >>>'):
                stop = True

    def read_audio(self, frame):
        waveFile = wave.open(f"Teste.wav{self.number}", 'wb')
        waveFile.setnchannels(2)
        waveFile.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(44100)
        waveFile.writeframes(b''.join(frame))
        waveFile.close()



Record()




