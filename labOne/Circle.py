from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Circle:
    def __init__(self):
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

    def draw(self, position = (0.75, 0.75, 0.75), radius = 0.5):
        self.xRot = self.xRot + 1
        self.yRot = self.yRot + 1
        self.zRot = self.zRot + 1       
        mat_emission = [0.0, 0.0, 0.2, 0.0]
        no_mat_emission = (0.0, 0.0, 0.2, 1.0)
        mat_diffuse = (0.1, 0.5, 0.0, 1.0)
        mat_specular = (1.0, 1.0, 1.0, 1.0)
        low_shininess = (4.0)   
        glPushMatrix()
        glTranslatef(0.75, 0.75, 0.75)
        glRotatef(self.xRot,1,0,0)
        glRotatef(self.yRot,0,1,0)
        glRotatef(self.zRot,0,0,1)
	    # glMaterialfv(GL_FRONT, GL_AMBIENT, (0.0, 0.0, 0.2, 0.0))
	    # glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	    # glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	    # glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess)
	    # glMaterialfv(GL_FRONT, GL_EMISSION, no_mat_emission)
        glMaterialfv(GL_FRONT,GL_AMBIENT,[0.1745,0.0,0.1,0.0])
        glMaterialfv(GL_FRONT,GL_DIFFUSE,[0.6, 0.0, 0.1, 0.0])
        glMaterialfv(GL_FRONT,GL_SPECULAR,[0.7, 0.6, 0.8, 0.0])
        glutSolidSphere(radius, 16, 16)
        glPopMatrix()