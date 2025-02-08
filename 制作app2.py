from tkinter import mainloop, ttk as ttk
import tkinter.filedialog as FD
import tkinter as tk
from pathlib import Path
import os
from PIL import Image
import shutil

##############################
######## コード部分 ##########
##############################

###削除ボタン
def clear_entry1():
    ftxt.delete("0","end")
def clear_entry2():
    utxt.delete("0","end")

###参照ボタン
def sansyou1():
    fast_folder = ("D:\\")
    file_path = tk.filedialog.askdirectory(initialdir = fast_folder)
    ftxt.insert(tk.END, file_path)
def sansyou2():
    fast_folder = ("D:\\")
    file_path = tk.filedialog.askdirectory(initialdir = fast_folder)
    utxt.insert(tk.END, file_path)

###フォーマット実行関数
def jikkou():
    directory = Path(ftxt.get())
    if ck_jpg.get():
        path = Path(ftxt.get() + "/jpeg")
        os.makedirs(path,exist_ok=True)
        os.chmod(path,0o644)
        for J in os.listdir(directory):
            if J.endswith((".png", ".gif", ".bmp")):
                basename = os.path.basename(J)
                name = path.joinpath(basename[:-4] + ".jpg")
                J_path = os.path.join(directory, J)
                J_img = Image.open(J_path).convert("P").convert("RGB")
                J_img.save(name, format = "JPEG", quality=95)
            elif J.endswith((".jpeg","jpg")):
                img = os.path.join(directory, J)
                shutil.copy(img, path)
    if ck_png.get():
        path = Path(ftxt.get() + "/png")
        os.makedirs(path,exist_ok=True)
        os.chmod(path,0o644)
        for P in os.listdir(directory):
            if P.endswith((".jpg", ".gif", ".bmp")):
               basename = os.path.basename(P)
               name = path.joinpath(basename[:-4] + ".png")
               P_path = os.path.join(directory, P)
               P_img = Image.open(P_path).convert("RGBA")
               P_img.save(name, format = "PNG", quality=95)
            elif P.endswith(".png"):
                img = os.path.join(directory, P)
                shutil.copy(img, path)
    if ck_gif.get():
        path = Path(ftxt.get() + "/gif")
        os.makedirs(path,exist_ok=True)
        os.chmod(path,0o644)
        for G in os.listdir(directory):
            if G.endswith((".jpg", ".png", ".bmp")):
               basename = os.path.basename(G)
               name = path.joinpath(basename[:-4] + ".gif")
               G_path = os.path.join(directory, G)
               G_img = Image.open(G_path).convert("P").convert("RGB")
               G_img.save(name, format = "GIF", quality=95)
            elif G.endswith(".gif"):
                img = os.path.join(directory, G)
                shutil.copy(img, path)

##############################
#########  GUI部分  ##########
##############################

###Tk_window 
root = tk.Tk()
root.geometry("350x300")
###フォーマット前指定
flbl = ttk.Label(text = "画像指定 : ")
flbl.place(relx=0.05, rely=0.05)
ftxt = ttk.Entry()
ftxt.place(relx=0.03, rely=0.05, width=300, x=10, y=20)

fbtn1 = ttk.Button(text = "参照", command = sansyou1)
fbtn1.place(relx=0.03, rely=0.05, x=150, y=45)

clear1 = ttk.Button(text = "clear", command=clear_entry1)
clear1.place(relx=0.03, rely=0.05, x=234, y=45)

###フォーマット後指定
ulbl = ttk.Label(text = "保存先指定 : ")
ulbl.place(relx=0.05, rely=0.05, y=90)
utxt = ttk.Entry()
utxt.place(relx=0.03, rely=0.05, width=300, x=10, y=115)

fbtn2 = ttk.Button(text = "参照", command = sansyou2)
fbtn2.place(relx=0.03, rely=0.05, x=150, y=140)

clear2 = ttk.Button(text = "clear", command=clear_entry2)
clear2.place(relx=0.03, rely=0.05, x=234, y=140)

###check_box
ck_jpg = tk.BooleanVar()
check_jpg = ttk.Checkbutton(text = "jpg", variable=ck_jpg)
check_jpg.place(relx=0.02, rely=0.05, x=25,y=200)

ck_png = tk.BooleanVar()
check_png = ttk.Checkbutton(root, text = "png", variable=ck_png)
check_png.place(relx=0.02, rely=0.05, x=100,y=200)

ck_gif = tk.BooleanVar()
check_gif = ttk.Checkbutton(root, text = "gif", variable=ck_gif)
check_gif.place(relx=0.02, rely=0.05, x=185,y=200)

###実行
strat_btn = ttk.Button(text = "Start!", command=jikkou)
strat_btn.place(relx=0.03, rely=0.05, x=234, y=250)
root.mainloop()###値URLの引き渡し
txb = ttk.Entry()
txb.place(relx=0.02, rely=0.05, height=75, width=355)

###値URLを取得・Start
btn0 = ttk.Button(root,text = "Ｓｔａｒｔ！", command = url_get)
btn0.place(relx=0.02, rely=0.05, x=600,y=250)

###フォルダ参照ラベル
label_text1 = tk.Label(text = "フォルダ指定 :")
label_text1.place(relx=0.01, rely=0.05, x=0, y=120)

###フォルダ参照入力欄
input_text =tk.Entry(width=48)
input_text.place(relx=0.02, rely=0.05, x=64, y=120)

###フォルダ参照btn
btn2 = tk.Button(text = "参照", command = btn2_FD)
btn2.place(relx=0.02, rely=0.05, x=280,y=145)

###削除ボタン
btn1 = tk.Button(text = "Clear", command = clear_entry1)
btn1.place(relx=0.02, rely=0.05, x=318,y=80)
btn3 = tk.Button(text = "Clear", command = clear_entry2)
btn3.place(relx=0.02, rely=0.05, x=318,y=145)

###check_box判定部分
ck_jpg = tk.BooleanVar()
check_jpg = ttk.Checkbutton(text = "jpg", variable=ck_jpg)
check_jpg.place(relx=0.02, rely=0.05, x=400,y=15)

ck_png = tk.BooleanVar()
check_png = ttk.Checkbutton(root, text = "png", variable=ck_png)
check_png.place(relx=0.02, rely=0.05, x=480,y=15)

ck_gif = tk.BooleanVar()
check_gif = ttk.Checkbutton(root, text = "gif", variable=ck_gif)
check_gif.place(relx=0.02, rely=0.05, x=560,y=15)

ck_odd = tk.BooleanVar()
check_odd = ttk.Checkbutton(root, text = "original_D", variable=ck_odd)
check_odd.place(relx=0.02, rely=0.05, x=560,y=50)

"""
###プログレスバー
pbval = tk.IntVar(value=count)
pb = ttk.Progressbar(root, length=350, maximum=100, mode="determinate", variable=pbval)
pb.place(relx=0.02, rely=0.05,x=5,y=235)
"""
"""
        if not file_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
            txt = file_name.find("?")
            file_name = (file_name[:txt])
        print(file_name)
"""
root.mainloop()