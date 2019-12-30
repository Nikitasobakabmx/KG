void SetLightWorld();
void ChangeSizeWorld(int width, int height);
void SpecialKeysWorld(int key);
void RenderSceneWorld(void);
void DrawInhabitants(GLint nShadow);
void DrawGround(void);

typedef GLfloat GLTVector3[3];
typedef GLfloat GLTVector4[4];
typedef GLfloat GLTMatrix[16];
void gltMakeShadowMatrix(GLTVector3 vPoints[3], GLTVector4 vLightPos, GLTMatrix destMat);
void gltGetPlaneEquation(GLTVector3 vPoint1, GLTVector3 vPoint2, GLTVector3 vPoint3, GLTVector3 vPlane);
void gltGetNormalVector(const GLTVector3 vP1, const GLTVector3 vP2, const GLTVector3 vP3, GLTVector3 vNormal);
void gltSubtractVectors(const GLTVector3 vFirst, const GLTVector3 vSecond, GLTVector3 vResult);
void gltVectorCrossProduct(const GLTVector3 vU, const GLTVector3 vV, GLTVector3 vResult);
void gltNormalizeVector(GLTVector3 vNormal);
GLfloat gltGetVectorLength(const GLTVector3 vVector);
GLfloat gltGetVectorLengthSqrd(const GLTVector3 vVector);
void gltScaleVector(GLTVector3 vVector, const GLfloat fScale);

typedef struct {
	GLTVector3 vLocation;
	GLTVector3 vUp;
	GLTVector3 vForward;
} GLTFrame;

GLTFrame frameCamera;

GLfloat fLightPos[4] = { -100.0f, 100.0f, 50.0f, 1.0f };
GLfloat fNoLight[] = { 0.0f, 0.0f, 0.0f, 0.0f };
GLfloat fLowLight[] = { 0.25f, 0.25f, 0.25f, 1.0f };
GLfloat fBrightLight[] = { 1.0f, 1.0f, 1.0f, 1.0f };

GLTMatrix mShadowMatrix;

void gltApplyActorTransform(GLTFrame* pFrame);
void gltApplyCameraTransform(GLTFrame* pCamera);
void gltInitFrame(GLTFrame* pFrame);
void gltMoveFrameForward(GLTFrame* pFrame, GLfloat fStep);
void gltRotateFrameLocalY(GLTFrame* pFrame, GLfloat fAngle);
#define GLT_PI_DIV_180 0.017453292519943296
#define gltDegToRad(x)  ((x)*GLT_PI_DIV_180)
void gltGetMatrixFromFrame(GLTFrame* pFrame, GLTMatrix mMatrix);
void gltRotateVector(const GLTVector3 vSrcVector, const GLTMatrix mMatrix, GLTVector3 vOut);
void gltRotationMatrix(float angle, float x, float y, float z, GLTMatrix mMatrix);
void gltLoadIdentityMatrix(GLTMatrix m);

void SetLightWorld()
{
	int iSphere;

	//����� ��������� ���������� ����
	GLTVector3 vPoints[3] = 
				{{ 0.0f, -0.4f, 0.0f },
				{ 20.0f, -0.4f, 0.0f },
				{ 5.0f, -0.4f, -5.0f }};

	//��������� ���������� �����
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, fNoLight);
	glLightfv(GL_LIGHT0, GL_AMBIENT, fLowLight);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, fBrightLight);
	glLightfv(GL_LIGHT0, GL_SPECULAR, fBrightLight);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);

	//��������� ������� ����
	gltMakeShadowMatrix(vPoints, fLightPos, mShadowMatrix);

	//������ ������������ ������ ���������
	glEnable(GL_COLOR_MATERIAL);
	glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);
	glMateriali(GL_FRONT, GL_SHININESS, 128);

	gltInitFrame(&frameCamera);  //�������������� ������
}

void DrawGround(void)
{
	GLfloat fExtent = 20.0f;
	GLfloat fStep = 1.0f;
	GLfloat y = -0.4f;
	GLint iStrip, iRun;

	for (iStrip = -fExtent; iStrip <= fExtent; iStrip += fStep)
	{
		glBegin(GL_TRIANGLE_STRIP);
		glNormal3f(0.0f, 1.0f, 0.0f);   //������� ��� ���� ������
		for (iRun = fExtent; iRun >= -fExtent; iRun -= fStep)
		{
			glVertex3f(iStrip, y, iRun);
			glVertex3f(iStrip + fStep, y, iRun);
		}
		glEnd();
	}
}

