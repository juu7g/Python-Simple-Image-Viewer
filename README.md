# Python-Simple-Image-Viewer


## 概要 Description
シンプル画像ビューア  
Simple image viewer

コマンドライン引数で画像ファイルを指定するか、画像ファイルをドラッグアンドドロップして表示するシンプルな画像ビューア  
A simple image viewer that displays an image file by specifying it with a command line argument or by dragging and dropping the image file.  

## 特徴 Features

- GIF、PNG、JPEG、WebP をはじめ多くの種類の画像ファイルを表示  
	View many types of image files including GIF, PNG, JPEG, WebP  
- ラベルウィジェットで画像表示  
	Image display with label widget  
- マウスホイールで表示した画像を拡大、縮小表示  
	Enlarge or shrink the image displayed with the mouse wheel  
- Ctrl + マウスホイールで同じフォルダの別画像を表示  
	Display another image in the same folder with Ctrl + mouse wheel  
- ドラッグアンドドロップでファイルを指定可能(TkinterDnD2使用)
	File can be specified by drag and drop(using TkinterDnD2)  
- exeにドラッグアンドドロップでファイルを指定可能(TkinterDnD2使用でも)
	File can be specified by dragging and dropping to exe(using TkinterDnD2)  

## 依存関係 Requirement

- Python 3.8.5  
- Pillow 8.3.0  
- TkinterDnD2 0.3.0  

## 使い方 Usage

```dosbatch
	simple_image_viewer.exe
```
またはsimple_image_viewer.exeのアイコンに表示したいファイルをドラッグ＆ドロップします

- 操作 Operation  
	- ドラッグ＆ドロップでの操作  
		Drag and drop operation  
		- アプリ画面上の任意の位置に表示したいファイルをドラッグ＆ドロップ  
			Drag and drop the file you want to display anywhere on the application screen  
	- 画像の拡大、縮小  
		Enlarging or shrinking the image  
		- 表示された画像の上でマウスホイール  
			Mouse wheel on the displayed image  
			上にホイールすると拡大  
			Wheel up to enlarge
			下にホイールすると縮小  
			Wheel down to shrink  
	- 同じフォルダの別の画像を表示  
		View another image in the same folder  
		- 表示された画像の上でctrl + マウスホイール  
			On the displayed image ctrl + mouse wheel  
			上にホイールすると次の画像を表示  
			Wheel up to see the next image  
			下にホイールすると前の画像を表示
			Wheel down to see the previous image  

  - 画面の説明 Screen description  
	- 指定したファイルをプレビューします  
		Preview the specified file  
	- ファイル名をタイトルに表示します  
		Display the file name in the title  
	- 画像の幅、高さ、Exif情報の有無を表示します  
		Shows the width, height, and presence / absence of Exif information in the image  
	- プレビューできない場合はファイル名だけ表示します  
		If preview is not possible, only the file name will be displayed.  

## インストール方法 Installation

- pip install tkinterdnd2  
- pip install pillow  

## プログラムの説明サイト Program description site

[シンプル画像ビューアの作り方(マウスホイール対応)【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/image/simple-viewer)  

## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
This software is released under the MIT License, see LICENSE.txt.

