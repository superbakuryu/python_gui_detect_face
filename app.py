import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
import api
from tkinter.ttk import *
import time


def open_folder():
    """Open a file for editing."""
    folder_path = askdirectory()
    if not folder_path:
        return
    list_file_path = api.get_list_file_path_from_folder(folder_path)

    txt_edit.delete(1.0, tk.END)
    text = "\n".join(list_file_path)
    txt_edit.insert(tk.END, text)
    window.title(f"Bài tập ứng dụng - Mai Trọng Thuần - {folder_path}")


def recognize():
    """Save the current file as a new file."""
    text = txt_edit.get(1.0, tk.END)
    list_file_path = text.split('\n')
    num_of_file_path = len(list_file_path) - 1

    for i in range(0, num_of_file_path):
        file_path = list_file_path[i]
        api.crop_image(file_path)
        percentage = int((i+1)/num_of_file_path * 100)
        progress['value'] = percentage
        txt['text'] = progress['value'], '%'
        window.update_idletasks()


window = tk.Tk()
window.title("Bài tập ứng dụng - Mai Trọng Thuần")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Mở thư mục", command=open_folder)
btn_save = tk.Button(fr_buttons, text="Phân tích ảnh", command=recognize)
txt = tk.Label(
    window,
    text='0%'
)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

progress = Progressbar(window, orient=tk.HORIZONTAL,
                       length=100, mode='determinate')

progress.grid(row=1, column=1, sticky="nsew")
txt.grid(row=2, column=1, sticky="nsew")
window.attributes('-topmost', True)
window.mainloop()
