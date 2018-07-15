from gtts import gTTS
from pygame import mixer
import tempfile
import speech_recognition
mixer.init()

def listento():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = r.listen(source)
    return r.recognize_google(audio, language='en')


def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='en')
        tts.save("/Users/StephenChou/Desktop/hello.mp3")
        mixer.music.load("/Users/StephenChou/Desktop/hello.mp3")
        mixer.music.play()


speak(listento())