import sounddevice as sd
import keyboard
import numpy as np
from scipy.io.wavfile import write
from src.core.stt import Stt

class AudioRecorder:
    @staticmethod
    def get_record_text():
        fs = 44100  
        channels = 1  
        output_file = "./src/utils/audio/output.wav"
        
        print("Hold space to record, release to stop...")
        try:
            # Wait for spacebar press
            keyboard.wait("space")
            print("Recording...")
            recording = []
            with sd.InputStream(samplerate=fs, channels=channels, dtype='float32') as stream:
                while keyboard.is_pressed("space"):
                    data, overflowed = stream.read(int(fs * 0.1)) 
                    if not overflowed:
                        recording.append(data)
            
            print("End recording")
            if recording:
                recording = np.concatenate(recording, axis=0)
                write(output_file, fs, recording)
                print(f"Saved to {output_file}")
                stt = Stt()
                print("--------------------------------")
                stt.load_model()
                return stt.transcribe(output_file)
            else:
                print("No recording")
                return None
        except KeyboardInterrupt:
            print("Stopped by user")
        except Exception as e:
            print(f"Error: {e}")