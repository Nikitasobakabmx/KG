#include<GL/glut.h>
////////////////////////////////////материя
GLfloat mat_ambient[] = { 0.7, 0.7, 0.7, 1.0 };
GLfloat mat_diffuse[] = { 0.8, 0.8, 0.8, 1.0 };
GLfloat mat_specular1[] = { 1.0, 1.0, 1.0, 1.0 };
GLfloat mat_specular2[] = { 0.2, 0.2, 0.2, 1.0 };
GLfloat mat_specular3[] = { 0.5, 0.5, 0.5, 1.0 };
GLfloat no_shininess[] = { 0.0 };
GLfloat low_shininess[] = { 5.0 };
GLfloat high_shininess[] = { 100.0 };
GLfloat ligth1[] = { 0.0, 1.0, 0.0, 1.0 };
GLfloat ligth2[] = { 1.0, 0.0, 0.0, 1.0 };
GLfloat ligth3[] = { 0.0, 0.0, 1.0, 1.0 };
float ambient[] = { 1.0f, 1.0f, 1.0f, 1.0f };
float tra_x = 0.0f;
float tra_y = 0.0f;
float tra_z = 0.0f;
int spin = 0;
int LOL = 0;
void resize(int w, int h)
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    float grow_shrink = 70.0f;
    float resize_f = 1.0f;
    glViewport(0, 0, w, h);
    gluPerspective(grow_shrink, resize_f * w / h, resize_f, 100.f * resize_f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void CUBE() {
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular2);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess);
    glPushMatrix();
    glTranslatef(tra_x + 1, tra_y, tra_z);
    glColor4f(0.0f, 0.0f, 0.0f, 0.3);//альфа за прозрачность
    glutSolidCube(2);
    glPopMatrix();
};

void TOR() {
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular3);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess);
    glPushMatrix();
    glTranslatef(tra_x, tra_y, tra_z);
    glColor4f(0.0f, 0.0f, 0.0f, 1);
    glutSolidTorus(0.15, 1, 40, 40);
    glPopMatrix();
};

void init(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glShadeModel(GL_SMOOTH);
    glEnable(GL_LIGHTING);
    glEnable(GL_DEPTH_TEST);
}

void shine()
{
/////////////////////////////////////////позиции света
    GLfloat light_position2[] = { 10.0, 10.0, 10.0, 0.0 };
    GLfloat light_position3[] = { 20, 20.0, 20.0, 0.0 };
    GLfloat light_position1[] = { -10.0, -10.0,10.0, 0.0 };
    glPushMatrix();
    glTranslatef(0.0, 0.0, -5.0);
    glPushMatrix();
    glLightfv(GL_LIGHT0, GL_SPECULAR, ligth2);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, ligth3);
    glLightfv(GL_LIGHT2, GL_DIFFUSE, ligth1);
    switch (LOL)
    {
        case 1:
        //красный зеркал
            glEnable(GL_LIGHT0);
            glDisable(GL_LIGHT1);
            glDisable(GL_LIGHT2);
            glRotated((GLdouble)spin, 1.0, 0.0, 0.0);
            glLightfv(GL_LIGHT0, GL_POSITION, light_position1);
            break;
        case 2:
        //синий диф
            glEnable(GL_LIGHT1);
            glDisable(GL_LIGHT0);
            glDisable(GL_LIGHT2);
            glRotated((GLdouble)spin, 1.0, 0.0, 0.0);
            glLightfv(GL_LIGHT1, GL_POSITION, light_position2);
            break;
        case 3:
        //зеленый диф
            glEnable(GL_LIGHT2);
            glDisable(GL_LIGHT0);
            glDisable(GL_LIGHT1);
            glRotated((GLdouble)spin, 1.0, 0.0, 0.0);
            glLightfv(GL_LIGHT2, GL_POSITION, light_position2);
            break;
        case 4:
        //синий по орбите

glEnable(GL_LIGHT1);

glDisable(GL_LIGHT0);

glDisable(GL_LIGHT2);

glRotated((GLdouble)spin, 0.0, 1.0, 0.0);

glLightfv(GL_LIGHT1, GL_POSITION, light_position1);

break;

case 5:

//синий и зеленый

glEnable(GL_LIGHT1);

glEnable(GL_LIGHT2);

glDisable(GL_LIGHT0);

glRotated((GLdouble)spin, 1.0, 0.0, 0.0);

glLightfv(GL_LIGHT2, GL_POSITION, light_position1);

//glRotated((GLdouble)spin, 0.0, 1.0, 0.0);

glLightfv(GL_LIGHT1, GL_POSITION, light_position1);

break;

case 6:

//розовый и синий

glEnable(GL_LIGHT0);

glEnable(GL_LIGHT2);

glDisable(GL_LIGHT1);

glRotated((GLdouble)spin, 1.0, 0.0, 0.0);

glLightfv(GL_LIGHT2, GL_POSITION, light_position1);

//glRotated((GLdouble)spin, 0.0, 1.0, 0.0);

glLightfv(GL_LIGHT0, GL_POSITION, light_position1);

break;

case 7:

//красный и зеленый

glEnable(GL_LIGHT0);

glEnable(GL_LIGHT1);

glDisable(GL_LIGHT1);

glRotated((GLdouble)spin, 1.0, 0.0, 0.0);

glLightfv(GL_LIGHT1, GL_POSITION, light_position1);

glRotated((GLdouble)spin, 0.0, 1.0, 0.0);

glLightfv(GL_LIGHT0, GL_POSITION, light_position1);

break;

case 8:

//розовый и синий

glEnable(GL_LIGHT1);

glEnable(GL_LIGHT2);

glDisable(GL_LIGHT0);

glRotated((GLdouble)spin, 0.0, 1.0, 0.0);

glLightfv(GL_LIGHT2, GL_POSITION, light_position2);

glLightfv(GL_LIGHT1, GL_POSITION, light_position2);

break;

case 9:

glDisable(GL_LIGHT0);

glDisable(GL_LIGHT1);

glDisable(GL_LIGHT2);

break;

case 10:

glEnable(GL_LIGHT0);

glEnable(GL_LIGHT1);

glEnable(GL_LIGHT2);

glLightfv(GL_LIGHT0, GL_POSITION, light_position3);

glLightfv(GL_LIGHT1, GL_POSITION, light_position3);

glLightfv(GL_LIGHT2, GL_POSITION, light_position3);

break;

}

