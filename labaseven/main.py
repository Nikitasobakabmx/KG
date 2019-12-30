from OpenGL.GL import *
from OpenGL.GLUT import *
#import sys
from random import random
global pointcolor



def specialkeys(key, x, y):
    global pointcolor
    if key == GLUT_KEY_UP:          
        glRotatef(5, 1, 0, 0)       
    if key == GLUT_KEY_DOWN:        
        glRotatef(-5, 1, 0, 0)      
    if key == GLUT_KEY_LEFT:        
        glRotatef(5, 0, 1, 0)       
    if key == GLUT_KEY_RIGHT:       
        glRotatef(-5, 0, 1, 0)      
    if key == GLUT_KEY_END:         
        # Ð—Ð°Ð¿Ð¾Ð»Ð½ÑÐµÐ¼ Ð¼Ð°ÑÑÐ¸Ð² pointcolor ÑÐ»ÑƒÑ‡Ð°Ð¹Ð½Ñ‹Ð¼Ð¸ Ñ‡Ð¸ÑÐ»Ð°Ð¼Ð¸ Ð² Ð´Ð¸Ð°Ð¿Ð°Ð·Ð¾Ð½Ðµ 0-1
        pointcolor = [[random(), random(), random()], [random(), random(), random()], [random(), random(), random()]]


# ÐŸÑ€Ð¾Ñ†ÐµÐ´ÑƒÑ€Ð° Ð¿Ð¾Ð´Ð³Ð¾Ñ‚Ð¾Ð²ÐºÐ¸ ÑˆÐµÐ¹Ð´ÐµÑ€Ð° (Ñ‚Ð¸Ð¿ ÑˆÐµÐ¹Ð´ÐµÑ€Ð°, Ñ‚ÐµÐºÑÑ‚ ÑˆÐµÐ¹Ð´ÐµÑ€Ð°)
def create_shader(shader_type, source):
    # Ð¡Ð¾Ð·Ð´Ð°ÐµÐ¼ Ð¿ÑƒÑÑ‚Ð¾Ð¹ Ð¾Ð±ÑŠÐµÐºÑ‚ ÑˆÐµÐ¹Ð´ÐµÑ€Ð°
    shader = glCreateShader(shader_type)
    # ÐŸÑ€Ð¸Ð²ÑÐ·Ñ‹Ð²Ð°ÐµÐ¼ Ñ‚ÐµÐºÑÑ‚ ÑˆÐµÐ¹Ð´ÐµÑ€Ð° Ðº Ð¿ÑƒÑÑ‚Ð¾Ð¼Ñƒ Ð¾Ð±ÑŠÐµÐºÑ‚Ñƒ ÑˆÐµÐ¹Ð´ÐµÑ€Ð°
    glShaderSource(shader, source)
    # ÐšÐ¾Ð¼Ð¿Ð¸Ð»Ð¸Ñ€ÑƒÐµÐ¼ ÑˆÐµÐ¹Ð´ÐµÑ€
    glCompileShader(shader)
    # Ð’Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÐ¼ ÑÐ¾Ð·Ð´Ð°Ð½Ð½Ñ‹Ð¹ ÑˆÐµÐ¹Ð´ÐµÑ€
    return shader

