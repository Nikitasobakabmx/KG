from Circle import Circle
from Shape import Shape
from Rectangle import Ractangle
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

class Rubish:
    def __init__(self, window = (300, 300), shapes = [ Circle(), Ractangle(), ]):   
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(window[0],window[1])
        glutInit(sys.argv)
        self.window = window
        #draw window
        glutCreateWindow("Rubish".encode("UTF8"))
        self.shapes = shapes
        for shape in shapes:
            glutIdleFunc(shape.draw)

        
    def setUI(self, bgColor = (0.0,0.0,0.0,0.0), angle = 30):
        self.bgColor = bgColor
        glClearColor(bgColor[0], bgColor[1], bgColor[2], bgColor[3])

        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   #rm shde
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()    #load curent matrix

        gluPerspective(angle, float(self.window[0])/float(self.window[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        
        # glEnable(GL_TEXTURE_2D)
        # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        # glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    
    def setLight(self, light = 0):
        glEnable(GL_LIGHTING)

        lightPosition = (1, 1, 0, 0.0)
        lightSetting = (0.5, 0.5, 0.5, 1.0)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lightSetting)
        glEnable(GL_DEPTH_TEST)

    def start(self):
        self.setUI()
        self.setLight()
        glutMainLoop()