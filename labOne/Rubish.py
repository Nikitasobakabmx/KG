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

        self.fog = False
        image = Image.open("image.jpeg")
        self.ix = image.size[0]
        self.iy = image.size[1]
        self.image = image.convert('RGBX').tobytes() 

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
        self.ListGen()

    def ListGen(self):
        self.listIndex = 1
        if self.listIndex != 0:
            glNewList(self.listIndex, GL_COMPILE)
            glutWireTorus(0.1 ,2, 800, 60)
            self.shapes[0].drawHM()
            glEndList()

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

    #magic don't touch
    def drawFromList(self, pos , scale ):
        glPushMatrix()
        glEnable(GL_CULL_FACE)
        glEnable(GL_COLOR_MATERIAL)
        glColor(1, 1, 1, 1)
        
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_REPLACE)
        glBindTexture(GL_TEXTURE_2D,self.texture)
        
        glScalef(scale, scale, scale)
        glTranslatef(pos[0], pos[1], pos[2])
        glRotatef(self.ListX, 1, 0, 0)
        glRotatef(self.ListY, 0, 1, 0)
        glRotatef(self.ListZ, 0, 0, 1)
        glCallList(self.listIndex)
        
        self.ListX += 0.1
        self.ListY += 0.1
        self.ListZ += 0.1
        
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_COLOR_MATERIAL)
        glEnable(GL_CULL_FACE)
        glPopMatrix()

    def fogSetup(self):
        glEnable(GL_FOG)
        glFogi(GL_FOG_MODE, GL_LINEAR)
        glFogfv(GL_FOG_COLOR, (1, 1, 1, 0.1))
        glFogf(GL_FOG_DENSITY, 0.35)
        glHint(GL_FOG_HINT, GL_DONT_CARE)
        glFogf(GL_FOG_START, 1.0)
        glFogf(GL_FOG_END, 5.0) 

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
        tmp = [{"pos":(0, -1, -3),"scale":0.2},
                {"pos":(1, -2, -4),"scale":0.3},
                {"pos":(3, -3, -5),"scale":0.4},
                {"pos":(-2, 1, -5),"scale":0.5},
                {"pos":(-5, -4, -5),"scale":0.6},
                {"pos":(-2, -1, -3),"scale":0.7},
                {"pos":(-1, -2, -4),"scale":0.8},
                {"pos":(-4, -5, -8),"scale":0.9}]
        for i in tmp:
            self.drawFromList(i["pos"], i["scale"])      
        for shape in self.shapes[::-1]:
            shape.draw()
        if self.fog:
            print("hehe")
            self.fogSetup()
        else:
            glDisable(GL_FOG)
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


    