void DrawInhabitants(GLint nShadow)
{
	static GLfloat yRot = 0.0f;
	GLint i;

	if (nShadow == 0) yRot += 0.5f;
	else glColor3f(0.0f, 0.0f, 0.0f);

	if (nShadow == 0) glColor3f(1.0f, 1.0f, 1.0f);

	glPushMatrix();
	glTranslatef(0.0f, 0.1f, -2.5f);

	if (nShadow == 0)
		glColor3f(0.0f, 0.0f, 0.0f);

	glPushMatrix();
	glRotatef(-yRot/2.0f, 0.0f, 1.0f, 0.0f);
	glTranslatef(1.0f, 0.0f, 0.0f);
	glutSolidTeapot(0.1);
	glPopMatrix();

	if (nShadow == 0)
	{
		glColor3f(1.0f, 1.0f, 1.0f); 
		glMaterialfv(GL_FRONT, GL_SPECULAR, fBrightLight);
	}

	glRotatef(yRot/2.0f, 0.0f, 1.0f, 0.0f);
	//glutSolidTorus(0.15, 0.35, 37, 61);
	glutSolidTeapot(0.5f);
	glMaterialfv(GL_FRONT, GL_SPECULAR, fNoLight);
	glPopMatrix();
}

void RenderSceneWorld(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glPushMatrix();
	gltApplyCameraTransform(&frameCamera);

	glLightfv(GL_LIGHT0, GL_POSITION, fLightPos);

	//������ ���������
	glColor3f(1.0f, 1.0f, 1.0f);
	DrawGround();

	//������� ������ ���� �������� (��� ����������� ������� � ���������)
	glDisable(GL_DEPTH_TEST);
	glDisable(GL_LIGHTING);
	glPushMatrix();
	glMultMatrixf(mShadowMatrix);
	DrawInhabitants(1);
	glPopMatrix();
	//�������� �������� ������� � ���������
	glEnable(GL_LIGHTING);
	glEnable(GL_DEPTH_TEST);

	//������ ������ ���� �������
	DrawInhabitants(0);

	glPopMatrix();

	//����������� ����� � ��������� �����
	glutSwapBuffers();
	glutPostRedisplay();
}

void SpecialKeysWorld(int key)
{
	if (key == GLUT_KEY_UP) gltMoveFrameForward(&frameCamera, 0.1f);
	if (key == GLUT_KEY_DOWN) gltMoveFrameForward(&frameCamera, -0.1f);
	if (key == GLUT_KEY_LEFT) gltRotateFrameLocalY(&frameCamera, 0.1);
	if (key == GLUT_KEY_RIGHT) gltRotateFrameLocalY(&frameCamera, -0.1);
}

void ChangeSizeWorld(int width, int height)
{
	SetLightWorld(); //������������� �������������� ��������� ��������� � ���������

	glEnable(GL_DEPTH_TEST);  //�������� ���� �������
	glEnable(GL_CULL_FACE);    //���������� ������ ������� �������
	glFrontFace(GL_CCW);    //������� ������� ����� ������ ������� �������
	glCullFace(GL_BACK);

	glClearColor(fLowLight[0], fLowLight[1], fLowLight[2], fLowLight[3]);

	if (height == 0) height = 1;
	glViewport(0, 0, width, height);

	//������������� ������� �������������� � ����� �������������
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	//������������� ������� ����������� ������ ����������� 
	GLfloat aspectRatio = (GLfloat)width / (GLfloat)height;  //��� ���������� ���������
	gluPerspective(35.0f, aspectRatio, 1.0f, 50.0f);    //���������� �����������

  //��������������� ������� �������������� � �������� ����� ����
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}


////////////////////////////////////////////////////////////////////
//Apply an actors transform given it's frame of reference
void gltApplyActorTransform(GLTFrame* pFrame)
{
	GLTMatrix mTransform;
	gltGetMatrixFromFrame(pFrame, mTransform);
	glMultMatrixf(mTransform);
}

