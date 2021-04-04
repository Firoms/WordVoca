파이썬을 기반으로 한 어휘 반복 듣기 단어장입니다.   
GUI(tkinter)를 이용하여 화면을 구성하였으며,   
gtts 라이브러리를 이용하여 문자를 음성으로 변환하였습니다.   
더 자연스럽고 좋은 음질을 위해 다양한 API도 고려해보았지만,   
당장은 무료로 이용할 수 있는 파이썬 라이브러리로 구성하였습니다.   

   ***
### ※ 주의 사항 
어휘추가.xlsx의 파일의 위치나 이름을 변경하면 정상적으로 작동하지 않을 수 있습니다.   
또한, exe 파일 실행시 사진 및 음악파일의 경로를 알맞게 위치시켜야 파일이 실행됩니다. (파일 위치를 변경할 때 주의해주세요)   
   ***

# Word_Voca - 어휘 반복 듣기 단어장
   단어를 추가하고 단어와 뜻을 음성으로 들려주는 프로그램입니다.   
   gtts 라이브러리의 무료 음성을 사용하여 음질이 그렇게 좋지는 않지만,   
   나름 제가 쓰기 편리한 구성의 단어장을 제작해 보았습니다.   
   텍스트를 mp3 파일로 변환하여 주는 gtts 모듈과 playsound 모듈을 이용하여 단어장을 구성하였습니다.   
***   
## 사용한 모듈 & 라이브러리
   1. tkinter   
   > GUI를 구성하기 위해 사용한 모듈입니다.
   2. threading
   > 여러 이벤트와 동작을 동시에 처리하기 위해 사용한 모듈입니다.
   3. sqlite3
   > 단어들을 저장하기 위해 사용한 Database 모듈입니다.
   4. pyglet
   > GUI에 폰트를 사용하기 위해 폰트를 추가해주는 모듈입니다.
   5. pillow
   > 이미지를 처리하기 위해 사용한 라이브러리 입니다.
   6. os
   > 사진 파일의 위치를 쉽게 지정해주기 위해 사용한 모듈입니다.
   7. pyinstaller
   > python 파일을 exe 파일로 변환하기 위해서 사용한 라이브러리입니다.
   8. time
   > 시간 지연을 이용하기 위해서 사용한 모듈입니다.
   9. multiprocessing
   > terminate를 이용하기 위해서 thread 대신 이용한 모듈입니다.
   10. gtts
   > 텍스트를 음성으로 변환하기 위해 사용한 라이브러리입니다.
   11. openpyxl
   > excel 파일의 내용을 받아오기 위해 사용한 모듈입니다.
   12. datetime
   > 현재 날짜와 시간을 받아오이 위해 사용한 모듈입니다.
***
## 기능