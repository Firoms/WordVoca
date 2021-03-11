from gtts import gTTS
from playsound import playsound

text1 = "Hi, everybody. Playing with Python is fun"

tts = gTTS(text=text1, lang="en")
tts.save("helloEN.mp3")
playsound("helloEN.mp3")
text2 = "안녕하세요, 여러분. 파이썬으로 노는 것은 재미있습니다"

tts = gTTS(text=text2, lang="ko")
tts.save("helloKO.mp3")
playsound("helloKO.mp3")


import requests
import json

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
body = '<speak>\
 <voice name="WOMAN_READ_CALM"> 지금은 여성 차분한 낭독체입니다.</voice>\
 <voice name="MAN_READ_CALM"> 지금은 남성 차분한 낭독체입니다.</voice>\
 <voice name="WOMAN_DIALOG_BRIGHT"> 안녕하세요. 여성 밝은 대화체예요.</voice>\
 <voice name="MAN_DIALOG_BRIGHT"> 안녕하세요. 남성 밝은 대화체예요.</voice>\
 </speak>\
'

headers = {
    "Content-Type": "application/xml",
    "Authorization": "KakaoAK c1702abfa4758f212a4f77684968eda9",
}

r = requests.post(url, data=body.encode("utf-8"), headers=headers)

with open("result.mp3", "wb") as f:
    f.write(r.content)

playsound("result.mp3")


# url = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'
# body ='<speak>\
#  <voice name="WOMAN_READ_CALM"> Hi im calm. </voice>\
#  <voice name="MAN_READ_CALM"> Hi im calm. </voice>\
#  <voice name="WOMAN_DIALOG_BRIGHT"> Hi im bright. </voice>\
#  <voice name="MAN_DIALOG_BRIGHT"> Hi im bright. </voice>\
#  </speak>\
# '

# headers = {
#     'Content-Type': 'application/xml',
#     'Authorization': 'KakaoAK c1702abfa4758f212a4f77684968eda9',
#     }

# r = requests.post(url, data=body, headers=headers)

# with open('resul2t.mp3', 'wb') as f:
#     f.write(r.content)

# playsound("result2.mp3")
