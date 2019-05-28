import tkinter
import dir_select
import contour

#イベント設定
def dir_mode():
    global img, file_path, pic_name
    file_path, pic_name = dirselect.select_mode()

# セグメントモード
def contour_mode():
    cont = contour.Contour_creator(file_path, pic_name)
    cont.create_widgets()
    del cont



# ウインドウを作る
root = tkinter.Tk()
root.title("data segmentar")
root.minsize(1200, 600)
root.option_add("*font", ["MS Pゴシック", 22])

# キャンバス設定
canvas = tkinter.Canvas(bg = "black", width = 640, height = 480)
canvas.place(x=0, y=0)
img = tkinter.PhotoImage(file = "") #初期画像設定　この行だけだと画像は非表示

#ファイル選択ボタン表示
dirSelect_button = tkinter.Button(text = "ファイル選択")
dirSelect_button.place(x=410, y=133)
dirSelect_button["command"] = dir_mode

#セグメント開始ボタン
segStart_button = tkinter.Button(text = "輪郭を囲う")
segStart_button.place(x=410, y=233)
segStart_button["command"] = contour_mode



#オブジェクト設定
dirselect = dir_select.DirSelect()
cont = None
file_path = "chap4-1-1.png"
pic_name = None

# ウインドウを表示する
root.mainloop()