import sounddevice as sd
import wavio
import datetime
import keyboard

def get_file_name():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    return f"recording_{timestamp}.wav" 

def start_recording():
    recording = []
    print("PRESS [S] KEY TO START RECORDING AND [E] TO END RECODING")

    while True:

        if keyboard.is_pressed('s') and not recording:
            print("RECORDING...")
            recording = sd.rec(44100, samplerate= 44100, channels= 1 , dtype='int16')

        elif keyboard.is_pressed('e') and len(recording) > 0:
            print("\nRECORDING STOPPED\n")
            break
        
        if len(recording) > 0:
            print("RECORDING...")

    sd.wait()

    file_name = get_file_name()
    wavio.write(file_name, recording, 44100, sampwidth=2)
    print(f'AUDIO SAVED AS [{file_name}]\nse')


start_recording()
