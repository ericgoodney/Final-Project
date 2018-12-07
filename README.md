# Ski Jumper

Fork this repository to begin working on your final project. Then do the following:

* Edit the file called "functional.md" to describe the **functionality** of your project.
* Edit the file called "design.md" to describe the **design** of your project.
* Add your python sources.
* When the project is finished, make  pull request to let me know you're finished.
from ggame import CircleAsset, LineStyle, Color, Sprite, App, RectangleAsset
from math import sin,cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2


black = Color(0x000000, 1.0)
blue = Color(0x0000FF, 1.0)
red = Color(0xDC143C, 1.0)
thinline = LineStyle(2, black)


for z in range(-15, 6):
    Ypoints = (-1*(z**2))+400
    Xpoints = 20*(z+(150/8))
    point = CircleAsset(4, thinline, black)
    Sprite(point, (Xpoints, Ypoints))
print(' ')

      
        
        
myapp = App()
myapp.run()