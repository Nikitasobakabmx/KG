#include<GL/glut.h>

void display(void)

{

	glClear(GL_COLOR_BUFFER_BIT);//Очистка буфера цвета

	glRotatef(25, 1, 1, 0);//ПОВОРОТ В ПРОСТРАНСТВЕ НА 25 ГРАДУСОВ

	glBegin(GL_LINE_STRIP);//Для задания примитива используется конструкция glBegin (тип_примитива)…glEnd ().

	//GL_LINE_STRIP-каждая пара вершин задает линию (т.е. конец предыдущей линии является началом следующей)

	glVertex3f(-50, -50, -50);//Вершины задаются glVertex*.

	glVertex3f(50, -50, -50);

	glVertex3f(50, 50, -50);

	glVertex3f(-50, 50, -50);

	glVertex3f(-50, -50, -50);

	glEnd();

	glBegin(GL_LINE_STRIP);

	glVertex3f(-50, -50, 50);

	glVertex3f(50, -50, 50);

	glVertex3f(50, 50, 50);

	glVertex3f(-50, 50, 50);

	glVertex3f(-50, -50, 50);

	glEnd();

	glBegin(GL_LINES);

	//GL_LINES-каждая пара вершин задает линию (т.е. конец предыдущей линии является началом следующей)

	glVertex3f(-50, -50, 50);

	glVertex3f(-50, -50, -50);

	glVertex3f(50, -50, 50);

	glVertex3f(50, -50, -50);

	glVertex3f(50, 50, 50);

	glVertex3f(50, 50, -50);

	glVertex3f(-50, 50, 50);

	glVertex3f(-50, 50, -50);

	glEnd();

	glutSwapBuffers();//сменить экранные буфера при помощи glutSwapBuffers (),

}

int main(int argc, char **argv)

{

	glutInit(&argc, argv);//Для инициализации GLUT

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);// задания режима дисплея вызывается

	glutInitWindowSize(480, 480);

	glutInitWindowPosition(20, 80);

	glutCreateWindow("1 лаба");

	glClearColor(1,0.5,0,1.0);//оманда glClearColor устанавливает цвет, которым будет заполнен буфер

	glMatrixMode(GL_PROJECTION);//Матрицу проекции

	glLoadIdentity();//заменяет текущую матрицу единичной матрицей

	glOrtho(-100,100,-100,100,-100,100);

	glutDisplayFunc(display);//адает функцию рисования изображения

	glutMainLoop();

	return 0;

}
