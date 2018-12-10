"""
Fork this repository to begin working on your final project. Then do the following:
* Edit the file called "functional.md" to describe the **functionality** of your project.
* Edit the file called "design.md" to describe the **design** of your project.
* Add your python sources.
* When the project is finished, make  pull request to let me know you're finished.
"""
#g=9.81m/s^2
#a=g*sinangle
#h(x) = ax^2 + bx + c 
#h'(x) = 2ax +b
#def height(x):
    slope(x): 
    


from ggame import App, RectangleAsset, ImageAsset, Frame, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import CircleAsset, LineStyle, Color, Sprite, App, RectangleAsset
from math import sin,cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2

myapp = App()

red = Color(0xFF4040, 1.0)
green = Color(0x00FF00, 1.0)
blue = Color(0x1C86EE, 1.0)
white = Color(0xF8F8FF, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xFF7D40, 1.0)
thinline1 = LineStyle(1, black)
thinline = LineStyle(1, black)

skier_asset = ImageAsset("images/Python Skiier.png", Frame(0,0,685,685))
skier = Sprite(skier_asset, (-30, 70))
skier.scale = 0.2
"""
skier.direction = 1
skier.go = True
"""
for z in range(-15, 6):
    Ypoints = (-1*(z**2))+400
    Xpoints = 20*(z+(150/8))
    point = CircleAsset(4, thinline, black)
    Sprite(point, (Xpoints, Ypoints))
print(' ')

rectangle1 = RectangleAsset(12, 700, thinline, black)

Sprite(rectangle1, (63,175))

rectangle2  = RectangleAsset(12,400, thinline, black)

Sprite(rectangle2, (474,384))






myapp = App()
myapp.run()