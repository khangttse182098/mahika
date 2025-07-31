import sounddevice as sd
import keyboard
import numpy as np
from scipy.io.wavfile import write
from src.core.stt import Stt
import threading
import time

class AudioRecorder:
    def __init__(self):
        self.fs = 44100
        self.channels = 1
        self.output_file = "./src/utils/audio/user_prompt.wav"
        self.recording = []
        self.is_recording = False
        self.stream = None
        
    def start_recording(self):
        """Start recording audio"""
        if self.is_recording:
            return
            
        self.is_recording = True
        self.recording = []
        
        def record_callback():
            with sd.InputStream(samplerate=self.fs, channels=self.channels, dtype='float32') as stream:
                self.stream = stream
                while self.is_recording:
                    try:
                        data, overflowed = stream.read(int(self.fs * 0.1))
                        if not overflowed and self.is_recording:
                            self.recording.append(data)
                    except Exception as e:
                        print(f"Recording error: {e}")
                        break
        
        # Start recording in a separate thread
        self.record_thread = threading.Thread(target=record_callback, daemon=True)
        self.record_thread.start()
        
    def stop_recording(self):
        """Stop recording and save to file"""
        if not self.is_recording:
            return None
            
        self.is_recording = False
        
        # Wait a bit for the recording thread to finish
        time.sleep(0.2)
        
        if self.recording:
            try:
                recording_data = np.concatenate(self.recording, axis=0)
                write(self.output_file, self.fs, recording_data)
                print(f"Saved recording to {self.output_file}")
                return self.output_file
            except Exception as e:
                print(f"Error saving recording: {e}")
                return None
        else:
            print("No recording data")
            return None
    
    @staticmethod
    def get_record_text():
        fs = 44100  
        channels = 1  
        output_file = "./src/utils/audio/user_prompt.wav"
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
        except Exception as e:
            print(f"Error: {e}")
            return None