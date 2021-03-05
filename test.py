from gtts import gTTS
from playsound import playsound
text1 ="Hi, everybody. Playing with Python is fun!!!"

tts = gTTS(text=text1, lang='en')
tts.save("helloEN.mp3")
playsound("helloEN.mp3")
text2 ="안녕하세요, 여러분. 파이썬으로 노는 것은 재미있습니다!!!"

tts = gTTS(text=text2, lang='ko')
tts.save("helloKO.mp3")
playsound("helloKO.mp3")