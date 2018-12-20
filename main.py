from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from time import sleep, time
from math import sin, cos, pi
from random import randint

TITLE = "Random Patterns"
WIDTH, HEIGHT = 600, 600

ANCHORS = 3.
RADIUS = WIDTH/2
FRACTION = 1/2.

class App:
    def __init__(self, title):
        self.title = title
        return

    def create_window(self,width, height, fullscreen=False):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width,height)
        glutCreateWindow(self.title.encode())
        self.width, self.height = width, height
        glEnable(GL_COLOR_MATERIAL)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glDisable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)
        glEnable (GL_BLEND)
        glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        return

class Pointer:
    def __init__(self):
        self.x=self.y=0
        return

    def move(self,x,y):
        self.x+=x
        self.y+=y
        return
     
def main():
    pointer = Pointer()
    def draw():
        glLoadIdentity()
        glOrtho(0,WIDTH,HEIGHT,0,-1,1)

        glPushMatrix()
        glTranslate(WIDTH/2,HEIGHT/2,0)

        anchor = randint(0,ANCHORS-1)
        anchorX, anchorY = cos(2*pi/ANCHORS*anchor),sin(2*pi/ANCHORS*anchor)
        dX = anchorX * RADIUS - pointer.x
        dY = anchorY * RADIUS - pointer.y
        pointer.move(dX*FRACTION,dY*FRACTION)
        for i in range(2):
            glBegin(GL_POINTS)
            glVertex2f(pointer.x,pointer.y)
            glEnd()
            glutSwapBuffers()

        glPopMatrix()
        return

    def keyboard_down(key, x, y):
        ''' Keyboard repeat is enabled by default '''
        ''' x and y represent the mouse position  '''
        if key == b'\x1b': # ESC key
            glutLeaveMainLoop()
        return
    
    app = App(TITLE)
    app.create_window(WIDTH,HEIGHT)
    glutDisplayFunc( draw )              
    glutIdleFunc( draw )
    glutKeyboardFunc( keyboard_down )   
    glClearColor(0,0,0, 0);
    glutMainLoop()
    return

if __name__ == "__main__":
    main()
