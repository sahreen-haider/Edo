import whisper
from pathlib import Path
from openai import OpenAI
import os
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)




os.environ["OPENAI_API_KEY"] = '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'

client = OpenAI()
model = whisper.load_model('tiny')

def get_audio(sample_path):
    result = model.transcribe(sample_path)
    return result["text"]

# def get_text(sample_path):
#     audio = whisper.load_audio(sample_path)
#     audio = whisper.pad_or_trim(audio)

#     mel = whisper.log_mel_spectrogram(audio).to(model.device)

#     _, probs = model.detect_language(mel)
#     options = whisper.DecodingOptions()
#     results = whisper.decode(model, mel, options)

#     with open ("trans_text.txt", 'w+') as f:
#         f.write(results.text)



def tts(text_response):
    # speech_file_path = Path(__file__).parent / "audio_data/response.ogg"
    response = client.audio.speech.create(
        model = 'tts-1',
        voice = 'onyx',
        input = text_response
    )
    return response.stream_to_file( "audio_data/response.ogg")
