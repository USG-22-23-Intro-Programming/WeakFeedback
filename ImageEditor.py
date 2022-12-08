from graphics import*

from Button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if red >= 50:
                red = red - 50
            else:
                red = 0
            if green >= 50:
                green = green - 50
            else:
                green = 0
            if blue >= 50:
                blue = blue - 50
            else:
                blue = 0

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)

def lighter(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if red <= 205:
                red = red + 50
            else:
                red = 255
            if green <= 205:
                green = green + 50
            else:
                green = 255
            if blue <= 205:
                blue = blue + 50
            else:
                blue = 255

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)


            
def contrast(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if (red + blue + green <= 337.5): 
                if red - 15 > 0:
                    red = red - 15
                else:
                    red = 0
                if green - 15 > 0:
                    green = green - 15
                else:
                    green = 0
                if blue - 15 > 0:
                    blue = blue - 15
                else:
                    blue = 0
            else:
                if red + 15 < 255:
                    red = red + 15
                else:
                    red = 255
                if green + 15 < 255:
                    green = green + 15
                else:
                    green = 255
                if blue + 15 < 255:
                    blue = blue + 15
                else:
                    blue = 255
               
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)
def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            color = (red + green + blue) / 3
            color = round(color)
            c = color_rgb(color, color, color)
            img.setPixel(i, j, c)


def reverse(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = 255 - red
            green = 255 - green
            blue = 255 - blue
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)

def OnlyGreen(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            
            pix = img.getPixel(i,j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if (green > blue) and (green > red):
                pass
            else:
                color = (red + green + blue) / 3
                color = round(color)
                c = color_rgb(color, color, color)
                img.setPixel(i, j, c)
                    

            
def main():
    win = GraphWin("Image Editor", 800, 600)
    B = Button(win, Point(650,100), Point(750,175), "LightSteelBlue1", "Darker")
    B2 = Button(win, Point(650,200), Point(750,275), "LightSteelBlue1", "Lighter")
    B3 = Button(win, Point(650,300), Point(750,375), "LightSteelBlue1", "Contrast")
    B4 = Button(win, Point(650,400), Point(750,475), "LightSteelBlue1", "Grayscale")
    B5 = Button(win, Point(525,100), Point(625,175), "LightSteelBlue1", "Reverse")
    B6 = Button(win, Point(525,200), Point(625,275), "LightSteelBlue1", "OnlyGreen")
    
  
    Q = Button(win, Point(650, 500), Point(750,575), "misty rose", "QUIT")

    img = Image(Point(300,300),"Cats.png")
    img.draw(win)
    
    while True:
        M = win.getMouse()
        
        if B.isClicked(M):
            darken(img)

        if B2.isClicked(M):
            lighter(img)
            
        if B3.isClicked(M):
            contrast(img)
            
        if B4.isClicked(M):
            grayscale(img)

        if B5.isClicked(M):
            reverse(img)

        if B6.isClicked(M):
            OnlyGreen(img)
 
            
        if Q.isClicked(M):
            break

    win.close()

if __name__ == "__main__":
    main()
    


