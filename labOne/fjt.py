import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    )
#поверхности 0 1 2 3 4 5 
normals = [
    ( 0,  0, -1),  
    (-1,  0,  0),  
    ( 0,  1,  1),  
    ( 1,  0,  0),  
    ( 0,  1,  0),  
    ( 0, -1,  0)   
]   
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (1,0,1),
    )

def Cube1():
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(surfaces):
        x = 0

        glNormal3fv(normals[i_surface]) #установить вектор нормали вершины поверхности

        for vertex in surface:
            x+=2
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv(colors[2])
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()    

def Cube2():
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(surfaces):
        x = 0

        glNormal3fv(normals[i_surface]) #установить вектор нормали вершины поверхности

        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv(colors[2])
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()    

def main():
    pygame.init()
    display = (600,500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0,0.0, -10)
    glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0)) # directional light from the front
    #glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1)) # point light from the left, top, front
    #glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glEnable(GL_DEPTH_TEST) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glRotatef(1, 3, 1, 2)
        Cube1()
        Cube2()    
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        
        pygame.display.flip()
main()