//////////////////////////////////////////////////////////////////
//Apply a camera transform given a frame of reference. This is
//pretty much just an alternate implementation of gluLookAt using
//floats instead of doubles and having the forward vector specified
//instead of a point out in front of me. 
void gltApplyCameraTransform(GLTFrame* pCamera)
{
	GLTMatrix mMatrix;
	GLTVector3 vAxisX;
	GLTVector3 zFlipped;

	zFlipped[0] = -pCamera->vForward[0];
	zFlipped[1] = -pCamera->vForward[1];
	zFlipped[2] = -pCamera->vForward[2];

	//Derive X vector
	gltVectorCrossProduct(pCamera->vUp, zFlipped, vAxisX);

	//Populate matrix, note this is just the rotation and is transposed
	mMatrix[0] = vAxisX[0];
	mMatrix[4] = vAxisX[1];
	mMatrix[8] = vAxisX[2];
	mMatrix[12] = 0.0f;

	mMatrix[1] = pCamera->vUp[0];
	mMatrix[5] = pCamera->vUp[1];
	mMatrix[9] = pCamera->vUp[2];
	mMatrix[13] = 0.0f;

	mMatrix[2] = zFlipped[0];
	mMatrix[6] = zFlipped[1];
	mMatrix[10] = zFlipped[2];
	mMatrix[14] = 0.0f;

	mMatrix[3] = 0.0f;
	mMatrix[7] = 0.0f;
	mMatrix[11] = 0.0f;
	mMatrix[15] = 1.0f;

	//Do the rotation first
	glMultMatrixf(mMatrix);

	//Now, translate backwards
	glTranslatef(-pCamera->vLocation[0], -pCamera->vLocation[1], -pCamera->vLocation[2]);
}

#define GLT_PI  3.14159265358979323846

//Initialize a frame of reference. 
//Uses default OpenGL viewing position and orientation
void gltInitFrame(GLTFrame* pFrame)
{
	pFrame->vLocation[0] = 0.0f;
	pFrame->vLocation[1] = 0.0f;
	pFrame->vLocation[2] = 0.0f;

	pFrame->vUp[0] = 0.0f;
	pFrame->vUp[1] = 1.0f;
	pFrame->vUp[2] = 0.0f;

	pFrame->vForward[0] = 0.0f;
	pFrame->vForward[1] = 0.0f;
	pFrame->vForward[2] = -1.0f;
}

/////////////////////////////////////////////////////////
//March a frame of reference forward. This simply moves
//the location forward along the forward vector.
void gltMoveFrameForward(GLTFrame* pFrame, GLfloat fStep)
{
	pFrame->vLocation[0] += pFrame->vForward[0] * fStep;
	pFrame->vLocation[1] += pFrame->vForward[1] * fStep;
	pFrame->vLocation[2] += pFrame->vForward[2] * fStep;
}

/////////////////////////////////////////////////////////
//Rotate a frame around it's local Y axis
void gltRotateFrameLocalY(GLTFrame* pFrame, GLfloat fAngle)
{
	GLTMatrix mRotation;
	GLTVector3 vNewForward;

	gltRotationMatrix((float)gltDegToRad(fAngle), 0.0f, 1.0f, 0.0f, mRotation);
	gltRotationMatrix(fAngle, pFrame->vUp[0], pFrame->vUp[1], pFrame->vUp[2], mRotation);

	gltRotateVector(pFrame->vForward, mRotation, vNewForward);
	memcpy(pFrame->vForward, vNewForward, sizeof(GLTVector3));
}

///////////////////////////////////////////////////////////////////
//Derives a 4x4 transformation matrix from a frame of reference
void gltGetMatrixFromFrame(GLTFrame* pFrame, GLTMatrix mMatrix)
{
	GLTVector3 vXAxis;       //Derived X Axis

	//Calculate X Axis
	gltVectorCrossProduct(pFrame->vUp, pFrame->vForward, vXAxis);

	//Just populate the matrix
	//X column vector
	memcpy(mMatrix, vXAxis, sizeof(GLTVector3));
	mMatrix[3] = 0.0f;

	//y column vector
	memcpy(mMatrix + 4, pFrame->vUp, sizeof(GLTVector3));
	mMatrix[7] = 0.0f;

	//z column vector
	memcpy(mMatrix + 8, pFrame->vForward, sizeof(GLTVector3));
	mMatrix[11] = 0.0f;

	//Translation/Location vector
	memcpy(mMatrix + 12, pFrame->vLocation, sizeof(GLTVector3));
	mMatrix[15] = 1.0f;
}

