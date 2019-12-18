from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Shape import Shape

class Bagel(Shape):
    def __init__(self, radius = 1, position = (-1.0,-1.0,-10.0)):
        self.pos = position
        self.radius = radius
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

    def draw(self):
        glPushMatrix()
        glLoadIdentity() 
        #rotate
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glRotatef(self.xRot,1,0,0)
        glRotatef(self.yRot,0,1,0)
        glRotatef(self.zRot,0,0,1)

        color = [1, 1, 1, 1]
        glEnable(GL_COLOR_MATERIAL)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glColor3f(color[0], color[1], color[2])
        #glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glutWireTorus(0.1 ,self.radius, 800, 60)

        glPopMatrix()

        self.xRot = self.xRot + 0.4
        self.yRot = self.yRot + 0.4
        self.zRot = self.zRot + 0.2