import queue
import tempfile
from pathlib import Path

import numpy as np
import sounddevice as sd
import soundfile as sf
import whisper

DEVICE_NAME = "BlackHole 2ch"
SAMPLE_RATE = 16000
CHUNK_SECONDS = 5
OUTPUT_FILE = Path("transcript_system.txt")

audio_queue = queue.Queue()

def has_audio(audio, threshold=0.01):
    volume = np.sqrt(np.mean(audio ** 2))
    return volume > threshold

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

def find_device(name):
    for index, device in enumerate(sd.query_devices()):
        if name.lower() in device["name"].lower():
            return index
    raise RuntimeError(f"Device not found: {name}")

def main():

    # Start with a clean transcript file
    OUTPUT_FILE.write_text("", encoding="utf-8")

    print("\033c", end="")

    device_index = find_device(DEVICE_NAME)

    print("Loading Whisper model...")
    model = whisper.load_model("small.en")

    print(f"Listening to {DEVICE_NAME}...")
    print(f"Saving transcript to {OUTPUT_FILE.resolve()}")

    buffer = []

    with sd.InputStream(
        device=device_index,
        channels=2,
        samplerate=SAMPLE_RATE,
        callback=audio_callback,
    ):
        while True:
            data = audio_queue.get()
            mono = np.mean(data, axis=1)
            buffer.append(mono)

            total_samples = sum(len(x) for x in buffer)

            if total_samples >= SAMPLE_RATE * CHUNK_SECONDS:
                audio = np.concatenate(buffer)
                buffer.clear()

                if not has_audio(audio):
                    continue

                with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
                    sf.write(tmp.name, audio, SAMPLE_RATE)

                    result = model.transcribe(
                        tmp.name,
                        language="en",
                        fp16=False,
                        condition_on_previous_text=False,
                        no_speech_threshold=0.6,
                        #temperature=0,
                    )

                text = result["text"].strip()

                if text:
                    print(text)
                    with OUTPUT_FILE.open("a", encoding="utf-8") as f:
                        f.write(text + "\n")

if __name__ == "__main__":
    main()