//Rotates a vector using a 4x4 matrix. Translation column is ignored
void gltRotateVector(const GLTVector3 vSrcVector, const GLTMatrix mMatrix, GLTVector3 vOut)
{
	vOut[0] = mMatrix[0] * vSrcVector[0] + mMatrix[4] * vSrcVector[1] + mMatrix[8] * vSrcVector[2];
	vOut[1] = mMatrix[1] * vSrcVector[0] + mMatrix[5] * vSrcVector[1] + mMatrix[9] * vSrcVector[2];
	vOut[2] = mMatrix[2] * vSrcVector[0] + mMatrix[6] * vSrcVector[1] + mMatrix[10] * vSrcVector[2];
}

///////////////////////////////////////////////////////////////////////////////
//Creates a 4x4 rotation matrix, takes radians NOT degrees
void gltRotationMatrix(float angle, float x, float y, float z, GLTMatrix mMatrix)
{
	float vecLength, sinSave, cosSave, oneMinusCos;
	float xx, yy, zz, xy, yz, zx, xs, ys, zs;

	//If NULL vector passed in, this will blow up...
	if (x == 0.0f && y == 0.0f && z == 0.0f)
	{
		gltLoadIdentityMatrix(mMatrix);
		return;
	}

	//Scale vector
	vecLength = (float)sqrt(x * x + y * y + z * z);

	//Rotation matrix is normalized
	x /= vecLength;
	y /= vecLength;
	z /= vecLength;

	sinSave = (float)sin(angle);
	cosSave = (float)cos(angle);
	oneMinusCos = 1.0f - cosSave;

	xx = x * x;
	yy = y * y;
	zz = z * z;
	xy = x * y;
	yz = y * z;
	zx = z * x;
	xs = x * sinSave;
	ys = y * sinSave;
	zs = z * sinSave;

	mMatrix[0] = (oneMinusCos * xx) + cosSave;
	mMatrix[4] = (oneMinusCos * xy) - zs;
	mMatrix[8] = (oneMinusCos * zx) + ys;
	mMatrix[12] = 0.0f;

	mMatrix[1] = (oneMinusCos * xy) + zs;
	mMatrix[5] = (oneMinusCos * yy) + cosSave;
	mMatrix[9] = (oneMinusCos * yz) - xs;
	mMatrix[13] = 0.0f;

	mMatrix[2] = (oneMinusCos * zx) - ys;
	mMatrix[6] = (oneMinusCos * yz) + xs;
	mMatrix[10] = (oneMinusCos * zz) + cosSave;
	mMatrix[14] = 0.0f;

	mMatrix[3] = 0.0f;
	mMatrix[7] = 0.0f;
	mMatrix[11] = 0.0f;
	mMatrix[15] = 1.0f;
}

///////////////////////////////////////////////////////////////////////////////
//Load a matrix with the Idenity matrix
void gltLoadIdentityMatrix(GLTMatrix m)
{
	static GLTMatrix identity = { 1.0f, 0.0f, 0.0f, 0.0f,
					0.0f, 1.0f, 0.0f, 0.0f,
					0.0f, 0.0f, 1.0f, 0.0f,
					0.0f, 0.0f, 0.0f, 1.0f };

	memcpy(m, identity, sizeof(GLTMatrix));
}

