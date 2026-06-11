import whisper
from pathlib import Path

audio_file = "./mp3/1.mp3"  # change this to your file

model = whisper.load_model("small.en")  # good option for Intel Mac + English

result = model.transcribe(
    audio_file,
    language="en",
    fp16=False
)

text = result["text"]

Path("transcript.txt").write_text(text, encoding="utf-8")

print(text)
print("\nSaved to transcript_mp3.txt")