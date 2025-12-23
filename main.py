import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # メインウィンドウを表示しない

messagebox.showinfo("挨拶", "こんにちは。金子")

root.destroy()