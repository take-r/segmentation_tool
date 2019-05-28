from sympy.geometry import Point, Polygon
from PIL import Image, ImageDraw

class FillArea():
    def __init__(self, points_data):
        self.polygon_points = []
        for i in range(len(points_data)):
            self.polygon_points.append(tuple(points_data[i]))

        self.points = tuple(self.polygon_points)
        img = Image.new('L', (320,320), 0)
        draw = ImageDraw.Draw(img)
        draw.polygon(self.points, fill=192)
        img.save("pic.png")
        

    


    
if __name__ == "__main__":
    fillArea = FillArea(((5,5),(100,100),(100,300)))