//��������� ������� �������������� ����.
//�������� ����������� �������� ���������� ���� �����
//�� ��������� (�� ������� �� ����� ������) 
//� ������������� ������ ��������� ��������� �����
//������������ �������� ��������� � destMat
void gltMakeShadowMatrix(GLTVector3 vPoints[3], GLTVector4 vLightPos, GLTMatrix destMat)
{
	GLTVector4 vPlaneEquation;
	GLfloat dot;

	gltGetPlaneEquation(vPoints[0], vPoints[1], vPoints[2], vPlaneEquation);

	//��������� ��������� ������������ ������������� ������� ���������
	//� ������� ��������� ��������� �����
	dot = vPlaneEquation[0] * vLightPos[0] +
		vPlaneEquation[1] * vLightPos[1] +
		vPlaneEquation[2] * vLightPos[2] +
		vPlaneEquation[3] * vLightPos[3];

	//��������� ������� ��������
	//������ �������
	destMat[0] = dot - vLightPos[0] * vPlaneEquation[0];
	destMat[4] = 0.0f - vLightPos[0] * vPlaneEquation[1];
	destMat[8] = 0.0f - vLightPos[0] * vPlaneEquation[2];
	destMat[12] = 0.0f - vLightPos[0] * vPlaneEquation[3];

	//������ �������
	destMat[1] = 0.0f - vLightPos[1] * vPlaneEquation[0];
	destMat[5] = dot - vLightPos[1] * vPlaneEquation[1];
	destMat[9] = 0.0f - vLightPos[1] * vPlaneEquation[2];
	destMat[13] = 0.0f - vLightPos[1] * vPlaneEquation[3];

	//������ �������
	destMat[2] = 0.0f - vLightPos[2] * vPlaneEquation[0];
	destMat[6] = 0.0f - vLightPos[2] * vPlaneEquation[1];
	destMat[10] = dot - vLightPos[2] * vPlaneEquation[2];
	destMat[14] = 0.0f - vLightPos[2] * vPlaneEquation[3];

	//��������� �������
	destMat[3] = 0.0f - vLightPos[3] * vPlaneEquation[0];
	destMat[7] = 0.0f - vLightPos[3] * vPlaneEquation[1];
	destMat[11] = 0.0f - vLightPos[3] * vPlaneEquation[2];
	destMat[15] = dot - vLightPos[3] * vPlaneEquation[3];
}

//**********************************************************
//���������� ������������ ��������� ��������� �� ���� ������
void gltGetPlaneEquation(GLTVector3 vPoint1, GLTVector3 vPoint2, GLTVector3 vPoint3, GLTVector3 vPlane)
{
	//��������� ������ �������
	gltGetNormalVector(vPoint1, vPoint2, vPoint3, vPlane);

	vPlane[3] = -(vPlane[0] * vPoint3[0] + vPlane[1] * vPoint3[1] + vPlane[2] * vPoint3[2]);
}

void gltGetNormalVector(const GLTVector3 vP1, const GLTVector3 vP2, const GLTVector3 vP3, GLTVector3 vNormal)
{
	GLTVector3 vV1, vV2;

	gltSubtractVectors(vP2, vP1, vV1);
	gltSubtractVectors(vP3, vP1, vV2);

	gltVectorCrossProduct(vV1, vV2, vNormal);
	gltNormalizeVector(vNormal);
}

void gltSubtractVectors(const GLTVector3 vFirst, const GLTVector3 vSecond, GLTVector3 vResult)
{
	vResult[0] = vFirst[0] - vSecond[0];
	vResult[1] = vFirst[1] - vSecond[1];
	vResult[2] = vFirst[2] - vSecond[2];
}

void gltVectorCrossProduct(const GLTVector3 vU, const GLTVector3 vV, GLTVector3 vResult)
{
	vResult[0] = vU[1] * vV[2] - vV[1] * vU[2];
	vResult[1] = -vU[0] * vV[2] + vV[0] * vU[2];
	vResult[2] = vU[0] * vV[1] - vV[0] * vU[1];
}

void gltNormalizeVector(GLTVector3 vNormal)
{
	GLfloat fLength = 1.0f / gltGetVectorLength(vNormal);
	gltScaleVector(vNormal, fLength);
}

GLfloat gltGetVectorLength(const GLTVector3 vVector)
{
	return (GLfloat)sqrt(gltGetVectorLengthSqrd(vVector));
}

GLfloat gltGetVectorLengthSqrd(const GLTVector3 vVector)
{
	return (vVector[0] * vVector[0]) + (vVector[1] * vVector[1]) + (vVector[2] * vVector[2]);
}

void gltScaleVector(GLTVector3 vVector, const GLfloat fScale)
{
	vVector[0] *= fScale; vVector[1] *= fScale; vVector[2] *= fScale;
}
