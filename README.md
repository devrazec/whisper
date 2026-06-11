# whisper
Whisper Project

python3.11 -m venv venv

. venv/bin/activate

python -m pip install load_dotenv

python -m pip install --upgrade pip setuptools wheel

pip install "numpy<2" "llvmlite==0.44.0"

pip install openai-whisper



-- Youtube
pip install yt-dlp

-- Computer System Audio

brew install blackhole-2ch

pip install sounddevice soundfile


# Install Dependencies 

pipenv install -r requirements.txt 

pipenv freeze > requirements.txt

# Commands

python3.11 model.py

python3.11 transcribe_mp3.py

python3.11 check_device.py
0 RTK FHD HDR
1 JBL TUNE 310C USB-C
2 JBL TUNE 310C USB-C
3 BlackHole 2ch
4 MacBook Pro Microphone
5 MacBook Pro Speakers
6 Multi-Output Device

python3.11 transcribe_youtube.py

python3.11 transcribe_system.py

python3.11 record_system.py

python3.11 transcribe_wav.py



