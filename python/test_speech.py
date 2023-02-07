import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Скажите что-нибудь...')
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)


query = r.recognize_google(audio, language='ru-RU')
print('Вы сказали: ' + query.lower())
