import tkinter
from PIL import Image, ImageTk

import fill_area

class Contour_creator(tkinter.Frame):
    
    # コンストラクタ
    def __init__(self, file_info, master = None):
        self.frame = tkinter.Frame.__init__(self, master)
        self.pack()
        self.file_info = file_info #ファイルパス, ファイル名, width, height
        self.Tdata_wid, self.Tdata_heig = 800, 600
        self.fillArea = fill_area.FillArea(self.Tdata_wid, self.Tdata_heig)
        
        

    # 各ウィジェットの配置
    def create_widgets(self):
        self.pic_wid, self.pic_heig = self.file_info[2], self.file_info[3]

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
        self.finish_button = tkinter.Button(self, text='保存して終了する', command=self.finish)
        self.finish_button.grid(row=3, column=2)
        self.fill_button = tkinter.Button(self, text='塗りつぶす', command=self.fill_polygon)
        self.fill_button.grid(row=4, column=2)

        self.text = tkinter.Text(self, height=20, width=20)
        self.text.grid(row=1, column=1)

        self.canvas = tkinter.Canvas(self, width=self.Tdata_wid, height=self.Tdata_heig) #
        self.canvas.grid(row=1, column=0, rowspan=5) ##rowspan??
        #self.img = tkinter.PhotoImage(self.frame, file = self.file_info[0]) #元
        self.img = Image.open(self.file_info[0]) #
        self.img = self.img.resize((self.Tdata_wid,self.Tdata_heig))
        self.img = ImageTk.PhotoImage(self.img)
        
        self.canvas.create_image(self.Tdata_wid/2,self.Tdata_heig/2, image = self.img) #
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
        if((event.x >= 0) and (event.x <= self.pic_wid) and
            (event.y >= 0) and (event.y <= self.pic_heig)):
            self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2,
                 fill='RED', tag="oval")
            self.text.insert(tkinter.END, str(event.x) + ', ' + str(event.y) + '\n')
            self.points.append([event.x, event.y])
            
            # 前の点が存在するか
            if self.pre_x:
                self.canvas.create_line(self.pre_x, self.pre_y, event.x, event.y, tag="line")

            self.pre_x, self.pre_y = event.x, event.y

    # 座標データを保存する
    def save_text(self):
        f = open('{}.txt'.format(self.file_info[1]), 'w')
        all_text = self.text.get('1.0', tkinter.END)
        f.write(all_text)
        f.close()
    
    # 始点と終点を結ぶ
    def tie_points(self):
        self.canvas.create_line(self.points[0][0], self.points[0][1], self.pre_x, self.pre_y)

    # 点を一つ戻す
    def delete_point(self):
        self.canvas.delete("oval")
        self.canvas.delete("line")
        self.text.delete('1.0', tkinter.END)

        self.points.pop(-1)
        if not self.points:
            self.pre_x, self.pre_y = None, None
        else:
            self.pre_x, self.pre_y = self.points[-1]



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
        self.fillArea.save_Tdata(self.file_info)
        self.destroy()

    # 多角形を塗りつぶす
    def fill_polygon(self):
        self.fillArea.fill_polygon(self.points, self.file_info)
        


if __name__ == '__main__':
    contour = Contour_creator(["chap4-1-1.png", "chap4-1-1", 320, 320])
    contour.create_widgets()
    contour.mainloop()