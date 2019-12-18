from Circle import Circle
from Shape import Shape
from Bagel import Bagel
from Rectangle import Ractangle
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

class Rubish:
    def __init__(self, window = (300, 300), shapes = [Ractangle(), Circle(), Bagel(), Bagel(position = [1.0,1.0,-12.0]) ]):   
        self.dx = 1
        self.dy = 1
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(window[0],window[1])
        glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        glutInit(sys.argv)
        self.window = window
        #draw window
        self.bgColor = [0.0,0.0,0.0,0.0]
        glutCreateWindow("Rubish".encode("UTF8"))
        self.shapes = shapes
        glutIdleFunc(self.draw)
        #callbak om kayboard and mouse
        glutSpecialFunc(self.specialKey)

    def draw(self):
        
        #scene
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #glTranslatef(0, 0, 0)
        glRotated(self.dx,1,0,0)
        glRotated(self.dy,0,1,0)

        for shape in self.shapes[::-1]:
            shape.draw()
        glutSwapBuffers()



    def mathSheet(self, x, y):
        new_x = 

        hRadians += h;
vRadians += v;

cam_target.y = cam_position.y+(float)(radius*sin(vRadians));
cam_target.x = cam_position.x+(float)(radius*cos(vRadians)*cos(hRadians));
cam_target.z = cam_position.z+(float)(radius*cos(vRadians)*sin(hRadians));

cam_up.x = cam_position.x-cam_target.x;
cam_up.y = ABS(cam_position.y+(float)(radius*sin(vRadians+PI/2))) ;
cam_up.z = cam_position.z-cam_target.z;

    def specialKey(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.dy += 5
        if key == GLUT_KEY_DOWN:
            self.dy += - 5
        if key == GLUT_KEY_LEFT:
            self.dx += - 7
        if key == GLUT_KEY_RIGHT:
            self.dx += 180
        if key == GLUT_KEY_F1:
            sys.exit()

    def setUI(self, angle = 30):
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

        lightColor = (0, 1, 0, 0)
        lightPosition = (0, 1, 0, 0)
        lightDirection = (0, 0, 0)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_LIGHT0)
        
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, lightDirection)

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lightColor)
        glEnable(GL_DEPTH_TEST)

    def start(self):
        self.setUI()
        self.setLight()
        glutMainLoop()