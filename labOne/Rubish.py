from Circle import Circle
from Shape import Shape
from Bagel import Bagel
from Rectangle import Ractangle
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos
from PIL import Image
import sys
from copy import deepcopy
from Nurbs import Nurbs

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

        self.ListX = 0
        self.ListY = 0
        self.ListZ = 0

        image = Image.open("image.jpeg")
        self.ix = image.size[0]
        self.iy = image.size[1]
        self.image = image.convert('RGBX').tobytes() 

        self.depthMapFBO = glGenFramebuffers(1)

        self.Nurb = Nurbs()   
        self.Nurb.init_surface()
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
        self.setUI()

   
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
        if key == GLUT_KEY_F2:
            self.fog = False
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
        if key == GLUT_KEY_F2:
            self.fog = True
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
        glPushMatrix()

        glEnable(GL_TEXTURE_2D)
        glTranslatef(0, 1, -4)

        glRotatef(self.ListX, 1, 0, 0)
        glRotatef(self.ListY, 0, 1, 0)
        glRotatef(self.ListZ, 0, 0, 1)

        self.ListX += 2
        self.ListY += 2
        self.ListZ += 2

        glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_REPLACE)
        glBindTexture(GL_TEXTURE_2D,self.texture)
        self.shapes[0].drawHM()
        glDisable(GL_TEXTURE_2D)

        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, -2, -4)
        self.Nurb.draw()
        glPopMatrix()
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
    
        #trextures       
        self.texture = glGenTextures(1) 
        glBindTexture(GL_TEXTURE_2D,self.texture)

        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, self.ix, self.iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        #Nurb
        glEnable(GL_AUTO_NORMAL)
        glEnable(GL_NORMALIZE) 

        #shadow
        glBindFramebuffer(GL_FRAMEBUFFER, self.depthMapFBO)    
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, self.texture, 0)
        glDrawBuffer(GL_NONE)
        glReadBuffer(GL_NONE)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)


    def setLight(self, light = 0):
        glEnable(GL_LIGHTING)
        glLoadIdentity()
        glTranslatef(0,0,0)
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
        # self.setUI()
        glutMainLoop()


    