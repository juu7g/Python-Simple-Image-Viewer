from PIL import ImageTk
import tkinter as tk
import sys
root = tk.Tk()              # トップレベルウィンドウの作成
root.title("画像 viewer")   # タイトル
img = ImageTk.PhotoImage(file=sys.argv[1])  # 画像の読み込み コマンドライン引数の1番目のファイル名
tk.Label(root, image=img).pack()   # ラベルウィジェットの作成、画像指定
root.mainloop()