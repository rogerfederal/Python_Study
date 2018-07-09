import speech_recognition


r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = r.listen(source)
print(r.recognize_google(audio, language='zh-CN'))
