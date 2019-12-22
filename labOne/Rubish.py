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

        self.KangleX = 0
        self.KangleY = 0
        self.KangleZ = 0  
        self.KdeltaX = 0
        self.KdeltaZ = 0
        self.KdeltaY = 0
        self.KRadius = 0
        self.CtrlPress = False

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
            self.KdeltaZ = 0
            self.deltaZ = 0
        if key == GLUT_KEY_RIGHT:
            self.KdeltaZ = 0
            self.deltaZ = 0
        if key == GLUT_KEY_UP:
            self.KdeltaX = 0
            self.deltaX = 0
        if key == GLUT_KEY_DOWN:
            self.KdeltaX = 0
            self.deltaX = 0
            return
        if key == 114:
            self.CtrlPress = False
            self.KdeltaX = 0
            self.KdeltaY = 0
            self.KdeltaZ = 0
    def specialKey(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            if self.CtrlPress:
                self.KdeltaZ = 10
                return
            self.deltaZ = 10
            return
        if key == GLUT_KEY_RIGHT:
            if self.CtrlPress:
                self.KdeltaZ = -10
                return
            self.deltaZ =  - 10
            return
        if key == GLUT_KEY_UP:
            if self.CtrlPress:
                self.KdeltaX = 10
                return
            self.deltaX = 10
            return
        if key == GLUT_KEY_DOWN:
            if self.CtrlPress:
                self.KdeltaX = -10
                return
            self.deltaX =  - 10
            return
        if key == GLUT_KEY_F1:
            sys.exit()
            return
        if key == 114:
            self.CtrlPress = True

    def draw(self):
        self.setLight()
        glLoadIdentity()
        glTranslatef(0,0,-5)
        self.angleX += self.deltaX
        self.angleY += self.deltaY
        self.angleZ += self.deltaZ
        glRotatef(self.KangleX, 1, 0, 0)
        glRotatef(self.KangleY, 0, 1, 0)
        glRotatef(self.KangleZ, 0, 0, 1)
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
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glLoadIdentity()    #load curent matrix

        gluPerspective(angle, float(self.window[0])/float(self.window[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        
        # glEnable(GL_TEXTURE_2D)
        # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        # glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    
    def setLight(self, light = 0):
        glEnable(GL_LIGHTING)
        glLoadIdentity()
        glTranslatef(0,0,-5)
        self.KangleX += self.KdeltaX
        self.KangleY += self.KdeltaY
        self.KangleZ += self.KdeltaZ
        glRotatef(self.angleX, 1, 0, 0)
        glRotatef(self.angleY, 0, 1, 0)
        glRotatef(self.angleZ, 0, 0, 1)

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
        glutMainLoop()