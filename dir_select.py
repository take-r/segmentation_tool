# モジュールのインポート
import os
import tkinter
import tkinter.filedialog
from PIL import Image


class DirSelect:
    def __init__(self):
        self.fileDir = os.path.abspath(__file__)

    def select_mode(self):
        self.file_path = tkinter.filedialog.askopenfilename(initialdir = self.fileDir)
        self.fileDir = self.file_path.rsplit("/", 1)
        self.fileDir = self.fileDir[0]

        # 元画像のファイル名を抽出
        self.pic_name = self.file_path.rsplit('/', 1)
        self.pic_name = self.pic_name[1].split('.')
        self.pic_name = self.pic_name[0]

        # 画像のサイズ
        self.wid, self.heig = Image.open(self.file_path).size

        return [self.file_path, self.pic_name, self.wid, self.heig]

        
        

if __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw() #rootを隠す

    dirselect = DirSelect()
    file_path = dirselect.select_mode()
    print(file_path)