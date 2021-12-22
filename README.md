# Python-Simple-Image-Viewer


## �T�v Description
�V���v���摜�r���[�A  
Simple image viewer

�R�}���h���C�������ŉ摜�t�@�C�����w�肷�邩�A�摜�t�@�C�����h���b�O�A���h�h���b�v���ĕ\������V���v���ȉ摜�r���[�A  
A simple image viewer that displays an image file by specifying it with a command line argument or by dragging and dropping the image file.  

## ���� Features

- GIF�APNG�AJPEG�AWebP ���͂��ߑ����̎�ނ̉摜�t�@�C����\��  
	View many types of image files including GIF, PNG, JPEG, WebP  
- ���x���E�B�W�F�b�g�ŉ摜�\��  
	Image display with label widget  
- �}�E�X�z�C�[���ŕ\�������摜���g��A�k���\��  
	Enlarge or shrink the image displayed with the mouse wheel  
- Ctrl + �}�E�X�z�C�[���œ����t�H���_�̕ʉ摜��\��  
	Display another image in the same folder with Ctrl + mouse wheel  
- �h���b�O�A���h�h���b�v�Ńt�@�C�����w��\(TkinterDnD2�g�p)
	File can be specified by drag and drop(using TkinterDnD2)  
- exe�Ƀh���b�O�A���h�h���b�v�Ńt�@�C�����w��\(TkinterDnD2�g�p�ł�)
	File can be specified by dragging and dropping to exe(using TkinterDnD2)  

## �ˑ��֌W Requirement

- Python 3.8.5  
- Pillow 8.3.0  
- TkinterDnD2 0.3.0  

## �g���� Usage

```dosbatch
	simple_image_viewer.exe
```
�܂���simple_image_viewer.exe�̃A�C�R���ɕ\���������t�@�C�����h���b�O���h���b�v���܂�

- ���� Operation  
	- �h���b�O���h���b�v�ł̑���  
		Drag and drop operation  
		- �A�v����ʏ�̔C�ӂ̈ʒu�ɕ\���������t�@�C�����h���b�O���h���b�v  
			Drag and drop the file you want to display anywhere on the application screen  
	- �摜�̊g��A�k��  
		Enlarging or shrinking the image  
		- �\�����ꂽ�摜�̏�Ń}�E�X�z�C�[��  
			Mouse wheel on the displayed image  
			��Ƀz�C�[������Ɗg��  
			Wheel up to enlarge
			���Ƀz�C�[������Ək��  
			Wheel down to shrink  
	- �����t�H���_�̕ʂ̉摜��\��  
		View another image in the same folder  
		- �\�����ꂽ�摜�̏��ctrl + �}�E�X�z�C�[��  
			On the displayed image ctrl + mouse wheel  
			��Ƀz�C�[������Ǝ��̉摜��\��  
			Wheel up to see the next image  
			���Ƀz�C�[������ƑO�̉摜��\��
			Wheel down to see the previous image  

  - ��ʂ̐��� Screen description  
	- �w�肵���t�@�C�����v���r���[���܂�  
		Preview the specified file  
	- �t�@�C�������^�C�g���ɕ\�����܂�  
		Display the file name in the title  
	- �摜�̕��A�����AExif���̗L����\�����܂�  
		Shows the width, height, and presence / absence of Exif information in the image  
	- �v���r���[�ł��Ȃ��ꍇ�̓t�@�C���������\�����܂�  
		If preview is not possible, only the file name will be displayed.  

## �C���X�g�[�����@ Installation

- pip install tkinterdnd2  
- pip install pillow  

## �v���O�����̐����T�C�g Program description site

[�V���v���摜�r���[�A�̍���(�}�E�X�z�C�[���Ή�)�yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/image/simple-viewer)  

## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B  
This software is released under the MIT License, see LICENSE.txt.

