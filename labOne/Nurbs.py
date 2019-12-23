from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Nurbs:
    def __init__(self):
        self.ctrlPoints = [ [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        self.Nurb = gluNewNurbsRenderer()
        gluNurbsProperty(self.Nurb,GLU_SAMPLING_TOLERANCE,2.0)
        gluNurbsProperty(self.Nurb,GLU_DISPLAY_MODE,GLU_FILL)
        gluNurbsCallback(self.Nurb, GLU_ERROR, self.callBack)

    def init_surface(self):
        for i in range(4):
            for j in range(4):
                self.ctrlPoints[i][j][0] = 2 * (i - 1.5)
                self.ctrlPoints[i][j][1] = 2 * (j - 1.5)
                if (i == 1 or i == 2) and (j == 1 or j == 2):
                    self.ctrlPoints[i][j][2] = 2
                else:
                    self.ctrlPoints[i][j][2] = -2

    def draw(self):
        knots =[0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0]
        glPushMatrix()
        #glScalef(1,10, 10)
        gluBeginSurface(self.Nurb)

        glEnable(GL_CULL_FACE)
        glEnable(GL_COLOR_MATERIAL)
        glColor(1, 1, 1, 1)
        glRotatef(270, 1, 0, 0)
        glRotatef(0, 0, 1, 0)
        glRotatef(0, 0, 0, 1)


        gluNurbsSurface(self.Nurb, knots, knots, self.ctrlPoints, GL_MAP2_VERTEX_3)
        
        gluEndSurface(self.Nurb)
        #if(showPoints)
        #  {
        #  glPointSize(5.0);
        #  glDisable(GL_LIGHTING);
        #  glColor3f(1.0,1.0,0.0);
        #  glBegin(GL_POINTS);
        #  for(i=0;i<4;i++)
        #  for(j=0;j<4;j++)
        #  glVertex3fv(&ctrlpoints[i][j][0]);
        #  glEnd();
        #  glEnable(GL_LIGHTING);
        #  } 
        
        
        glPopMatrix() 

    def callBack(self, msg):
        print(msg)