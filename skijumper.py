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
thinline = LineStyle(1, black)

"""



print('Enter the folowing values of the domain and function y = ax^2 + bx + c of your ski jump: ')
x1 = float(input('left domain = '))
x2 = float(input('right domain = '))
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

y = a*('x'**2) + b*'x' + c
print(y)

y1 = 2*a*x + b 





"""
#g=9.81m/s^2
#a=g*sinangle
#h(x) = ax^2 + bx + c 
#h'(x) = 2ax +b
#def height(x):
    #slope(x): 
y=ax^2+bx+x
y=2ax+ b
x min
x max
a
b
c
"""
    
#myapp = skijump()
myapp.run()