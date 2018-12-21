"""
Fork this repository to begin working on your final project. Then do the following:
* Edit the file called "functional.md" to describe the **functionality** of your project.
* Edit the file called "design.md" to describe the **design** of your project.
* Add your python sources.
* When the project is finished, make  pull request to let me know you're finished.


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

deriv = (-z/10)

xfunc = lambda z: 20*(z+(150/8))
    
yfunc = lambda z: (-1*(z**2))+400
  
xlist = [xfunc(d/10) for d in range(-150, 100)]
ylist = [yfunc(d/10) for d in range(-150, 100)]
zlist = [d/10 for d in range(-150, 100)]

zindex  = 0
def step ():
    global zindex
    if zindex < len(xlist):
        skier.position = (xlist[zindex], ylist[zindex])
        skier.rotation = atan(zlist[zindex]/10) + .37
        zindex += 1

myapp = App()
myapp.run(step)
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

h = int(input('enter the h value of a parabola in the form y=(x-h)^2+k: '))
k = int(input('enter the k value of a parabola in the form y=(x-h)^2+k: '))

skier_asset = ImageAsset("images/Python Skiier.png", Frame(0,0,685,685))
skier = Sprite(skier_asset, (50, 160))
skier.fxcenter=.5
skier.fycenter=.7
skier.scale = 0.2
skier.rotation = .3


xfunc = lambda t: 20*t+480
    
yfunc = lambda t:-((t-h)**2)+k + 380


for t in range(-50, 50):
    Ypoints = yfunc(t)
    Xpoints = xfunc(t)
    point = CircleAsset(4, thinline, black)
    Sprite(point, (Xpoints, Ypoints))
print(' ')

#rectangle1  = RectangleAsset(30, 700, thinline, black)
#Sprite(rectangle1, (40,170))
#rectangle2  = RectangleAsset(12,400, thinline, black)
#Sprite(rectangle2, (455,390))

for t in range(-100,100):
    deriv = 2*(t-h)

  
xlist = [xfunc(t/10) for t in range(-500, 500)]
ylist = [yfunc(t/10) for t in range(-500, 500)]
zlist = [t/10 for t in range(-500, 500)]
zindex  = 0

def step ():
    global zindex
    if zindex < len(xlist):
        skier.position = (xlist[zindex], ylist[zindex])
        skier.rotation = atan(zlist[zindex]/10) + .37
        zindex += 1

myapp = App()
myapp.run(step)
