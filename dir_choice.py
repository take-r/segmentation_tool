import tkinter

#関数設定
cur_dir = "documents"


#イベント設定
def dirMove_click(add_dir):
    global cur_dir
    cur_dir = cur_dir + "/" + add_dir
    answer["text"] = cur_dir

def dirReset_click():
    global cur_dir
    cur_dir = "documents"
    answer["text"] = cur_dir

def upload_click():
    global cur_dir, img
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 620, 434, fill="black")
    img = tkinter.PhotoImage(file = cur_dir)
    canvas.create_image(320, 240, image=img)

# ウインドウを作る
root = tkinter.Tk()
root.title("data segmentar")
root.minsize(880, 480)
root.option_add("*font", ["MS Pゴシック", 22])

# キャンバス設定
canvas = tkinter.Canvas(bg = "black", width = 640, height = 480)
canvas.place(x=0, y=0)
img = tkinter.PhotoImage(file = "documents/segmentation_tool/chap4-1-1.png")

#テキスト表示
question = tkinter.Label(text = "ディレクトリ先を入力してください", bg="white")
question.place(x=100, y=40)

#テキストボックス表示
entry = tkinter.Entry(width=12, bd=4)
entry.place(x=100, y=133)

#移動ボタン表示
dirMove_button = tkinter.Button(text = "移動")
dirMove_button.place(x=310, y=133)
dirMove_button["command"] = lambda : dirMove_click(entry.get())
#リセットボタン表示
dirReset_button = tkinter.Button(text = "リセット")
dirReset_button.place(x=410, y=133)
dirReset_button["command"] = dirReset_click
#画像表示ボタン
upload_button = tkinter.Button(text = "表示")
upload_button.place(x=410, y=183)
upload_button["command"] = upload_click


#現在のディレクトリ表示
answer = tkinter.Label(text = "...", bg="white")
answer.place(x=100, y=235)




# ウインドウを表示する
root.mainloop()