from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import os
import sqlite3
from Make_label import Get_label
import pyglet


python_path = os.path.join(os.getcwd())

class Gui:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Word Voca")
        self.gui.geometry("804x804")
        self.gui.resizable(width=False, height=False)
        execute_location = self.center_window(804, 804)
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
        Menu_Screen_background = Get_label.image_label(
            self.gui, os.path.join(python_path, "../../images/menu_bg.png"), 0, 0
        )
        Add_E_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/add_E_btn.png"),
            20,
            450,
            self.Add_Eng_Screen,
        )
        Li_E_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/li_E_btn.png"),
            275,
            450,
            self.Li_Eng_Screen,
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
            self.Add_Kor_Screen,
        )
        Li_K_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/li_K_btn.png"),
            275,
            600,
            self.Li_Kor_Screen,
        )
        Exit_button = Get_label.image_button(
            self.gui,
            os.path.join(python_path, "../../images/exit_btn.png"),
            530,
            600,
            self.quit,
        )
        
    def Add_Eng_Screen(self):
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
    
    def Li_Eng_Screen(self):
        self.destroy()
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
    
    def Add_Kor_Screen(self):
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
    
    def Li_Kor_Screen(self):
        self.destroy()
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
        

if __name__ == "__main__":
    execute = Gui()
