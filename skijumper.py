from ggame import App, RectangleAsset, ImageAsset, Frame, SoundAsset, TextAsset
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
#values chosen by the user
h = int(input('enter the h value of a parabola in the form y=(x-h)^2+k: '))
k = int(input('enter the k value of a parabola in the form y=(x-h)^2+k: '))
#this is the image used to represent the skier
skier_asset = ImageAsset("images/Python Skiier.png", Frame(0,0,685,685))
skier = Sprite(skier_asset, (50, 160))
skier.fxcenter=.5
skier.fycenter=.7
skier.scale = 0.2
skier.rotation = .3
#here is the parametric used to later find the derivtive for the tilt, and here it is also centering the grid
xfunc = lambda t: 8*t+480
yfunc = lambda t:-((t-h)**2)+k + 340
for t in range(-30, 30):
    Ypoints = yfunc(t)
    Xpoints = xfunc(t)
    point = CircleAsset(4, thinline, black)
    Sprite(point, (Xpoints, Ypoints))
print(' ')
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
sendit = TextAsset("Send It!", style="bold 40pt Arial", width=250)
Sprite(sendit, (100, 100))

myapp = App()
myapp.run(step)