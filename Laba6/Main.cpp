#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>  
#include <stdlib.h>
#include <cmath>
#include <cstring>

#include <iostream>

void TimerFunc(int);
void SpecialKeys(int, int, int);
void RenderScene(void);
void ChangeSize(int, int);

GLfloat xRot = 0.0f;
GLfloat yRot = 0.0f;
GLfloat zRot = 0.0f;

#include "World.h" 

void RenderScene(void)
{
	glPushAttrib(GL_LIGHTING_BIT); // ��������� ������� ��������� OpenGL � ����� ���������
	RenderSceneWorld(); 
	glPopAttrib(); // ������������ ������� ��������� OpenGL �� ����� ���������
}

void ChangeSize(int width, int height)
{
	ChangeSizeWorld(width, height);
}

void TimerFunc(int value) // ���������� ������� �������
{
	glutPostRedisplay();
	glutTimerFunc(3, TimerFunc, 1);
}

void SpecialKeys(int key, int x, int y)
{
	SpecialKeysWorld(key);
	glutPostRedisplay();
}

int main(int argc, char* argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(300, 300);
	glutCreateWindow("LabSix");
	glutDisplayFunc(RenderScene);
	glutReshapeFunc(ChangeSize); 
	glutTimerFunc(100, TimerFunc, 1); 
	glutSpecialFunc(SpecialKeys); 

	glutMainLoop();
	return 0;
}