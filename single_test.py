import tkinter
import dir_select

#イベント設定
def dir_mode():
    file_path = dirselect.select_mode()
    canvas.create_image(310, 200, image=img)


# ウインドウを作る
root = tkinter.Tk()
root.title("data segmentar")
root.minsize(880, 480)
root.option_add("*font", ["MS Pゴシック", 22])

# キャンバス設定
canvas = tkinter.Canvas(bg = "black", width = 640, height = 480)
canvas.place(x=0, y=0)
canvas.create_rectangle(0, 0, 600, 300, fill="gray")
img = tkinter.PhotoImage(file = "chap4-1-1.png")
canvas.create_image(310, 200, image=img)

#画像選択ボタン表示
dirReset_button = tkinter.Button(text = "ファイル選択")
dirReset_button.place(x=410, y=133)
dirReset_button["command"] = dir_mode

#オブジェクト設定
dirselect = dir_select.DirSelect()


# ウインドウを表示する
root.mainloop()