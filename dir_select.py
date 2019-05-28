# モジュールのインポート
import os
import tkinter
import tkinter.filedialog, tkinter.messagebox


class DirSelect:
    def select_mode(self):
        fileDir = os.path.abspath(__file__)
        # アナウンス表示
        # tkinter.messagebox.showinfo('ファイル選択','処理するファイルを選択してください')
        self.file_path = tkinter.filedialog.askopenfilename(initialdir = fileDir)

        self.pic_name = self.file_path.rsplit('/', 1)
        self.pic_name = self.pic_name[1].split('.')
        self.pic_name = self.pic_name[0]

        
        return self.file_path, self.pic_name

        
        

if __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw() #rootを隠す

    dirselect = DirSelect()
    file_path = dirselect.select_mode()
    print(file_path)