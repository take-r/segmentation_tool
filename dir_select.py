# モジュールのインポート
import os
import tkinter
import tkinter.filedialog, tkinter.messagebox


class DirSelect:
    def select_mode(self):
        fileDir = os.path.abspath(__file__)
        # アナウンス表示
        # tkinter.messagebox.showinfo('ファイル選択','処理するファイルを選択してください')
        file = tkinter.filedialog.askopenfilename(initialdir = fileDir)
        
        return file

        
        

if __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw() #rootを隠す

    dirselect = DirSelect()
    file_path = dirselect.select_mode()
    print(file_path)