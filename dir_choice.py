import tkinter

class DirChoice:
    def choice_mode(self):
        self.dialog.place(x=10, y=10)
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 620, 434, fill="blue")
        self.canvas.create_image(310, 200, image=self.img)

    #イベント設定
    def dirMove_click(self, add_dir):
        global cur_dir
        self.cur_dir = self.cur_dir + "/" + add_dir
        self.directory["text"] = self.cur_dir

    def dirReset_click(self):
        global cur_dir
        self.cur_dir = "/Users/take/Documents"
        self.directory["text"] = self.cur_dir
    
    def dirBack_click(self):
        global cur_dir
        dir_sprit = self.cur_dir.rsplit('/', 1)
        self.cur_dir = dir_sprit[0]
        self.directory["text"] = self.cur_dir

    def upload_click(self):
        global cur_dir, img
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 620, 434, fill="black")
        self.img = tkinter.PhotoImage(file = self.cur_dir)
        self.canvas.create_image(320, 240, image = self.img)

    def __init__(self):
            
        #関数設定
        self.cur_dir = "/Users/take/Documents"

        # ウインドウを作る
        self.dialog = tkinter.Frame(width=600, height=440)
        self.dialog.place(x=10, y=10)

        # # キャンバス設定
        self.canvas = tkinter.Canvas(self.dialog, width = 580, height = 400)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, 540, 380, fill='blue')
        self.img = tkinter.PhotoImage(file = "chap4-1-1.png")
        self.canvas.create_image(310, 200, image=self.img)

        # #テキスト表示
        self.question = tkinter.Label(self.dialog, text = "ディレクトリ先を入力してください", bg="white")
        self.question.place(x=100, y=40)

        # #テキストボックス表示
        self.entry = tkinter.Entry(self.dialog, width=12, bd=4)
        self.entry.place(x=100, y=133)

        # #移動ボタン表示
        self.dirMove_button = tkinter.Button(self.dialog, text = "移動")
        self.dirMove_button.place(x=310, y=133)
        self.dirMove_button["command"] = lambda : self.dirMove_click(self.entry.get())
        #リセットボタン表示
        self.dirReset_button = tkinter.Button(self.dialog, text = "リセット")
        self.dirReset_button.place(x=410, y=133)
        self.dirReset_button["command"] = self.dirReset_click
        #バックボタン表示
        self.dirBack_button = tkinter.Button(self.dialog, text = "バック")
        self.dirBack_button.place(x=310, y=183)
        self.dirBack_button["command"] = self.dirBack_click
        #画像表示ボタン
        self.upload_button = tkinter.Button(self.dialog, text = "表示")
        self.upload_button.place(x=410, y=183)
        self.upload_button["command"] = self.upload_click


        #現在のディレクトリ表示
        self.directory = tkinter.Label(self.dialog, text = "...", bg="white")
        self.directory.place(x=100, y=235)

        #非表示
        self.dialog.place_forget()

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("data segmentar")
    root.minsize(880, 480)
    root.option_add("*font", ["MS Pゴシック", 22])

    dirchoice = DirChoice()
    dirchoice.choice_mode()

    root.mainloop()