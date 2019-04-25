import tkinter
import dir_choice

#イベント設定
def dir_mode():
    dirchoice.choice_mode()


# ウインドウを作る
root = tkinter.Tk()
root.title("data segmentar")
root.minsize(880, 480)
root.option_add("*font", ["MS Pゴシック", 22])

# キャンバス設定
canvas = tkinter.Canvas(bg = "black", width = 640, height = 480)
canvas.place(x=0, y=0)
canvas.create_rectangle(0, 0, 600, 300, fill="gray")

#画像選択ボタン表示
dirReset_button = tkinter.Button(text = "画像選択")
dirReset_button.place(x=410, y=133)
dirReset_button["command"] = dir_mode

#オブジェクト設定
dirchoice = dir_choice.DirChoice()


# ウインドウを表示する
root.mainloop()