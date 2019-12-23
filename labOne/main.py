from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

RECTANGLE = 0

class Shape:
    def __init__(self,shape = 0, image = "image.jpeg", sizeX = 450, sizeY = 300, Heder = "Rectangle", key = 0):
        self.shape = shape
        self.fileImage = image
        self.sizeX = sizeX
        self.sizeY = sizeY

        #enum of lightings
        self.lights = (GL_LIGHT0, GL_LIGHT1, GL_LIGHT2, GL_LIGHT3)


        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(sizeX,sizeY)
        glutInit(sys.argv)
        
        #window init
        self.window = glutCreateWindow(Heder.encode("UTF8"))
        if shape == 0:
            #glutDisplayFunc(self.drawRectangle)
            glutIdleFunc(self.drawRectangle)
        
        

        #callbak om kayboard and mouse
        glutSpecialFunc(self.specialKey)
        glutMouseFunc(self.mouseMove)

        if key == 1:
            glutFullScreen()
        self.initUI()
        self.setLight()
        self.loadImage()
        glutMainLoop()

    def loadImage(self):
        image = Image.open(self.fileImage)
        ix = image.size[0]
        iy = image.size[1]
        image = image.convert('RGBX').tobytes()      
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    def setLight(self, amount = 1):
        glEnable(GL_LIGHTING)
        for i in range(amount):
            lightPosition = (random(), random(), random(), 0.0)
            lightSetting = (0.5, 0.5, 0.5, 1.0)
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glEnable(GL_LIGHT0)
            glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
            glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lightSetting)

        glEnable(GL_DEPTH_TEST)



    def initUI(self):
        self.xRot = 0.0
        self.yRot = 0.0
        self.zRot = 0.0
        self.color = (1, 1, 1, 0.5)
        self.bgColor = (0.0,0.0,0.0,0.0) #black
        self.light = (1.0, 1.0, 1.0, 1.0)
        self.lightPos = (1.0, 1.0, 1.0)

        glClearColor(self.bgColor[0], self.bgColor[1], self.bgColor[2], self.bgColor[3])
        
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

        glShadeModel(GL_SMOOTH)   #rm shde
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()    #load curent matrix

        gluPerspective(10.0, float(self.sizeX)/float(self.sizeY), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    def mouseMove(self,left, right, x, y):
        if left == 0:
            if x >= 0.5 * self.sizeX:
                self.xRot += 5
            if x < 0.5 * self.sizeX:
                self.xRot -= 5
        if right == 0:
            if y >= 0.5 * self.sizeY:
                self.yRot += 5
            if y < 0.5 * self.sizeY:
                self.yRot -= 5

    def specialKey(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.zRot = self.zRot + 5
        if key == GLUT_KEY_DOWN:
            self.zRot = self.zRot - 5
        if key == GLUT_KEY_LEFT:
            self.yRot  = self.yRot + 7
        if key == GLUT_KEY_RIGHT:
            self.xRot  = self.xRot - 7
        if key == GLUT_KEY_F1:
            sys.exit()
    def drawRectangle(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.initUI()
        #glPushMatrix()
        glLoadIdentity()
        glTranslatef(0.0,0.0,-10.0)
        glRotatef(self.xRot,1,0,0)
        glRotatef(self.yRot,0,1,0)
        glRotatef(self.zRot,0,0,1)

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

        self.xRot = self.xRot + 0.25
        self.yRot = self.yRot + 0.25

        glutSwapBuffers()

def main():
    global RECTANGLE
    shape = RECTANGLE
    fileImage = "image.jpeg"
    if len(sys.argv) == 7:
        shape = int(sys.argv[1])
        fileImage = str(sys.argv[2])
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        name = str(sys.argv[5])
        key = int(sys.argv[6])
        rectangle = Shape(shape,fileImage, x, y, name, key)
    else:
        rectangle = Shape()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print(ex)