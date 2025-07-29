from cmu_graphics import *

def onAppStart(app):
    app.rectW = app.width
    app.rectH = app.height

def redrawAll(app):
## initial background soccer field
    drawRect(0, 0, app.rectW, app.rectH, fill = 'green', opacity = 90 )
    drawLine(app.width/2, 0, 200, app.height, fill = 'white')
    # right goal area
    drawLine(0, 150, 50, 150, fill = 'white')
    drawLine(50, 150, 50, 250, fill = 'white')
    drawLine(0, 250, 50, 250, fill = 'white')
    #left goal area
    drawLine(app.width - 50, 150, app.width, 150, fill = 'white')
    drawLine(app.width - 50, 150, app.width - 50, 250, fill = 'white')
    drawLine(app.width - 50, 250, app.width, 250, fill = 'white')
    
    # pillars to jump through
    drawPillars(app)
    
    
def drawPillars(app):
    #top pillars
    for i in range(5):
        x0 = (60 * i) + 120
        drawRect(x0, 0, 30, 170, fill = 'pink', border = 'black')
    #bottom pillars
    for j in range(5):
        x0 = (60 *j) + 120
        drawRect(x0, 270, 30, app.height, fill = 'pink', border = 'black')
      
    
    
    
   

def main():
    runApp()

main()

cmu_graphics.run()