glTranslated(0.0, 0.0, 1.5);

glDisable(GL_LIGHTING);

glEnable(GL_LIGHTING);

glColor3f(0.0, 1.0, 1.0);

glutWireCube(0.1);

glPopMatrix();

}

void processSpecialKeys(int key, int x, int y) {

switch (key) {

case GLUT_KEY_F1:

LOL = 1;

break;

case GLUT_KEY_F2:

LOL = 2;

break;

case GLUT_KEY_F3:

LOL = 3;

break;

case GLUT_KEY_F4:

LOL = 4;

break;

case GLUT_KEY_F5:

LOL = 5;

break;

case GLUT_KEY_F6:

LOL = 6;

break;

case GLUT_KEY_F7:

LOL = 7;

break;

case GLUT_KEY_F8:

LOL = 8;

break;

case GLUT_KEY_F9:

LOL = 9;

break;

case GLUT_KEY_F10:

LOL = 10;

break;

}

}

void display(void)

{

glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

glLoadIdentity();

glEnable(GL_BLEND);

//glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

gluLookAt(

0.0, -0.5, 6.0,

0.0, 0.0, 0.0,

0.0, 1.0, 0.0);

glRotatef(12, 0, 0.0f, 0.0f);

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);//прозрачность

glBlendFunc(GL_ONE, GL_ONE);

TOR();

CUBE();

shine();

glFlush();

glutSwapBuffers();

}

void light_moving(void)

{

spin = (spin + 1) % 360;

glutPostRedisplay();//снова вызывает функцию дисплей

}

void mouse(int button, int state, int x, int y)

{

switch (button)

{

case GLUT_LEFT_BUTTON:

if (state == GLUT_DOWN)

glutIdleFunc(light_moving);

else

glutIdleFunc(NULL);

break;

}

}

int main(int argc, char* argv[])

{

glutInit(&argc, argv);

glutInitWindowPosition(50, 50);

glutInitWindowSize(500, 500);

glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);

glutCreateWindow("4 лаба");

init();

glutDisplayFunc(display);

glutMouseFunc(mouse);

glutSpecialFunc(processSpecialKeys);

glutReshapeFunc(resize);//размер

glutMainLoop();

return 0;

}