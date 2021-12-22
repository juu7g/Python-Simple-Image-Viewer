"""
シンプル画像ビューワー
"""
import pathlib
from PIL import ImageTk, Image
import tkinter as tk
import sys
from tkinterdnd2 import *

def set_image(event=None, path=""):
    """
    画像をラベルウィジェットに設定
    画像は後で拡大縮小できるようにpillowのImageオブジェクトで持つ
    PhotoImageオブジェクトは関数を抜けてもgcされないようグローバル変数で持つ
    openでエラーになったらラベルウィジェットのイメージは非表示にする
    ウィンドウのタイトルにパス名を表示
    ラベルウィジェットに幅、高さ、変更日時を表示
    """
    global img          # グローバル変数の宣言(グローバルにしないとオブジェクトがgcされる)
    global photo_img    # グローバル変数の宣言(グローバルにしないとオブジェクトがgcされる)

    if event:
        paths = root.tk.splitlist(event.data)   # ドロップされた複数パス名をパス名ごとに分割
        path = paths[0]                         # 1番目だけを対象にする

    try:
        img = Image.open(path)                  # 画像オブジェクトの作成
    except Exception as e:                      # 例外の時imgは
        label1.configure(image="", text="エラー：" + path)
    else:
        photo_img = ImageTk.PhotoImage(img)     # PhotoImageオブジェクト作成
        if img.getexif():
            exif = "Exifあり"
        else:
            exif = "Exifなし"
        info = f"{img.width} x {img.height} | {exif}"
        label1.configure(image=photo_img, text=info)  # 画像をラベルに設定
    root.title(path)                            # パス名をタイトルに(後で参照する)

def resize_image(event=None):
    """
    画像のリサイズ
    マウスホイールのイベントで呼ばれる
    リサイズしたものをリサイズすると画質が悪くなるので常に元の画像をリサイズ
    サイズはホイールの増分の何分の一とする
    幅を決めたらアスペクト比を維持して高さを決める
    リサイズ後のサイズをテキストで表示
    """
    global img          # グローバル変数の宣言(グローバルにしないとオブジェクトがgcされる)
    global photo_img    # グローバル変数の宣言(グローバルにしないとオブジェクトがgcされる)
    # event.deltaはwindowsの場合、+-120単位で返る
    new_width = photo_img.width() + int(event.delta / 12)
    new_height = round(img.height * new_width / img.width)
    img2 = img.resize((new_width, new_height))      # 読み込んだ画像をリサイズしないと画質が悪くなる
    photo_img = ImageTk.PhotoImage(img2)
    if img.getexif():
        exif = "Exifあり"
    else:
        exif = "Exifなし"
    info = f"{new_width} x {new_height}({img.width} x {img.height}) | {exif}"
    label1.configure(image=photo_img, text=info)  # 画像をラベルに設定

def preview_other_image(event=None):
    """
    表示している画像と同じフォルダの画像を表示
    表示している画像のパスはタイトルから取得
    同フォルダのファイルをPathオブジェクトでリスト化(毎回は無駄(対応保留))
    表示しているファイルのリスト内の位置を求める
    マウスホイールの方向で次の表示ファイルを決める
    """
    file = pathlib.Path(root.title())           # タイトルから現対象のパスを取得
    paths = [p for p in file.parent.iterdir() if p.is_file()]   # 同フォルダのファイルを取得
    i = paths.index(file)                       # フォルダ内の位置を取得
    if event:
        i = i + int(event.delta / abs(event.delta))     # ホイールの移動を1単位にして次のファイルを決める
        if i >= len(paths):                     # はみ出したら戻す
            i = 0                               # -1はリストの再末尾なので許容
    # print(f"{i}:{paths[i]}")                  # debug用
    set_image(path = str(paths[i]))             # 画像表示

root = TkinterDnD.Tk()      # トップレベルウィンドウの作成  tkinterdnd2の適用
img = None                  # グローバル変数の定義
photo_img = None            # グローバル変数の定義
root.title("画像 viewer")   # 初期タイトル
label1 = tk.Label(root, text="ここに画像ファイルを\nドロップしてください", compound="bottom")
label1.pack()
# bind
root.bind("<MouseWheel>", resize_image)
root.bind("<Control-MouseWheel>", preview_other_image)
# DnD
root.drop_target_register(DND_FILES)    # ドロップ受け取りを登録
root.dnd_bind("<<Drop>>", set_image)    # ドロップ後に実行するメソッドを登録
# コマンドライン引数からドラッグ＆ドロップされたファイル情報を取得
if len(sys.argv) > 1:
    set_image(path = sys.argv[1])       # コマンドラインの1つ目だけを引数で渡す
root.mainloop()