import tkinter
from PIL import Image

class Contour_creator(tkinter.Frame):
    
    # コンストラクタ
    def __init__(self, master = None):
        self.frame = tkinter.Frame.__init__(self, master)
        self.pack()

    # 各ウィジェットの配置
    def create_widgets(self, file_path):
        self.wid, self.heig = Image.open(file_path).size
        self.file_path = file_path

        self.entry = tkinter.Entry(self)
        self.entry.grid(self.frame, row=0, column=0)

        self.save_button = tkinter.Button(self, text='保存', command=self.save_text)
        self.save_button.grid(row=0, column=1)
        self.tie_button = tkinter.Button(self, text='始点と結ぶ', command=self.tie_points)
        self.tie_button.grid(row=0, column=2)
        self.deletePoint_button = tkinter.Button(self, text='一つ戻る', command=self.delete_point)
        self.deletePoint_button.grid(row=1, column=2)
        self.reset_button = tkinter.Button(self, text='リセット', command=self.reset_points)
        self.reset_button.grid(row=2, column=2)
        self.finish_button = tkinter.Button(self, text='セグメントモードを終了する', command=self.finish)
        self.finish_button.grid(row=3, column=2)
        

        self.text = tkinter.Text(self, height=20, width=20)
        self.text.grid(row=1, column=1)

        self.canvas = tkinter.Canvas(self, height=self.heig, width=self.wid)
        self.canvas.grid(row=1, column=0, rowspan=5) ##rowspan??
        self.img = tkinter.PhotoImage(file = file_path)
        self.canvas.create_image(self.wid/2, self.heig/2, image = self.img)
        self.canvas.bind('<Motion>', self.mouse_pos)
        self.canvas.bind('<Button-1>', self.lclick)

        # 初期化
        self.pre_x, self.pre_y = None, None
        self.start_x, self.start_y = None, None
        self.points = []


    # マウス座標の表示
    def mouse_pos(self, event):
        line = 'x:' + str(event.x) + ' ' + 'y:' + str(event.y)
        self.entry.delete(0, 20) #0から20文字まで消す
        self.entry.insert(0, line)

    # クリック座標の記録＆線つなぐ
    def lclick(self, event):
        if((event.x >= 0) and (event.x <= self.wid) and
            (event.y >= 0) and (event.y <= self.heig)):
            self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2,
                 fill='RED', tag="oval")
            self.text.insert(tkinter.END, str(event.x) + ', ' + str(event.y) + '\n')
            self.points.append([event.x, event.y])
            
            # 前の点が存在するか
            if self.pre_x:
                self.canvas.create_line(self.pre_x, self.pre_y, event.x, event.y, tag="line")
            else:
                self.start_x, self.start_y = event.x, event.y

            self.pre_x, self.pre_y = event.x, event.y

    # 座標データを保存する
    def save_text(self):
        # 元画像の名前を抽出
        pic_name = self.file_path.rsplit('/', 1)
        pic_name = pic_name[1].split('.')
        f = open('{}.txt'.format(pic_name[0]), 'w')

        all_text = self.text.get('1.0', tkinter.END)
        f.write(all_text)
        f.close()
    
    # 始点と終点を結ぶ
    def tie_points(self):
        self.canvas.create_line(self.start_x, self.start_y, self.pre_x, self.pre_y)

    # 点を一つ戻す
    def delete_point(self):
        self.canvas.delete("oval")
        self.canvas.delete("line")
        self.text.delete('1.0', tkinter.END)

        self.points.pop(-1)
        for i in range(len(self.points)):
            self.text.insert(tkinter.END, 
                str(self.points[i][0]) + ', ' + str(self.points[i][1]) + '\n')
            self.canvas.create_oval(self.points[i][0]-2, self.points[i][1]-2,
                self.points[i][0]+2, self.points[i][1]+2, fill='RED', tag="oval")
            if i==0:
                continue
            else:
                self.canvas.create_line(self.points[i-1][0], self.points[i-1][1],
                    self.points[i][0], self.points[i][1], tag="line")

    # 点をリセットする
    def reset_points(self):
        self.canvas.delete('oval')
        self.canvas.delete('line')
        self.text.delete('1.0', tkinter.END)
        self.points.clear()
        self.pre_x, self.pre_y = None, None
    
    # セグメントモードを終了する
    def finish(self):
        self.reset_points()
        self.pack_forget()




if __name__ == '__main__':
    contour = Contour_creator()
    contour.create_widgets("chap4-1-1.png")
    contour.mainloop()