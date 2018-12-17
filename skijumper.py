"""
Fork this repository to begin working on your final project. Then do the following:
* Edit the file called "functional.md" to describe the **functionality** of your project.
* Edit the file called "design.md" to describe the **design** of your project.
* Add your python sources.
* When the project is finished, make  pull request to let me know you're finished.
"""
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
thinline = LineStyle(1, blue)

skier_asset = ImageAsset("images/Python Skiier.png", Frame(0,0,685,685))
skier = Sprite(skier_asset, (50, 160))
skier.fxcenter=.5
skier.fycenter=.7
skier.scale = 0.2
skier.rotation = .3

for z in range(-15, 6):
    Ypoints = (-1*(z**2))+400
    Xpoints = 20*(z+(150/8))
    point = CircleAsset(4, thinline, black)
    Sprite(point, (Xpoints, Ypoints))
print(' ')

rectangle1  = RectangleAsset(30, 700, thinline, black)
Sprite(rectangle1, (40,170))
rectangle2  = RectangleAsset(12,400, thinline, black)
Sprite(rectangle2, (455,390))
"""
if Xpoints in range(-15,1):
    skier.rotation == z*-0.3
            
if Xpoints in range(0,1):
    skier.rotation == .3
            
elif Xpoints in range(1,6):
            skier.rotation == .3*z
"""  
#Goal: Find all x points by small parts, find the slope of that point for tilt, inverse tan of the angle, speed?
for z in range (-150, 60):
    
xfunc(z)
yfunc(z)
#slope? #derivative? how do you find it of a parametric?

def  xfunc(z);
return
    
xfunc = lambda z:
    

STOP();
skier.x=xfunc(z)
skier.y=yfunc(z)
skier.rotation = #derivative? how do you find it of a parametric?

def step ():
       
myapp = App()
myapp.run(step)