import yt_dlp
import whisper
from pathlib import Path

url = "https://www.youtube.com/watch?v=vOuhs1mA0xo"

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "youtube_audio.%(ext)s",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

model = whisper.load_model("small.en")

result = model.transcribe(
    "youtube_audio.webm",
    language="en",
    fp16=False
)

text = result["text"]

Path("transcript.txt").write_text(text, encoding="utf-8")

print(text)
print("\nSaved to transcript_youtube.txt")