import tkinter.messagebox
import time
import os
import pyglet
import threading
from Make_label import Get_label
from playsound import playsound
from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
from db import *
from gtts import gTTS
from playsound import playsound

python_path = os.path.join(os.getcwd())


class Gui:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Word Voca")
        self.gui.geometry("804x804")
        self.gui.resizable(width=False, height=False)
        execute_location = self.center_window(804, 804)
        self.en_word_thread = threading.Thread(target=self.no_action)
        self.en_word_thread.start()
        self.ko_word_thread = threading.Thread(target=self.no_action)
        self.ko_word_thread.start()
        self.Menu_Screen()
        self.gui.mainloop()

    def destroy(self):
        for l in self.gui.place_slaves():
            l.destroy()

    def center_window(self, width, height):
        scr_width = self.gui.winfo_screenwidth()
        scr_height = self.gui.winfo_screenheight()
        x = (scr_width / 2) - (width / 2)
        y = (scr_height / 2) - (height / 2) - 25
        self.gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def no_action(self):
        pass

    def quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.gui.quit()
            self.gui.destroy()
            exit()

    def Menu_Screen(self):
        self.destroy()
        self.stop = "no"
        Menu_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/menu_bg.png"), 0, 0
        )
        Add_E_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add_E_btn.png"),
            20,
            450,
            self.Add_en_Screen,
        )
        Li_E_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/li_E_btn.png"),
            275,
            450,
            self.Li_en_Screen,
        )
        See_A_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/see_A_btn.png"),
            530,
            450,
            self.See_All_Screen,
        )
        Add_K_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add_K_btn.png"),
            20,
            600,
            self.Add_ko_Screen,
        )
        Li_K_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/li_K_btn.png"),
            275,
            600,
            self.Li_ko_Screen,
        )
        Exit_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/exit_btn.png"),
            530,
            600,
            self.quit,
        )

    def Add_en_Screen(self):
        self.destroy()
        add_E_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/add_E_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/return_btn.png"),
            590,
            30,
            self.Menu_Screen,
        )
        self.word_entry = tkinter.Text(self.gui, width=15, height=1)
        self.word_entry.place(x=250, y=450)
        self.word_entry.config(font=("고도 M", 45))
        self.content_entry = tkinter.Text(self.gui, width=15, height=1)
        self.content_entry.place(x=250, y=570)
        self.content_entry.config(font=("고도 M", 45))
        add_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add.png"),
            200,
            700,
            lambda: self.add_btn("en"),
        )
        cancle_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/cancle.png"),
            450,
            700,
            self.Add_en_Screen,
        )

    def add_btn(self, lang):
        self.word_entry.config(state="disabled")
        self.content_entry.config(state="disabled")
        self.word = self.word_entry.get("1.0", "end")
        self.word = self.word.strip()
        self.content = self.content_entry.get("1.0", "end")
        self.content = self.content.strip()
        add_db(lang, self.word, self.content)
        success_message = tkinter.messagebox.showinfo("추가 완료", "추가가 완료되었습니다.")
        if lang == "en":
            self.Add_en_Screen()
        elif lang == "ko":
            self.Add_ko_Screen()
        else:
            self.Menu_Screen()

    def Li_en_Screen(self):
        self.destroy()
        self.stop = "en"
        li_E_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/li_E_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/return_btn.png"),
            590,
            30,
            self.Menu_Screen,
        )
        if not self.en_word_thread.is_alive():
            self.en_word_thread = threading.Thread(
                target=lambda: self.repeat_word("en")
            )
            self.en_word_thread.daemon = True
            self.en_word_thread.start()
        else:
            word_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                190,
                f"{self.cur[0]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 50),
            )
            word_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                480,
                f"{self.cur[1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 50),
            )

    def repeat_word(self, lang):
        words = get_ran_word(lang)
        if len(words) == 0:
            error_message = tkinter.messagebox.showinfo("단어 없음", "단어를 먼저 추가해주세요.")
            self.Menu_Screen()
            return
        while self.stop == lang:
            if len(words) == 0:
                words = get_ran_word(lang)
            self.cur = words.pop()
            word_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                190,
                f"{self.cur[0]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 50),
            )
            word_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                480,
                f"{self.cur[1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 50),
            )
            if self.stop != lang:
                break
            tts1 = gTTS(text=self.cur[0], lang=lang)
            try:
                os.remove("word.mp3")
            except:
                pass
            tts1.save("word.mp3")
            playsound("word.mp3")
            if self.stop != lang:
                break
            time.sleep(1)
            if self.stop != lang:
                break
            tts2 = gTTS(text=self.cur[1], lang="ko")
            try:
                os.remove("content.mp3")
            except:
                pass
            tts2.save("content.mp3")
            playsound("content.mp3")
            if self.stop != lang:
                break
            time.sleep(1)

    def See_All_Screen(self):
        self.destroy()
        see_A_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/see_A_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/return_btn.png"),
            590,
            30,
            self.Menu_Screen,
        )
        left_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/left.png"),
            350,
            50,
            self.no_action,
        )
        right_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/right.png"),
            450,
            50,
            self.no_action,
        )
        self.Intro1 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa1-1.png"),
            19,
            140,
            self.no_action,
            f"번호",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa2-1.png"),
            78,
            140,
            self.no_action,
            f"분류",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa3-1.png"),
            170,
            140,
            self.no_action,
            f"내용",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa4-1.png"),
            397,
            140,
            self.no_action,
            f"뜻",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa5-1.png"),
            624,
            140,
            self.no_action,
            f"등록일",
            "#472f91",
            ("고도 M", 12),
        )
        for i in range(15):
            li1 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa1-2.png"),
                19,
                185 + (40 * i),
                f"{i+1}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa2-2.png"),
                78,
                185 + (40 * i),
                f" ",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa3-2.png"),
                170,
                185 + (40 * i),
                f" ",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa4-2.png"),
                397,
                185 + (40 * i),
                f" ",
                "#472f91",
                ("고도 M", 12),
            )
            li5 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa5-2.png"),
                624,
                185 + (40 * i),
                f" ",
                "#472f91",
                ("고도 M", 12),
            )
            del_btn = Get_label.image_button(
                self.gui,
                os.path.join(python_path, "../../images/delete.png"),
                753,
                185 + (40 * i),
                self.no_action,
            )

    def Add_ko_Screen(self):
        self.destroy()
        add_K_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/add_K_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/return_btn.png"),
            590,
            30,
            self.Menu_Screen,
        )
        self.word_entry = tkinter.Text(self.gui, width=15, height=1)
        self.word_entry.place(x=250, y=450)
        self.word_entry.config(font=("고도 M", 45))
        self.content_entry = tkinter.Text(self.gui, width=15, height=1)
        self.content_entry.place(x=250, y=570)
        self.content_entry.config(font=("고도 M", 45))
        add_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add.png"),
            200,
            700,
            lambda: self.add_btn("ko"),
        )
        cancle_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/cancle.png"),
            450,
            700,
            self.Add_ko_Screen,
        )

    def Li_ko_Screen(self):
        self.destroy()
        self.stop = "ko"
        li_K_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/li_K_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/return_btn.png"),
            590,
            30,
            self.Menu_Screen,
        )
        if not self.ko_word_thread.is_alive():
            self.ko_word_thread = threading.Thread(
                target=lambda: self.repeat_word("ko")
            )
            self.ko_word_thread.daemon = True
            self.ko_word_thread.start()
        else:
            word_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                190,
                f"{self.cur[0]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 50),
            )
            word_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                480,
                f"{self.cur[1]}",
                "#0051C9",
                ("1훈떡볶이 Regular", 50),
            )


if __name__ == "__main__":
    execute = Gui()