def draw():
    glClear(GL_COLOR_BUFFER_BIT)                    
    glEnableClientState(GL_VERTEX_ARRAY)            # Ð’ÐºÐ»ÑŽÑ‡Ð°ÐµÐ¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ð½Ð¸Ðµ Ð¼Ð°ÑÑÐ¸Ð²Ð° Ð²ÐµÑ€ÑˆÐ¸Ð½
    glEnableClientState(GL_COLOR_ARRAY)             # Ð’ÐºÐ»ÑŽÑ‡Ð°ÐµÐ¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ð½Ð¸Ðµ Ð¼Ð°ÑÑÐ¸Ð²Ð° Ñ†Ð²ÐµÑ‚Ð¾Ð²
    # Ð£ÐºÐ°Ð·Ñ‹Ð²Ð°ÐµÐ¼, Ð³Ð´Ðµ Ð²Ð·ÑÑ‚ÑŒ Ð¼Ð°ÑÑÐ¸Ð² Ð²ÐµÑ€ÑˆÐ¸Ð½:
    # ÐŸÐµÑ€Ð²Ñ‹Ð¹ Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€ - ÑÐºÐ¾Ð»ÑŒÐºÐ¾ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·ÑƒÐµÑ‚ÑÑ ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚ Ð½Ð° Ð¾Ð´Ð½Ñƒ Ð²ÐµÑ€ÑˆÐ¸Ð½Ñƒ
    # Ð’Ñ‚Ð¾Ñ€Ð¾Ð¹ Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€ - Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ñ‚Ð¸Ð¿ Ð´Ð°Ð½Ð½Ñ‹Ñ… Ð´Ð»Ñ ÐºÐ°Ð¶Ð´Ð¾Ð¹ ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚Ñ‹ Ð²ÐµÑ€ÑˆÐ¸Ð½Ñ‹
    # Ð¢Ñ€ÐµÑ‚Ð¸Ð¹ Ð¿Ð°Ñ€Ð¼ÐµÑ‚Ñ€ - Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÑ‚ ÑÐ¼ÐµÑ‰ÐµÐ½Ð¸Ðµ Ð¼ÐµÐ¶Ð´Ñƒ Ð²ÐµÑ€ÑˆÐ¸Ð½Ð°Ð¼Ð¸ Ð² Ð¼Ð°ÑÑÐ¸Ð²Ðµ
    # Ð•ÑÐ»Ð¸ Ð²ÐµÑ€ÑˆÐ¸Ð½Ñ‹ Ð¸Ð´ÑƒÑ‚ Ð¾Ð´Ð½Ð° Ð·Ð° Ð´Ñ€ÑƒÐ³Ð¾Ð¹, Ñ‚Ð¾ ÑÐ¼ÐµÑ‰ÐµÐ½Ð¸Ðµ 0
    # Ð§ÐµÑ‚Ð²ÐµÑ€Ñ‚Ñ‹Ð¹ Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€ - ÑƒÐºÐ°Ð·Ð°Ñ‚ÐµÐ»ÑŒ Ð½Ð° Ð¿ÐµÑ€Ð²ÑƒÑŽ ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚Ñƒ Ð¿ÐµÑ€Ð²Ð¾Ð¹ Ð²ÐµÑ€ÑˆÐ¸Ð½Ñ‹ Ð² Ð¼Ð°ÑÑÐ¸Ð²Ðµ
    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    # Ð£ÐºÐ°Ð·Ñ‹Ð²Ð°ÐµÐ¼, Ð³Ð´Ðµ Ð²Ð·ÑÑ‚ÑŒ Ð¼Ð°ÑÑÐ¸Ð² Ñ†Ð²ÐµÑ‚Ð¾Ð²:
    # ÐŸÐ°Ñ€Ð°Ð¼ÐµÑ‚Ñ€Ñ‹ Ð°Ð½Ð°Ð»Ð¾Ð³Ð¸Ñ‡Ð½Ñ‹, Ð½Ð¾ ÑƒÐºÐ°Ð·Ñ‹Ð²Ð°ÐµÑ‚ÑÑ Ð¼Ð°ÑÑÐ¸Ð² Ñ†Ð²ÐµÑ‚Ð¾Ð²
    glColorPointer(3, GL_FLOAT, 0, pointcolor)
    # Ð Ð¸ÑÑƒÐµÐ¼ Ð´Ð°Ð½Ð½Ñ‹Ðµ Ð¼Ð°ÑÑÐ¸Ð²Ð¾Ð² Ð·Ð° Ð¾Ð´Ð¸Ð½ Ð¿Ñ€Ð¾Ñ…Ð¾Ð´:
    # ÐŸÐµÑ€Ð²Ñ‹Ð¹ Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€ - ÐºÐ°ÐºÐ¾Ð¹ Ñ‚Ð¸Ð¿ Ð¿Ñ€Ð¸Ð¼Ð¸Ñ‚Ð¸Ð²Ð¾Ð² Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ (Ñ‚Ñ€ÐµÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ¸, Ñ‚Ð¾Ñ‡ÐºÐ¸, Ð»Ð¸Ð½Ð¸Ð¸ Ð¸ Ð´Ñ€.)
    # Ð’Ñ‚Ð¾Ñ€Ð¾Ð¹ Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€ - Ð½Ð°Ñ‡Ð°Ð»ÑŒÐ½Ñ‹Ð¹ Ð¸Ð½Ð´ÐµÐºÑ Ð² ÑƒÐºÐ°Ð·Ð°Ð½Ð½Ñ‹Ñ… Ð¼Ð°ÑÑÐ¸Ð²Ð°Ñ…
    # Ð¢Ñ€ÐµÑ‚Ð¸Ð¹ Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€ - ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð¾ Ñ€Ð¸ÑÑƒÐµÐ¼Ñ‹Ñ… Ð¾Ð±ÑŠÐµÐºÑ‚Ð¾Ð² (Ð² Ð½Ð°ÑˆÐµÐ¼ ÑÐ»ÑƒÑ‡Ð°Ðµ ÑÑ‚Ð¾ 3 Ð²ÐµÑ€ÑˆÐ¸Ð½Ñ‹ - 9 ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glDisableClientState(GL_VERTEX_ARRAY)           # ÐžÑ‚ÐºÐ»ÑŽÑ‡Ð°ÐµÐ¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ð½Ð¸Ðµ Ð¼Ð°ÑÑÐ¸Ð²Ð° Ð²ÐµÑ€ÑˆÐ¸Ð½
    glDisableClientState(GL_COLOR_ARRAY)            # ÐžÑ‚ÐºÐ»ÑŽÑ‡Ð°ÐµÐ¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ð½Ð¸Ðµ Ð¼Ð°ÑÑÐ¸Ð²Ð° Ñ†Ð²ÐµÑ‚Ð¾Ð²
    glutSwapBuffers()                               # Ð’Ñ‹Ð²Ð¾Ð´Ð¸Ð¼ Ð²ÑÐµ Ð½Ð°Ñ€Ð¸ÑÐ¾Ð²Ð°Ð½Ð½Ð¾Ðµ Ð² Ð¿Ð°Ð¼ÑÑ‚Ð¸ Ð½Ð° ÑÐºÑ€Ð°Ð½


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(300, 300)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Lab Seven: Shaders!")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialkeys)
glClearColor(0.2, 0.2, 0.2, 1)
#create vertex shader
vertex = create_shader(GL_VERTEX_SHADER, """
varying vec4 vertex_color;
            void main(){
                gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                vertex_color = gl_Color;
            }""")
