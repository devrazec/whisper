import whisper
from pathlib import Path

audio_file = "record_system.wav"  # change this to your file

model = whisper.load_model("small.en")  # good option for Intel Mac + English

result = model.transcribe(
    audio_file,
    language="en",
    fp16=False
)

text = result["text"]

Path("transcript_wav.txt").write_text(text, encoding="utf-8")

print(text)
print("\nSaved to transcript_wav.txt")