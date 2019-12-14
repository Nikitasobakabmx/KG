#include<GL/glut.h>
GLfloat mat_ambient[] = { 0.7, 0.7, 0.7, 1.0 };
GLfloat mat_diffuse[] = { 0.8, 0.8, 0.8, 1.0 };
GLfloat mat_specular1[] = { 1.0, 1.0, 1.0, 1.0 };
GLfloat mat_specular2[] = { 0.2, 0.2, 0.2, 1.0 };
GLfloat mat_specular3[] = { 0.5, 0.5, 0.5, 1.0 };
GLfloat no_shininess[] = { 0.0 };
GLfloat low_shininess[] = {15.0 };
GLfloat high_shininess[] = { 100.0 };
GLfloat ligth1[] = { 0.0, 1.0, 0.0, 1.0 };
GLfloat ligth2[] = { 1.0, 0.0, 0.0, 1.0 };
GLfloat ligth3[] = { 0.0, 0.0, 1.0, 1.0 };
GLfloat light_position1[] = { 5.0, 0.0, 0.0, 0.0 };
GLfloat light_position2[] = { -5.0, -4.0, 10.0, 0.0 };
GLfloat light_position3[] = { 4.0, -4.0, 10.0, 0.0 };
float ambient[] = { 1.0f, 1.0f, 1.0f, 1.0f };
float black[] = { 0, 0, 0, 1.0f };
////////////////////////////////////////ДЛЯ МЫШИ
int mouseDown = 0;
float xrot = 100.0f;
float yrot = -100.0f;
float xdiff = 100.0f;
float ydiff = 100.0f;
//////////////////////////////////////////
/////////////////////////////КООРДИНАТЫ ФИГУР
float tra_x = 0.0f;
float tra_y = 0.0f;
float tra_z = 0.0f;
///////////////////////////////////ДЛЯ ФУНКЦИИ РАЗМЕРА
float grow_shrink = 70.0f;
float resize_f = 1.0f;
/////////////////////////////////////////////////
void resize(int w, int h)
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glViewport(0, 0, w, h);
    gluPerspective(grow_shrink, resize_f * w / h, resize_f, 100.f * resize_f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void Sph() {
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular1);
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, high_shininess);
    glTranslatef(tra_x - 1, tra_y, tra_z);
    //glTranslatef(tra_x, tra_y, tra_z);
    //glColor4f(0.0f, 0.0f, 1.0f, 0.2f);
    glColor4f(0.0f, 0.0f, 0.0f, 1.0f);
    glutSolidSphere(.3f, 400, 40);
};

void Cube() {
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular2);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess);
    glPushMatrix();
    glTranslatef(tra_x + 1, tra_y, tra_z);
    glColor4f(0.0f, 0.0f, 0.0f, 1.0f);
    glutSolidCube(1);
    glPopMatrix();
};

void tetr() {
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular3);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess);
    glPushMatrix();
    glTranslatef(tra_x, tra_y, tra_z);
    //glTranslatef(tra_x - 1, tra_y, tra_z);
    glBegin(GL_TRIANGLES);
    glColor4f(0.0f, 0.0f, 0.0f, 1.0f);
    //glColor3f(1.0f, 1.0f, 1.0f);
    glNormal3f(0, 0, -1);
    glVertex3f(0.5f, -0.5f, 0.0f);
    glVertex3f(0.0f, 0.5f, 0.0f);
    glVertex3f(-0.5f, -0.5f, 0.0f);
    glNormal3f(0.5, 0.25, 0.25);
    glVertex3f(0.5f, -0.5f, 0.0f);
    glVertex3f(0.0f, 0.5f, 0.0f);
    glVertex3f(0.0f, 0.0f, 0.5f);
    glNormal3f(-0.5, 0.25, 0.25);
    glVertex3f(0.0f, 0.5f, 0.0f);
    glVertex3f(-0.5f, -0.5f, 0.0f);
    glVertex3f(0.0f, 0.0f, 0.5f);
    glNormal3f(0, -0.5, 0.5);
    glVertex3f(-0.5f, -0.5f, 0.0f);
    glVertex3f(0.5f, -0.5f, 0.0f);
    glVertex3f(0.0f, 0.0f, 0.5f);
    glEnd();
    glPopMatrix();
};

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(
        0.0f, 0.0f, 4.0f,
        0.0f, 0.0f, 0.0f,
        0.0f, 1.0f, 0.0f);
    glRotatef(xrot, 1.0f, 0.0f, 0.0f);
    glRotatef(yrot, 0.0f, 1.0f, 0.0f);
    Cube();
    tetr();
    Sph();
    glFlush();
    glutSwapBuffers();
}

void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        mouseDown = 1;
        xdiff = x - yrot;
        ydiff = -y + xrot;
    }
    else
        mouseDown = 0;
}

void mouseMotion(int x, int y)
{
    if (mouseDown)
    {
        yrot = x - xdiff;
        xrot = y + ydiff;
        glutPostRedisplay();
    }
}

int main(int argc, char* argv[])
{
    glutInit(&argc, argv);
    glutInitWindowPosition(50, 50);
    glutInitWindowSize(500, 500);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    glutCreateWindow(" лаба 3");
    glutDisplayFunc(display);
    glutMouseFunc(mouse);//ЗАХВАТ МЫШИ
    glutMotionFunc(mouseMotion);
    glutReshapeFunc(resize);//размер
////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////// свет //////////////////////////////////////////////////////////
    glEnable(GL_LIGHTING);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, black);
    //glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHT1);
    glEnable(GL_LIGHT2);
    glEnable(GL_DEPTH_TEST);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, ligth1);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position1);
    glLightfv(GL_LIGHT1, GL_POSITION, light_position2);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, ligth2);
    glLightfv(GL_LIGHT2, GL_POSITION, light_position3);
    glLightfv(GL_LIGHT2, GL_DIFFUSE, ligth3);
    glShadeModel(GL_SMOOTH);//сглаживание
    //glEnable(GL_COLOR_MATERIAL);
    //glColorMaterial(GL_FRONT, GL_AMBIENT);
    //glEnable(GL_BLEND);
    glutMainLoop();
    return 0;
}