#fragment shader
fragment = create_shader(GL_FRAGMENT_SHADER, """
varying vec4 vertex_color;
            void main() {
                gl_FragColor = vertex_color;
}""")
#create empty object of shader program
program = glCreateProgram()
#connect vertex shader and program
glAttachShader(program, vertex)
#fragment+program
glAttachShader(program, fragment)
# "Ð¡Ð¾Ð±Ð¸Ñ€Ð°ÐµÐ¼" ÑˆÐµÐ¹Ð´ÐµÑ€Ð½ÑƒÑŽ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ñƒ
glLinkProgram(program)
# Ð¡Ð¾Ð¾Ð±Ñ‰Ð°ÐµÐ¼ OpenGL Ð¾ Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼Ð¾ÑÑ‚Ð¸ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð°Ð½Ð½ÑƒÑŽ ÑˆÐµÐ¹Ð´ÐµÑ€Ð½Ñƒ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ñƒ Ð¿Ñ€Ð¸ Ð¾Ñ‚Ñ€Ð¸ÑÐ¾Ð²ÐºÐµ Ð¾Ð±ÑŠÐµÐºÑ‚Ð¾Ð²
glUseProgram(program)
# ÐžÐ¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ð¼Ð°ÑÑÐ¸Ð² Ð²ÐµÑ€ÑˆÐ¸Ð½ (Ñ‚Ñ€Ð¸ Ð²ÐµÑ€ÑˆÐ¸Ð½Ñ‹ Ð¿Ð¾ Ñ‚Ñ€Ð¸ ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚Ñ‹)
pointdata = [[0, 0.5, 0], [-0.5, -0.5, 0], [0.5, -0.5, 0]]
# ÐžÐ¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ð¼Ð°ÑÑÐ¸Ð² Ñ†Ð²ÐµÑ‚Ð¾Ð² (Ð¿Ð¾ Ð¾Ð´Ð½Ð¾Ð¼Ñƒ Ñ†Ð²ÐµÑ‚Ñƒ Ð´Ð»Ñ ÐºÐ°Ð¶Ð´Ð¾Ð¹ Ð²ÐµÑ€ÑˆÐ¸Ð½Ñ‹)
pointcolor = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
# Ð—Ð°Ð¿ÑƒÑÐºÐ°ÐµÐ¼ Ð¾ÑÐ½Ð¾Ð²Ð½Ð¾Ð¹ Ñ†Ð¸ÐºÐ»
glutMainLoop()
