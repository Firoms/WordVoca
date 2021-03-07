from tkinter import *
import tkinter
import os
from PIL import ImageTk


class Get_label:
    def image_label(screen, file_name, x, y):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_label = Label(screen)
        image_label.configure(image=image)
        image_label.image = image
        image_label.place(x=x, y=y)
        return image_label

    def image_label_text(screen, file_name, x, y, text, color, font):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_label = Label(
            screen, text=text, compound=tkinter.CENTER, fg=color, font=font
        )
        image_label.configure(image=image)
        image_label.image = image
        image_label.configure(text=text)
        image_label.place(x=x, y=y)
        return image_label

    def image_button(screen, file_name, x, y, command):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_button = Button(screen, overrelief=SOLID, command=command)
        image_button.configure(image=image)
        image_button.image = image
        image_button.place(x=x, y=y)
        return image_button

    def image_button_text(screen, file_name, x, y, command, text, color, font):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_button = Button(
            screen,
            overrelief=SOLID,
            command=command,
            text=text,
            compound=tkinter.CENTER,
            fg=color,
            font=font,
            justify=LEFT,
        )
        image_button.configure(image=image)
        image_button.image = image
        image_button.configure(text=text)
        image_button.place(x=x, y=y)
        return image_button
