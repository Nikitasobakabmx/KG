from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Shape import Shape


class Circle(Shape):
    def __init__(self, radius = 0.8, position = (-1.0,-1.0,1.0)):
        self.radius = radius
        self.pos = position
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

    def draw(self):
        glPushMatrix()

        #rotate
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glRotatef(self.xRot,1,0,0)
        glRotatef(self.yRot,0,1,0)
        glRotatef(self.zRot,0,0,1)

        glDisable(GL_CULL_FACE)
        glEnable(GL_COLOR_MATERIAL)
        glColor4f(1,1,1,1)
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT, (0, 0, 0))
        glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE, (0, 0, 0))
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR, (0, 0, 0))
        glMaterialf(GL_FRONT,GL_SHININESS, 0)
        #glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glutSolidSphere(self.radius, 100, 15)
        glDisable(GL_COLOR_MATERIAL)
        glEnable(GL_CULL_FACE)
        glPopMatrix()
        self.xRot = self.xRot + 0.4
        self.yRot = self.yRot + 0.4