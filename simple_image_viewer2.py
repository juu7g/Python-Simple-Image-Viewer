from PIL import ImageTk
import tkinter as tk
from tkinterdnd2 import *

def set_image(event):
    global img      # グローバル変数の宣言(グローバルにしないとオブジェクトがgcされる)
    paths = root.tk.splitlist(event.data)   # ドロップされた複数パス名をパス名ごとに分割
    img = ImageTk.PhotoImage(file=paths[0])    # 画像オブジェクトの作成。1番目だけを対象にする
    label1.configure(image=img)             # ラベルの画像の更新

root = TkinterDnD.Tk()      # トップレベルウィンドウの作成  tkinterdnd2の適用
img = None                  # グローバル変数の定義
root.title("画像 viewer")   # タイトル
label1 = tk.Label(root, text="ここに画像ファイルを\nドロップしてください")  # ラベルの作成
label1.pack()
root.drop_target_register(DND_FILES)    # ドロップ受け取りを登録
root.dnd_bind("<<Drop>>", set_image)    # ドロップ後に実行するメソッドを登録
root.mainloop()