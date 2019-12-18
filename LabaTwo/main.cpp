#include<GL/glut.h>

void resize(int width, int height)
{
	glViewport(0, 0, width, height); // Window
	glMatrixMode(GL_PROJECTION);//set maatrix
	glLoadIdentity();//текущая матрица будет сделана единичной
	glOrtho(-20, 20, -20, 20, 1, 17);//Указывает размеры плоскости
	gluLookAt(0, 0, 8, 0, 0, 0, 0, 2, 0);//1-3 => wuwer, 4-6 => scene, 7-9 => acceleration vector
	glMatrixMode(GL_MODELVIEW);//все последующие изменения будут применяться к объектно-видовой матрице.
}

void init()
{
	GLfloat light_position[] = { 1.0, 1.0, 1.0, 0.0 };// Расположение источника
	GLfloat lmodel_ambient[] = { 0.5, 0.5, 0.5, 1.0 };// Параметры фонового освещения
	glClearColor(0.0, 0.0, 0.0, 1.0);//задает значения очистки цветом буфера цвета
	glShadeModel(GL_SMOOTH);//Отключение сглаживания
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_DEPTH_TEST);
	glLightfv(GL_LIGHT0, GL_POSITION, light_position);
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient);
}

GLfloat xRot = 25;
GLfloat yRot = 25;
GLfloat zRot = 25;

void display()
{
	GLfloat mat_emission[] = { 0.8, 0.0, 0.2, 0.0 };// Красноватое излучение
	GLfloat no_mat[] = { 0.0, 0.0, 0.0, 1.0 };
	GLfloat mat_diffuse[] = { 0.1, 0.5, 0.8, 1.0 };
	GLfloat mat_specular[] = { 1.0, 1.0, 1.0, 1.0 };// Цвет блика белый
	GLfloat no_shininess[] = { 0.0 }; // Размер блика (обратная пропорция)
	GLfloat low_shininess[] = { 5.0 }; // Размер блика (большая площадь)
	GLfloat high_shininess[] = { 100.0 }; // Размер блика (маленькая площадь - большой фокус)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);// Сбрасываем буфер цвета и буфер глубины
	init();

///////////////////////////////////////////////////////////////////////////////////////////////
	xRot += 2.0;
	yRot += 2.0;
	zRot += 2.0;
/////////////////////////////////////////////////////////////////////////////////////////// Рисуем правую верхнюю сферу
	glPushMatrix();// Сохранить матрицу преобразования модели
	glTranslatef(6.75, 6.75, 0.0);
	glRotatef(xRot, 1.0 , 0.0 , 0.0 );
	glRotatef(yRot, 0.0 , 1.0 , 0.0 );
	glRotatef(zRot, 0.0 , 0.0 , 1.0 );
	glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);//определяют рассеянный цвет материала (цвет материала в тени)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);//цвет диффузного отражения материала
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);//цвет зеркального отражения материала
	glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess);// определяет степень зеркального отражения материала
	glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);//пределяют интенсивность излучаемого света материала
	glutSolidSphere(4.75, 16, 16);//
	glPopMatrix();// Восстановить матрицу преобразования модели
	// Рисуем левую нижнюю сферу
	glPushMatrix();// Сохранить матрицу преобразования модели
	glTranslatef(-6.75, -6.75, 0.0);
	glRotatef(xRot, 1.0 , 0.0 , 0.0 );
	glRotatef(yRot, 0.0 , 1.0 , 0.0 )
	glRotatef(zRot, 0.0 , 0.0 , 1.0 );
	glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);
	glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
	//glutSolidCube(5);
	glutSolidSphere(4.75, 16, 16);
	glPopMatrix();// Восстановить матрицу преобразования модели
///////////////////////////////////////////////////////////////////////////////////////////////////////// Рисуем правый нижний куб (Доминант диффуз)
	glPushMatrix();// Сохранить матрицу преобразования модели
	glTranslatef(6.75, -6.75, 0.0);
	glRotatef(xRot, 1.0 , 0.0 , 0.0 );
	glRotatef(yRot, 0.0 , 1.0 , 0.0 );
	glRotatef(zRot, 0.0 , 0.0 , 1.0 );
	glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat);
	glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission);
	//glutSolidSphere(4.75, 16, 16); // Диаметр, число параллелей и меридиан
	glutSolidCube(5);
	glPopMatrix();// Восстановить матрицу преобразования модели
	glutSwapBuffers();// Переключить буфер
	//glFlush();

}

int main(int argc, char **argv)

{

	glutInit(&argc, argv);//Для инициализации GLUT

	glutInitWindowSize(480, 480);//Размер окна

	glutInitWindowPosition(20, 80);//положение появления окна

	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

	glutCreateWindow("2 лаба OpenGl");//Имя окна

	glutDisplayFunc(display);//Вызов функции которая будет рисовать

	glutReshapeFunc(resize);//Вызов функции отвечающий за изменение размеров окна

	glutMainLoop();// перейти в главный цикл GLUT(обеспечивает взаимосвязь между операционной системой и теми функциями, которые отвечают за окно, получают информацию от устройств ввода/вывода

return 0;

}
