from Shape import Shape
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Ractangle(Shape):
    def __init__(self, size = 0.5, color = (0,0,0,1)):
        self.size = size
        self.color = color
        self.xRot = 0.0
        self.yRot = 0.0
        self.zRot = 0.0

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glLoadIdentity()

        #rotation
        glTranslatef(0.0,0.0,-10.0)
        glRotatef(self.xRot,1,0,0)
        glRotatef(self.yRot,0,1,0)
        glRotatef(self.zRot,0,0,1)

        #magic, don't touch 
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

        #rotation per frame
        self.xRot = self.xRot + 0.25
        self.yRot = self.yRot + 0.25

        glutSwapBuffers()