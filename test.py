# from gtts import gTTS
# from playsound import playsound
# text1 ="Hi, everybody. Playing with Python is fun!!!"

# tts = gTTS(text=text1, lang='en')
# tts.save("helloEN.mp3")
# playsound("helloEN.mp3")
# text2 ="안녕하세요, 여러분. 파이썬으로 노는 것은 재미있습니다!!!"

# tts = gTTS(text=text2, lang='ko')
# tts.save("helloKO.mp3")
# playsound("helloKO.mp3")


import requests
import json

url = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'
body = '<speak> 그는 그렇게 말했습니다. \
        <voice name="MAN_DIALOG_BRIGHT">잘 지냈어? 나도 잘 지냈어.</voice> \
        <voice name="WOMAN_DIALOG_BRIGHT" speechStyle="SS_ALT_FAST_1">금요일이 좋아요.</voice> </speak>'
headers = {
    'Content-Type': 'application/xml',
    'Authorization': 'KakaoAK c1702abfa4758f212a4f77684968eda9',
    }

r = requests.post(url, data=json.dumps(body), headers=headers)
print(r)