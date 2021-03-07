import serial
from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from playsound import playsound
import os
import threading
import time
import sqlite3
import tkinter.messagebox
from Make_label import Get_label
from db import *
import pyglet
from tkinter.simpledialog import askstring


img_path = os.path.join(os.getcwd())


class Gui:
    def __init__(self):
        self.screen_num = 0
        self.screen = Tk()
        self.screen.iconbitmap("../../images/logo.ico")
        self.screen.title("방문록 자동 입력 프로그램")
        self.screen.geometry("804x804")
        self.screen.resizable(width=False, height=False)
        execute_location = self.center_window(804, 804)
        pyglet.font.add_file("../../fonts/GodoM.otf")
        pyglet.font.add_file("../../fonts/HoonDdukbokki.ttf")
        self.main_screen()
        self.com_port = askstring("아두이노 연결", "COM 포트 번호를 입력해주세요.(숫자로만)")
        if self.com_port == None:
            self.com_port = "COM3"
        else:
            self.com_port = f"COM{self.com_port}"
        arduino_thread = threading.Thread(target=self.arduino)
        arduino_thread.daemon = True
        arduino_thread.start()
        self.screen.mainloop()

    def destroy(self):
        list1 = self.screen.place_slaves()
        for l in list1:
            l.destroy()

    def center_window(self, width, height):
        screen_width = self.screen.winfo_screenwidth()
        screen_height = self.screen.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2) - 25
        self.screen.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def arduino(self):
        ser = serial.Serial(
            port=self.com_port,
            baudrate=9600,
        )
        self.last_res = ""
        while True:
            if ser.readable():
                res = ser.readline()
                self.res = (res.decode()[: len(res) - 2]).strip()
                self.last_res = str(self.res)
                if 0 < self.screen_num < 3:
                    warn_message = tkinter.messagebox.showinfo(
                        "가입 불가", "이름과 소속을 모두 입력해주세요."
                    )
                elif self.screen_num == 3:
                    check = check_pin_num(self.last_res)
                    if check == "None":
                        new = input_Name(self.last_res, self.name, self.content)
                        warn_message = tkinter.messagebox.showinfo(
                            "가입 완료", "회원가입이 완료 되었습니다."
                        )
                        self.user_data = get_last_user()
                        self.list_data = get_last_list()
                        self.apply_screen()
                    else:
                        warn_message = tkinter.messagebox.showinfo(
                            "가입 불가", "회원가입이 이미 되어있는 카드입니다."
                        )
                        self.apply_screen()
                else:
                    check = check_pin_num(self.last_res)
                    if check == "None":
                        warn_message = tkinter.messagebox.showinfo(
                            "사용 불가", "회원가입 후 이용해 주세요."
                        )
                    else:
                        save(self.last_res)
                        self.user_data = get_last_user()
                        self.list_data = get_last_list()
                        if self.screen_num == 5:
                            self.reload()
                        elif self.screen_num == 0:
                            self.main_screen()

    def no_action(self):
        pass

    def main_screen(self):
        self.destroy()
        self.screen_num = 0
        self.sort_num = 0
        self.sort_color = 0
        Main_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/main_bg.png"), 0, 0
        )
        User_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/btn1.png"),
            20,
            290,
            self.apply_screen,
        )
        List_button = Get_label.image_button(
            self, os.path.join(img_path, "../../images/btn2.png"), 280, 290, self.reload
        )
        Exit_button = Get_label.image_button(
            self, os.path.join(img_path, "../../images/btn3.png"), 540, 290, self._quit
        )
        self.user_data = get_last_user()
        self.list_data = get_last_list()
        Data_1 = Get_label.image_label_text(
            self,
            os.path.join(img_path, "../../images/Data.png"),
            32,
            390,
            f"{self.user_data[1]} 소속 \n\n {self.user_data[0]}님 \n\n 회원가입 되셨습니다. ",
            "#472f91",
            ("고도 M", 24),
        )
        Data_2 = Get_label.image_label_text(
            self,
            os.path.join(img_path, "../../images/Data.png"),
            422,
            390,
            f"{self.list_data[2]} 님 \n\n {self.list_data[0]} \n\n {self.list_data[1]} \n\n 방문하셨습니다.",
            "#472f91",
            ("고도 M", 24),
        )

    def apply_screen(self):
        self.screen_num = 1
        self.destroy()
        Apply_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/apply_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/return.png"),
            580,
            30,
            self.main_screen,
        )

        self.name_entry = tkinter.Text(self.screen, width=10, height=1)
        self.name_entry.place(x=200, y=450)
        self.name_entry.config(font=("고도 M", 45))
        self.name_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/commit.png"),
            560,
            450,
            self.commit1,
        )
        self.content_entry = tkinter.Text(self.screen, width=10, height=1)
        self.content_entry.place(x=200, y=570)
        self.content_entry.config(font=("고도 M", 45))
        self.content_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/commit.png"),
            560,
            570,
            self.commit2,
        )
        recommit_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/recommit.png"),
            250,
            700,
            self.apply_screen,
        )

    def commit1(self):
        self.name_entry.config(state="disabled")
        self.name_button.config(state="disabled")
        self.screen_num += 1
        self.name = self.name_entry.get("1.0", "end")
        self.name = self.name.strip()

    def commit2(self):
        self.content_entry.config(state="disabled")
        self.content_button.config(state="disabled")
        self.screen_num += 1
        self.content = self.content_entry.get("1.0", "end")
        self.content = self.content.strip()

    def reload(self):
        self.list = get_list("Date", self.sort_num)
        self.list_screen1()

    def list_screen1(self):
        self.destroy()
        self.screen_num = 5
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/return.png"),
            580,
            30,
            self.main_screen,
        )
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/left.png"),
            300,
            40,
            self.no_action,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/right.png"),
            400,
            40,
            self.list_screen2,
        )
        left_button.config(state="disabled")
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li1.png"),
            12,
            133,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            62,
            133,
            self.sort1,
            f"날짜",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li3.png"),
            272,
            133,
            self.sort2,
            f"시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li4.png"),
            482,
            133,
            self.sort3,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li5.png"),
            612,
            133,
            self.sort4,
            f"소속",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 15:
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li1-1.png"),
                12,
                173 + (40 * i),
                f"{i+1}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                62,
                173 + (40 * i),
                f"{self.list[i][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li3-1.png"),
                272,
                173 + (40 * i),
                f"{self.list[i][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li4-1.png"),
                482,
                173 + (40 * i),
                f"{self.list[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            li5 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li5-1.png"),
                612,
                173 + (40 * i),
                f"{self.list[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )

    def list_screen2(self):
        self.destroy()
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/return.png"),
            580,
            30,
            self.main_screen,
        )
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/left.png"),
            300,
            40,
            self.list_screen1,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/right.png"),
            400,
            40,
            self.list_screen3,
        )
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li1.png"),
            12,
            133,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            62,
            133,
            self.sort1,
            f"날짜",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li3.png"),
            272,
            133,
            self.sort2,
            f"시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li4.png"),
            482,
            133,
            self.sort3,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li5.png"),
            612,
            133,
            self.sort4,
            f"소속",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 30:
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length - 15
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li1-1.png"),
                12,
                173 + (40 * i),
                f"{i+16}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                62,
                173 + (40 * i),
                f"{self.list[i+15][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li3-1.png"),
                272,
                173 + (40 * i),
                f"{self.list[i+15][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li4-1.png"),
                482,
                173 + (40 * i),
                f"{self.list[i+15][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            li5 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li5-1.png"),
                612,
                173 + (40 * i),
                f"{self.list[i+15][3]}",
                "#472f91",
                ("고도 M", 12),
            )

    def list_screen3(self):
        self.destroy()
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/return.png"),
            580,
            30,
            self.main_screen,
        )
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/left.png"),
            300,
            40,
            self.list_screen2,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/right.png"),
            400,
            40,
            self.no_action,
        )
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li1.png"),
            12,
            133,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            62,
            133,
            self.sort1,
            f"날짜",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li3.png"),
            272,
            133,
            self.sort2,
            f"시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li4.png"),
            482,
            133,
            self.sort3,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li5.png"),
            612,
            133,
            self.sort4,
            f"소속",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 45:
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length - 30
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li1-1.png"),
                12,
                173 + (40 * i),
                f"{i+31}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                62,
                173 + (40 * i),
                f"{self.list[i+30][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li3-1.png"),
                272,
                173 + (40 * i),
                f"{self.list[i+30][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li4-1.png"),
                482,
                173 + (40 * i),
                f"{self.list[i+30][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            li5 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li5-1.png"),
                612,
                173 + (40 * i),
                f"{self.list[i+30][3]}",
                "#472f91",
                ("고도 M", 12),
            )

    def sort1(self):
        self.sort = "Date"
        self.list = get_list("Date", self.sort_num)
        self.sort_color = 1
        fir = self.list_screen1()

    def sort2(self):
        self.sort = "Time"
        self.list = get_list("Time", self.sort_num)
        self.sort_color = 2
        fir = self.list_screen1()

    def sort3(self):
        self.sort = "Name"
        self.list = get_list("Name", self.sort_num)
        self.sort_color = 3
        fir = self.list_screen1()

    def sort4(self):
        self.sort = "Content"
        self.list = get_list("Content", self.sort_num)
        self.sort_color = 4
        fir = self.list_screen1()

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.screen.quit()
            self.screen.destroy()
            exit()

    def change_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")


if __name__ == "__main__":
    a = Gui()
