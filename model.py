import whisper

print("Downloading...")
model = whisper.load_model("tiny.en")
model = whisper.load_model("base.en")
model = whisper.load_model("small.en")
model = whisper.load_model("medium.en")

print("Done!")
print(whisper._MODELS.keys())

#'tiny.en', 
# 'tiny', 72.1M
#'base.en', 
# 'base', 139M
#'small.en', 
# 'small', 461M
#'medium.en', 
# 'medium', 1.42G
#'large-v1', 'large-v2', 
#'large-v3', 'large', 
#'large-v3-turbo',
#'turbo' 1.51G