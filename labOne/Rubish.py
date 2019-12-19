from Circle import Circle
from Shape import Shape
from Bagel import Bagel
from Rectangle import Ractangle
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos
import sys

class Rubish:
    def __init__(self, window = (300, 300), shapes = [Ractangle(), Circle(), Bagel(), Bagel(position = [1.0,1.0, -2.0]) ]): 
        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0  
        self.deltaX = 0
        self.deltaZ = 0
        self.deltaY = 0
        self.Radius = 0

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(window[0],window[1])
        glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        glutInit(sys.argv)
        self.window = window
        #draw window
        self.bgColor = [0.0,0.0,0.0,0.0]
        glutCreateWindow("Rubish".encode("UTF8"))
        self.shapes = shapes
        glutSpecialFunc(self.specialKey)
        glutSpecialUpFunc(self.xKey)
        glutIdleFunc(self.draw)


    def xKey(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.deltaZ = 0
        if key == GLUT_KEY_RIGHT:
            self.deltaZ = 0
        if key == GLUT_KEY_UP:
            self.deltaX = 0
        if key == GLUT_KEY_DOWN:
            self.deltaX = 0
    def specialKey(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.deltaZ = 10
        if key == GLUT_KEY_RIGHT:
            self.deltaZ =  - 10
        if key == GLUT_KEY_UP:
            self.deltaX = 10
        if key == GLUT_KEY_DOWN:
            self.deltaX =  - 10
        if key == GLUT_KEY_F1:
            sys.exit()
    def draw(self):
        glLoadIdentity()
        glTranslatef(0,0,-5)
        self.angleX += self.deltaX
        self.angleY += self.deltaY
        self.angleZ += self.deltaZ
        glRotatef(self.angleX, 1, 0, 0)
        glRotatef(self.angleY, 0, 1, 0)
        glRotatef(self.angleZ, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for shape in self.shapes[::-1]:
            shape.draw()
        glutSwapBuffers()


    def setUI(self, angle = 60):
        self.bgColor[1] += 1
        glClearColor(self.bgColor[0], self.bgColor[1], self.bgColor[2], self.bgColor[3])

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

        LightingSettings = [{"light":GL_LIGHT0, "pos":(0, 1, 0, 0), "dir":(0, 0, 0), "color":(1, 0, 0, 0.4)},
                            {"light":GL_LIGHT1, "pos":(-1, 1, 0, 0), "dir":(0, 0, 0), "color":(0, 1, 0, 0.5)},
                            {"light":GL_LIGHT2, "pos":(1, 1, 1, 0), "dir":(0, 0, 0), "color":(0, 0, 1, 0.6)}]
        glClearColor(0.0, 0.0, 0.0, 1.0)

        for light in LightingSettings:
            glEnable(light["light"])
            glLightfv(light["light"], GL_POSITION, light["pos"])
            glLightfv(light["light"], GL_SPOT_DIRECTION, light["dir"])
            glLightfv(light["light"], GL_DIFFUSE, light["color"])

        glEnable(GL_DEPTH_TEST)

    def start(self):
        self.setUI()
        self.setLight()
        glutMainLoop()