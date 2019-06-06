from sympy.geometry import Point, Polygon
from PIL import Image, ImageDraw

class FillArea():
    def __init__(self, Tdata_wid, Tdata_heig):
        self.img = Image.new('L', (Tdata_wid, Tdata_heig), 0)
    
    def fill_polygon(self, points_data, file_info):
        self.polygon_points = []
        for i in range(len(points_data)):
            self.polygon_points.append(tuple(points_data[i]))

        self.points = tuple(self.polygon_points)
        draw = ImageDraw.Draw(self.img)
        draw.polygon(self.points, fill=192)

        
    def save_Tdata(self, file_info):
        self.img.save("{}_seg.png".format(file_info[1]))


        

    


    
if __name__ == "__main__":
    fillArea = FillArea(((5,5),(100,100),(100,300)), ["", "", 320, 320])

