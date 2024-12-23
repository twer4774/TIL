from gtts import gTTS
from pydub import AudioSegment

# 변환할 텍스트 (10초 정도 분량)
text = "This is a sample audio file with 10 seconds of speech for testing purposes."

# 텍스트를 음성으로 변환
tts = gTTS(text, lang="en")

# WAV 파일로 임시 저장
wav_filename = "temp.wav"
tts.save(wav_filename)

# WAV -> FLAC 변환 및 16kHz로 샘플링
flac_filename = "sample1.flac"
audio = AudioSegment.from_file(wav_filename, format="wav")
audio = audio.set_frame_rate(16000)  # 16kHz로 변환
audio.export(flac_filename, format="flac")

print(f"FLAC 파일 생성 완료: {flac_filename}")
