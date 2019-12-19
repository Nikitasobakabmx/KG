from Shape import Shape
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Ractangle(Shape):
    def __init__(self, size = 1, color = (0,0,0,1), position = [1.0,1.0, -2.0]):
        self.pos = position
        self.size = size
        self.color = color
        self.xRot = 0.0
        self.yRot = 0.0
        self.zRot = 0.0

    def draw(self):
        #rotation
        glPushMatrix()
        red = [0, 0, 0, 1]
        glEnable(GL_COLOR_MATERIAL)
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, red)
        #glColorMaterial(GL_FRONT_AND_BACK, red)
        # glColorMaterial(GL_BACK, GL_AMBIENT)

        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glRotatef(self.xRot,1,0,0)
        glRotatef(self.yRot,0,1,0)
        glRotatef(self.zRot,0,0,1)

        glutSolidCube(self.size)
        
        #rotation per frame
        self.xRot = self.xRot + 0.25
        self.yRot = self.yRot + 0.25

        glPopMatrix()
        