import whisper

def transcribe_audio(audio_path):
    # Load the model
    model = whisper.load_model("base")  # You can choose different model sizes like "tiny", "small", "medium", or "large"

    # Load and transcribe the audio
    result = model.transcribe(audio_path)
    print("Transcription:", result['text'])

# Example usage
transcribe_audio("path/to/your/audio/file.mp3")
