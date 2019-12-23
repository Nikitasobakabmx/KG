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

    def drawHM(self):
        glPushMatrix()

        glBegin(GL_QUADS)

        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)

        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)
        
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)

        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)

        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)

        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)

        glEnd()
        glPopMatrix()

    def draw(self):
        #rotation
        glPushMatrix()
        red = [0, 0, 0, 1]
        glDisable(GL_CULL_FACE)
        glEnable(GL_COLOR_MATERIAL)
        glColor4f(0,0,0,0.3)
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT, (1, 0, 0))
        glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE, (0, 0, 1))
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR, (0, 1, 0))
        glMaterialf(GL_FRONT,GL_SHININESS, 127)
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

        glDisable(GL_COLOR_MATERIAL)
        glEnable(GL_CULL_FACE)
        glPopMatrix()
        