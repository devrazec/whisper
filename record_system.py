import sounddevice as sd
import soundfile as sf

DEVICE_NAME = "BlackHole 2ch"
SAMPLE_RATE = 44100

def find_device(name):
    for i, device in enumerate(sd.query_devices()):
        if name.lower() in device["name"].lower():
            return i
    raise Exception(f"Device '{name}' not found")

device = find_device(DEVICE_NAME)

print("Recording... Press Ctrl+C to stop")

with sf.SoundFile(
    "record_system.wav",
    mode="w",
    samplerate=SAMPLE_RATE,
    channels=2
) as file:

    def callback(indata, frames, time, status):
        file.write(indata)

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        device=device,
        channels=2,
        callback=callback
    ):
        while True:
            sd.sleep(1000)