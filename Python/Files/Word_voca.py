import tkinter.messagebox
import time
import os
import pyglet
import threading
import multiprocessing
from Make_label import Get_label
from playsound import playsound
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import *
from playsound import playsound

python_path = os.path.join(os.getcwd())


class Gui:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Word Voca")
        self.gui.geometry("804x804")
        self.gui.resizable(width=False, height=False)
        pyglet.font.add_file("../../Fonts/GodoM.otf")
        pyglet.font.add_file("../../Fonts/HoonDdukbokki.ttf")
        execute_location = self.center_window(804, 804)
        self.gui.iconbitmap("../../Images/logo.ico")
        self.word_thread = threading.Thread(target=self.no_action)
        self.word_thread.start()
        self.num = 0
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
        if answer:
            self.gui.quit()
            self.gui.destroy()
            exit()

    def Menu_Screen(self):
        self.destroy()
        self.num += 1
        Menu_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/menu_bg.png"), 0, 0
        )
        Version_label = Label(
            self.gui,
            text="ver.2.0",
            fg="yellow",
            bg="purple",
            font=("1훈떡볶이 Regular", 18),
            height=1,
        )
        Version_label.place(x=720, y=10)
        Add_en_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add_en_btn.png"),
            20,
            450,
            lambda: self.Add_Screen("en"),
        )
        Li_en_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/li_en_btn.png"),
            275,
            450,
            lambda: self.Li_Screen("en"),
        )
        See_A_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/see_A_btn.png"),
            530,
            450,
            lambda: self.See_All_Screen(1, ["Seq", True]),
        )
        Add_ko_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add_ko_btn.png"),
            20,
            600,
            lambda: self.Add_Screen("ko"),
        )
        Li_ko_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/li_ko_btn.png"),
            275,
            600,
            lambda: self.Li_Screen("ko"),
        )
        Exit_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/exit_btn.png"),
            530,
            600,
            self.quit,
        )

    def Add_Screen(self, lang):
        self.destroy()
        add_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, f"../../images/add_{lang}_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/return_btn.png"),
            590,
            30,
            self.Menu_Screen,
        )
        add_excel_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add_excel.png"),
            450,
            30,
            self.add_excel_btn,
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
            lambda: self.add_btn(lang),
        )
        cancle_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/cancle.png"),
            450,
            700,
            lambda: self.Add_Screen(lang),
        )

    def add_excel_btn(self):
        answer = messagebox.askyesno(
            "대량 추가", "어휘추가.xlsx에 있는 내용들을 대량으로 추가하시겠습니까?\n (이후에는 되돌릴 수 없습니다.)"
        )
        if answer:
            try:
                result, error = add_excel_file()
            except:
                error_message = tkinter.messagebox.showinfo(
                    "대량 추가 불가",
                    f"Excel 파일을 읽어들일 수 없어 오류가 발생했습니다. \n 저장되었는지, Excel 파일을 닫았는지, 정확한 이름과 위치에 있는지 확인해주십시오.",
                )
                return
            success_message = tkinter.messagebox.showinfo(
                "추가 완료", f"{result[0]-4}번 {result[1]} {result[2]}까지 추가가 완료되었습니다."
            )
            if error:
                error_message = tkinter.messagebox.showinfo(
                    "내용 삭제 불가",
                    f"Excel 파일이 실행되고 있어 Excel 파일의 내용을 삭제하지 못했습니다. \n 다음 대량 추가 시에 수동으로 삭제하고 입력해주세요.",
                )

    def add_btn(self, lang):
        self.word = self.word_entry.get("1.0", "end")
        self.word = self.word.strip()
        self.content = self.content_entry.get("1.0", "end")
        self.content = self.content.strip()
        if self.word and self.content:
            self.word_entry.config(state="disabled")
            self.content_entry.config(state="disabled")
            add_db(lang, self.word, self.content)
            success_message = tkinter.messagebox.showinfo("추가 완료", "추가가 완료되었습니다.")
            self.Add_Screen(lang)
        else:
            failed_message = tkinter.messagebox.showinfo("입력 없음", "단어와 내용을 모두 입력해주세요.")

    def Li_Screen(self, lang):
        self.destroy()
        li_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, f"../../images/li_{lang}_bg.png"), 0, 0
        )
        Return_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/return_btn.png"),
            590,
            30,
            self.Menu_Screen,
        )
        self.repeat1 = ttk.Combobox(
            self.gui,
            width=5,
            height=1,
            values=(" 0번", " 1번", " 2번", " 3번", " 4번", " 5번"),
            state="readonly",
            font=("고도 M", 24),
        )
        self.repeat1.place(x=660, y=285)
        self.repeat1.current(1)
        self.sleep1 = ttk.Combobox(
            self.gui,
            width=5,
            height=1,
            values=("0.0초", "0.3초", "0.5초", "0.8초", "1.0초", "1.5초", "2.0초", "3.0초"),
            state="readonly",
            font=("고도 M", 24),
        )
        self.sleep1.place(x=660, y=400)
        self.sleep1.current(2)
        self.repeat2 = ttk.Combobox(
            self.gui,
            width=5,
            height=1,
            values=(" 0번", " 1번", " 2번", " 3번", " 4번", " 5번"),
            state="readonly",
            font=("고도 M", 24),
        )
        self.repeat2.place(x=660, y=565)
        self.repeat2.current(1)
        self.repeat2.config(font=("고도 M", 24))
        self.sleep2 = ttk.Combobox(
            self.gui,
            width=5,
            height=1,
            values=("0.0초", "0.3초", "0.5초", "0.8초", "1.0초", "1.5초", "2.0초", "3.0초"),
            state="readonly",
            font=("고도 M", 24),
        )
        self.sleep2.place(x=660, y=680)
        self.sleep2.current(2)
        self.num += 1
        self.word_thread = threading.Thread(
            target=lambda: self.repeat_word(lang, False, self.num), daemon=True
        )
        self.word_thread.start()

    def change_thread(self, lang, rev):
        self.num += 1
        self.word_thread = threading.Thread(
            target=lambda: self.repeat_word(lang, rev, self.num), daemon=True
        )
        self.word_thread.start()

    def repeat_word(self, lang, rev, num):
        Reverse_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/reverse_btn.png"),
            500,
            30,
            lambda: self.change_thread(lang, not rev),
        )
        words = get_ran_word(lang)
        if len(words) == 0:
            error_message = tkinter.messagebox.showinfo("단어 없음", "단어를 먼저 추가해주세요.")
            self.Menu_Screen()
            return
        while self.num == num:
            if len(words) == 0:
                words = get_ran_word(lang)
            self.cur = words.pop()
            if rev == True:
                word1, word2 = self.cur[1], self.cur[0]
                seq_num1, seq_num2 = 2, 1
            else:
                word1, word2 = self.cur[0], self.cur[1]
                seq_num1, seq_num2 = 1, 2
            if self.num != num:
                break
            word1_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                205,
                f"{word1}",
                "#0051C9",
                ("1훈떡볶이 Regular", 30),
            )
            word1_label.configure(wraplength="550")
            word2_label = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../Images/word_bg.png"),
                50,
                480,
                f"{word2}",
                "#0051C9",
                ("1훈떡볶이 Regular", 30),
            )
            word2_label.configure(wraplength="550")
            if self.num != num:
                break
            try:
                for _ in range(int(self.repeat1.get()[1])):
                    p = multiprocessing.Process(
                        target=playsound,
                        args=(f"../../Sound/{self.cur[2]}_{seq_num1}.mp3",),
                        daemon=True,
                    )
                    p.start()
                    while p.is_alive():
                        time.sleep(0.1)
                        if self.num != num:
                            p.terminate()
                    time.sleep(float(self.sleep1.get()[:3]))
                    if self.num != num:
                        break
                for _ in range(int(self.repeat2.get()[1])):
                    p = multiprocessing.Process(
                        target=playsound,
                        args=(f"../../Sound/{self.cur[2]}_{seq_num2}.mp3",),
                        daemon=True,
                    )
                    p.start()
                    while p.is_alive():
                        time.sleep(0.1)
                        if self.num != num:
                            p.terminate()
                    time.sleep(float(self.sleep2.get()[:3]))
                    if self.num != num:
                        break
            except:
                pass

    def See_All_Screen(self, page, sort):
        self.destroy()
        word_num = get_word_num()
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
            lambda: self.See_All_Screen(page - 1, sort),
        )
        if page == 1:
            left_button.config(state="disabled")
        right_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/right.png"),
            450,
            50,
            lambda: self.See_All_Screen(page + 1, sort),
        )
        if word_num <= page * 15:
            right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa1-1.png"),
            19,
            140,
            lambda: self.See_All_Screen(1, ["Seq", True]),
            f"번호",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa2-1.png"),
            78,
            140,
            lambda: self.See_All_Screen(1, ["Type", not sort[1]]),
            f"분류",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa3-1.png"),
            170,
            140,
            lambda: self.See_All_Screen(1, ["Word", not sort[1]]),
            f"내용",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa4-1.png"),
            397,
            140,
            lambda: self.See_All_Screen(1, ["Content", not sort[1]]),
            f"뜻",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self.gui,
            os.path.join(python_path, "../../images/sa5-1.png"),
            624,
            140,
            lambda: self.See_All_Screen(1, ["Date", not sort[1]]),
            f"등록일",
            "#472f91",
            ("고도 M", 12),
        )
        data = get_all_words(sort)
        data_num = word_num - (page - 1) * 15
        if data_num > 15:
            data_num = 15
        del_btn_li = [i for i in range(data_num)]
        for i in range(data_num):
            data_index = (page - 1) * 15 + i
            li1 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa1-2.png"),
                19,
                185 + (40 * i),
                f"{data_index+1}",
                "#472f91",
                ("고도 M", 12),
            )
            word_type = data[data_index][1]
            if word_type == "en":
                word_type = "ENG"
            elif word_type == "ko":
                word_type = "KOR"
            li2 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa2-2.png"),
                78,
                185 + (40 * i),
                f"{word_type}",
                "#472f91",
                ("고도 M", 12),
            )
            word = data[data_index][2][:25]
            li3 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa3-2.png"),
                170,
                185 + (40 * i),
                f"{word}",
                "#472f91",
                ("고도 M", 12),
            )
            content = data[data_index][3][:15]
            li4 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa4-2.png"),
                397,
                185 + (40 * i),
                f"{content}",
                "#472f91",
                ("고도 M", 12),
            )
            date = data[data_index][4].split()[0]
            li5 = Get_label.image_label_text(
                self.gui,
                os.path.join(python_path, "../../images/sa5-2.png"),
                624,
                185 + (40 * i),
                f"{date}",
                "#472f91",
                ("고도 M", 12),
            )
            seq = data[data_index][0]
            self.make_del_btn(i, seq)

    def make_del_btn(self, i, seq):
        del_btn = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/delete.png"),
            753,
            185 + (40 * i),
            lambda: self.delete_btn(seq),
        )

    def delete_btn(self, seq):
        print(seq)
        answer = messagebox.askyesno("단어 삭제", "정말 단어를 삭제하시겠습니까?")
        if answer == True:
            delete_word(seq)
            finish_message = tkinter.messagebox.showinfo("삭제 완료", "단어를 삭제했습니다.")
            self.See_All_Screen(1, ["Seq", True])


if __name__ == "__main__":
    multiprocessing.freeze_support()
    execute = Gui()
