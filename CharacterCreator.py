
from graphics import*

from Button import*
#star means all
#allows python to copy and paste 
    
def main():
    window = GraphWin("character creator", 800, 600)
#firt is name of window
#width of how many pixels wide your window will be
#tallness of how many pixels window will be
    C = Circle(Point(300, 300), 175)
#point defined by x and y pixel
#radius also taken
    C.draw(window)
#the win inside draw specifies which window if there are multiple
#objects default to be hidden
    #R = Rectangle(Point(200,500), Point(400,575))
    #R.draw(window)

    Mouth = Line(Point(200,375), Point(400,375))
    
    
    HappySmile1 = (Line(Point(200,375), Point(175,350)))
    HappySmile2 = (Line(Point(400,375), Point(425,350)))
    
    
    SadSmile1 = (Line(Point(200,375), Point(175,400)))
    SadSmile2 = (Line(Point(400,375), Point(425,400)))
  

    SmallNose = Polygon(Point(300,275), Point(325,325), Point (275,325))
    BigNose = Polygon(Point(300,250), Point(350,350), Point (250,350))
    
    
    BigEye1 = Circle(Point(200, 250), 50)
    BigEye2 = Circle(Point(400, 250), 50)
    
    SmallEye1 = Circle(Point(225, 250), 20)
    SmallEye2 = Circle(Point(375, 250), 20)

    Hair1 = (Line(Point(300,100), Point(300,125)))
    
    Hair2 = (Line(Point(260,105), Point(265,130)))
    
    Hair3 = (Line(Point(340,105), Point(335,130)))
    
    
    B = Button(window, Point(650,100), Point(750,175), "LightSteelBlue1", "Big Eyes")
    B2 = Button(window, Point(650,200), Point(750,275), "LightSteelBlue1", "Small Eyes")
    B3 = Button(window, Point(650,300), Point(750,375), "LightSteelBlue1", "Bald")
    B4 = Button(window, Point(650,400), Point(750,475), "LightSteelBlue1", "Hair")
    B5 = Button(window, Point(200,500), Point(300,575), "LightSteelBlue1", "Sad")
    B6 = Button(window, Point(50,500), Point(150,575), "LightSteelBlue1", "Happy")
    B7 = Button(window, Point(350,500), Point(450,575), "LightSteelBlue1", "Small Nose")
    B8 = Button(window, Point(500,500), Point(600,575), "LightSteelBlue1", "Big Nose")
    Q = Button(window, Point(650, 500), Point(750,575), "misty rose", "QUIT")
#takes window, p1, p2, color, and text
#colors should be recognizable as strings
    '''for i in range(5):
        M = window.getMouse()
        if B. isClicked(M):
            C2 = Circle(Point(400,300),20 + 10*i)
            C2.draw(window)
    #M becomes point to see if that is button'''
# win.setBackground("cyan") to change colors between window backgrounds
    '''i = 1
    Q = Button(window, Point(600,300), Point(700,375), "LightSteelBlue1", "Click Me")
    while True:
        M = window.getMouse()
        if B. isClicked(M):
            C2 = Circle(Point(400,300),20 + 10*i)
            C2.draw(window)
        if Q.isClicked(M):
            break
        i = i + 1
    window.close()'''

    
    while True:
        M = window.getMouse()
        
        if B.isClicked(M):
            BigEye1.undraw()
            BigEye2.undraw()

            SmallEye1.undraw()
            SmallEye2.undraw()
            
            BigEye1.draw(window)
            BigEye2.draw(window)

        if B2.isClicked(M):
            SmallEye1.undraw()
            SmallEye2.undraw()
            
            BigEye1.undraw()
            BigEye2.undraw()

            SmallEye1.draw(window)
            SmallEye2.draw(window)
            
        if B3.isClicked(M):
            Hair1.undraw()
            Hair2.undraw()
            Hair3.undraw()
            
        if B4.isClicked(M):

            Hair1.draw(window)
            Hair2.draw(window)
            Hair3.draw(window)

        if B5.isClicked(M):
            Mouth.undraw()
            
            SadSmile1.undraw()
            SadSmile2.undraw()
            
            HappySmile1.undraw()
            HappySmile2.undraw()

            SadSmile1.draw(window)
            SadSmile2.draw(window)

            Mouth.draw(window)
            
        if B6.isClicked(M):
            Mouth.undraw()
            
            HappySmile1.undraw()
            HappySmile2.undraw()

            SadSmile1.undraw()
            SadSmile2.undraw()
            
            HappySmile1.draw(window)
            HappySmile2.draw(window)
            
            Mouth.draw(window)
        if B8.isClicked(M):
            
            BigNose.undraw()

            SmallNose.undraw()
            
            BigNose.draw(window)
            
        if B7.isClicked(M):
            
            SmallNose.undraw()

            BigNose.undraw()
            
            SmallNose.draw(window)
            
        if Q.isClicked(M):
            break

    window.close()
    
# M becomes point to see
# a button can tell you when to stop (can break the loop0
    
    
if __name__ == "__main__":
    main()
