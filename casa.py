from OpenGL import GL
import numpy as np
import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import PIL
from PIL import Image

punto_x = 0.0
punto_y = -0.0
punto_z = 10.0
ojo_x = 0.0
ojo_y = 0.0
ojo_z = 0.0
vector_x = 0.0
vector_y = 1.0
vectorz = 0.0
Luz_difusa=[5.0,5.0,5.0,5.0]
Luz_especular=[5.0,5.0,5.0,5.0]
posicion=[50.0,50.0,50.0,1.0]
direccion=[0.0,40.0,0.0]
# La matriz capa nos ayudara a construir la casa dentro del eje z  semejante a la manera
# que trabaja una impresora 3D 
capa1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# 1 2 3 4 5 6 7 8 9
capa2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 2
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 4
         [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 5
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 6
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 7
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 9
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # 12
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 13
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 14
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 15
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 16
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 17
         [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]  # 18

# 1 2 3 4 5 6 7 8 9
capa3 = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 2
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 4
         [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 5
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 6
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 7
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 9
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # 12
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 13
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 14
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 15
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 16
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 17
         [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]]  # 18
# 1 2 3 4 5 6 7 8 9
capa4 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 2
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 3
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 4
         [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],  # 5
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 6
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 7
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 9
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # 12
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 13
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 14
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 15
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 16
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 17
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]]  # 18
# 1 2 3 4 5 6 7 8 9
capa5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 2
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 3
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 4
         [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],  # 5
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 6
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 7
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 9
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # 12
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 13
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 14
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 15
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 16
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 17
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]  # 18


# se define largo y alto
w, h = len(capa1), len(capa1[0])
#funcion que recibe la localizacion de la imagen y lel numero de textura
def cargarTexturas(path,texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) #en esta parte se dira que la imagen se repita por toda el area indicada
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = Image.open(path) #abrimos la imagem
    image = image.transpose(Image.FLIP_TOP_BOTTOM) 
    img_data = image.convert("RGBA").tobytes() #lo convertimos en un arreglo de bytes
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data) #decimos que esta kl aimagen que usaremos porl largo y ancho
    return texture
    

def cuadrados():
    # cuando las capas se construyen se tienen que desplazar en el eje Z pero
    # de alguna manera tambien se desplazan en el eje x y hay que correguirlo
    ajustez = 18
    ajustex = 340
    ajustez2 = ajustez*2
    ajustex2 = ajustex*2
    ajustez3 = ajustez*3
    ajustex3 = ajustex*3
    ajustez4 = ajustez*4
    ajustex4 = ajustex*4
    # PISO:
    gluLookAt(punto_x, punto_y, punto_z, ojo_x, ojo_y,
              ojo_z, vector_x, vector_y, vectorz)
    
    
    #primeras texturas
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING) #activa la iluminacion
    glEnable(GL_LIGHT0) #activa el primer foco
    glLightfv (GL_LIGHT0, GL_DIFFUSE, Luz_difusa) #activamos la luz difus
    glLightfv (GL_LIGHT0, GL_SPECULAR, Luz_especular) #activamos la luz especular
    glLightfv (GL_LIGHT0, GL_POSITION, posicion) #le decimo es que psicion estamos
    glLightfv (GL_LIGHT0, GL_SPOT_DIRECTION, direccion) #le decmo hacia donde quermos apunte la luz
    glLightf (GL_LIGHT0, GL_SPOT_CUTOFF, 30.0)  
    tex=cargarTexturas('.vscode\strr.png',1) #buscmaos la imgen que queremos aplica
    glGenTextures(tex) #asociamos la imagen 
    glBegin(GL_QUADS)
    #glColor3f(1.0, 0.5, 0.0)
    glNormal3f(1,0,1) #decimos la normal para indicar la luza
    glTexCoord2f(22.0,28.0) #apilicamos la textura en los vertices marcados por esta funcion
    glVertex3f(22, 28, -18*5)
    glTexCoord2f(320.0,28.0)
    glVertex3f(320, 28, -18*5)
    glTexCoord2f(320.0,340.0)
    glVertex3f(320, 340, -18*5)
    glTexCoord2f(22.0,340.0)
    glVertex3f(22, 340, -18*5)
    glEnd()
    #glFlush()
    glDisable(GL_TEXTURE_2D) #desactivmoas l atextura 2D
    glDisable(GL_LIGHTING) #desactimamos la iluminacion
  
    
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\cuadros.png',1)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(1.0,1.0,1.0)
    glTexCoord2f(260,28)
    glVertex3f(260,28,-80.5)
    glTexCoord2f(320,28)
    glVertex3f(320,28,-80.5)
    glTexCoord2f(320,120)
    glVertex3f(320,120,-80.5)
    glTexCoord2f(260,120)
    glVertex3f(260,120,-80.5)
    #sglFlush
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
    
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(0.4,0.4,0.4)
    glNormal3f(0,0,1)
    glTexCoord2f(200,180)
    glVertex3f(200,180,18.5)
    glTexCoord2f(320,180)
    glVertex3f(320,180,18.5)
    glTexCoord2f(320,180)
    glVertex3f(320,180,-80.5)
    glTexCoord2f(200,180)
    glVertex3f(200,180,-80.5)
    #glFlush
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(0.4,0.4,0.4)
    glNormal3f(0,0,1)
    glTexCoord2f(240,140)
    glVertex3f(240,140,18.5)
    glTexCoord2f(320,140)
    glVertex3f(320,140,18.5)
    glTexCoord2f(320,140)
    glVertex3f(320,140,-80.5)
    glTexCoord2f(240,140)
    glVertex3f(240,140,-80.5)
    #glFlush
    glEnd()
    glDisable(GL_TEXTURE_2D)

    #borde de la puerta del baño
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(120,260)
    glVertex3f(120,260,18.5)
    glTexCoord2f(200,260)
    glVertex3f(200,260,18.5)
    glTexCoord2f(200,260)
    glVertex3f(200,260,-10.5)
    glTexCoord2f(120,260)
    glVertex3f(120,260,-10.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(120,260)
    glVertex3f(120,260,18.5)
    glTexCoord2f(140,260)
    glVertex3f(140,260,18.5)
    glTexCoord2f(140,260)
    glVertex3f(140,260,-80.5)
    glTexCoord2f(120,260)
    glVertex3f(120,260,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(180,260)
    glVertex3f(180,260,18.5)
    glTexCoord2f(200,260)
    glVertex3f(200,260,18.5)
    glTexCoord2f(200,260)
    glVertex3f(200,260,-80.5)
    glTexCoord2f(180,260)
    glVertex3f(180,260,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(20,20)
    glVertex3f(20,20,18.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,18.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-5.5)
    glTexCoord2f(20,20)
    glVertex3f(20,20,-5.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(20,20)
    glVertex3f(20,20,-40.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-40.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-80.5)
    glTexCoord2f(20,20)
    glVertex3f(20,20,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(20,20)
    glVertex3f(20,20,18.5)
    glTexCoord2f(40,20)
    glVertex3f(40,20,18.5)
    glTexCoord2f(40,20)
    glVertex3f(40,20,-80.5)
    glTexCoord2f(20,20)
    glVertex3f(20,20,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(160,20)
    glVertex3f(160,20,18.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,18.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-80.5)
    glTexCoord2f(160,20)
    glVertex3f(160,20,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(240,20)
    glVertex3f(240,20,18.5)
    glTexCoord2f(320,20)
    glVertex3f(320,20,18.5)
    glTexCoord2f(320,20)
    glVertex3f(320,20,-20.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-20.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-40.5)
    glTexCoord2f(320,20)
    glVertex3f(320,20,-40.5)
    glTexCoord2f(320,20)
    glVertex3f(320,20,-80.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\piedra.jpg',3)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glTexCoord2f(240,20)
    glVertex3f(240,20,18.5)
    glTexCoord2f(270,20)
    glVertex3f(270,20,18.5)
    glTexCoord2f(270,20)
    glVertex3f(270,20,-80.5)
    glTexCoord2f(240,20)
    glVertex3f(240,20,-80.5)
    glEnd()
    glDisable(GL_LIGHT0)
    
    #####################
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glTexCoord2f(120,280)
    glVertex3f(120,280,18.5)
    glTexCoord2f(200,280)
    glVertex3f(200,280,18.5)
    glTexCoord2f(200,280)
    glVertex3f(200,280,-10.5)
    glTexCoord2f(120,280)
    glVertex3f(120,280,-10.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glTexCoord2f(120,280)
    glVertex3f(120,280,18.5)
    glTexCoord2f(140,280)
    glVertex3f(140,280,18.5)
    glTexCoord2f(140,280)
    glVertex3f(140,280,-80.5)
    glTexCoord2f(120,280)
    glVertex3f(120,280,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glTexCoord2f(180,280)
    glVertex3f(180,280,18.5)
    glTexCoord2f(200,280)
    glVertex3f(200,280,18.5)
    glTexCoord2f(200,280)
    glVertex3f(200,280,-80.5)
    glTexCoord2f(180,280)
    glVertex3f(180,280,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glTexCoord2f(120,330)
    glVertex3f(120,330,18.5)
    glTexCoord2f(200,330)
    glVertex3f(200,330,18.5)
    glTexCoord2f(200,280)
    glVertex3f(200,330,-80.5)
    glTexCoord2f(120,330)
    glVertex3f(120,330,-80.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glTexCoord2f(120,270)
    glVertex3f(120,270,18.5)
    glTexCoord2f(120,270)
    glVertex3f(120,270,-80.5)
    glTexCoord2f(120,340)
    glVertex3f(120,340,-80.5)
    glTexCoord2f(120,340)
    glVertex3f(120,340,18.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glBegin(GL_QUADS)
    glColor3f(0.3,0.3,0.3)
    glVertex3f(100,270,18.5)
    glVertex3f(100,270,-80.5)
    glVertex3f(100,340,-80.5)
    glVertex3f(100,340,18.5)
    glEnd()

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glTexCoord2f(200,270)
    glVertex3f(200,270,18.5)
    glTexCoord2f(200,270)
    glVertex3f(200,270,-80.5)
    glTexCoord2f(200,340)
    glVertex3f(200,340,-80.5)
    glTexCoord2f(200,340)
    glVertex3f(200,340,18.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glBegin(GL_QUADS)
    glColor3f(0.9,0.4,0.0)
    glVertex3f(220,270,18.5)
    glVertex3f(220,270,-80.5)
    glVertex3f(220,340,-80.5)
    glVertex3f(220,340,18.5)
    glEnd()
    
    ####################
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\strr.png',4)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    glColor3f(1.0,0.5,0.0)
    glTexCoord2f(10,180)
    glVertex3f(10,180,18.5)
    glTexCoord2f(120,180)
    glVertex3f(120,180,18.5)
    glTexCoord2f(120,180)
    glVertex3f(120,180,-80.5)
    glTexCoord2f(10,180)
    glVertex3f(10,180,-80.5)
    #glFlush
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(0.4,0.4,0.4)
    glTexCoord2f(240,120)
    glVertex3f(240,120,18.5)
    glTexCoord2f(320,120)
    glVertex3f(320,120,18.5)
    glTexCoord2f(320,120)
    glVertex3f(320,120,-80.5)
    glTexCoord2f(240,120)
    glVertex3f(240,120,-80.5)
    #glFlush
    glEnd()
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(0.4,0.4,0.4)
    glTexCoord2f(320,20)
    glVertex3f(320,20,18.5)
    glTexCoord2f(320,20)
    glVertex3f(320,20,-80.5)
    glTexCoord2f(320,120)
    glVertex3f(320,120,-80.5)
    glTexCoord2f(320,120)
    glVertex3f(320,120,18.5)
    #glFlush
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
    #borde de la puesta principal
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(320,140,18.5)
    glVertex3f(320,140,-10.5)
    glVertex3f(320,180,-10.5)
    glVertex3f(320,180,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(320,140,18.5)
    glVertex3f(320,140,-80.5)
    glVertex3f(320,145,-80.5)
    glVertex3f(320,145,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(320,175,18.5)
    glVertex3f(320,175,-80.5)
    glVertex3f(320,180,-80.5)
    glVertex3f(320,180,18.5)
    glEnd()
    
    #borde de la puerta de la cocina
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(240,20,18.5)
    glVertex3f(240,20,-10.5)
    glVertex3f(240,140,-10.5)
    glVertex3f(240,140,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(240,20,18.5)
    glVertex3f(240,20,-80.5)
    glVertex3f(240,60,-80.5)
    glVertex3f(240,60,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(240,100,18.5)
    glVertex3f(240,100,-80.5)
    glVertex3f(240,140,-80.5)
    glVertex3f(240,140,18.5)
    glEnd()

    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(1.0,0.0,-1.0)
    glTexCoord2f(260,20)
    glVertex3f(260,20,18.5)
    glTexCoord2f(260,20)
    glVertex3f(260,20,-10.5)
    glTexCoord2f(260,140)
    glVertex3f(260,140,-10.5)
    glTexCoord2f(260,140)
    glVertex3f(260,140,18.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(1.0,0.0,-1.0)
    glTexCoord2f(260,20)
    glVertex3f(260,20,18.5)
    glTexCoord2f(260,20)
    glVertex3f(260,20,-80.5)
    glTexCoord2f(260,60)
    glVertex3f(260,60,-80.5)
    glTexCoord2f(260,60)
    glVertex3f(260,60,18.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
    glEnable(GL_TEXTURE_2D)
    tex=cargarTexturas('.vscode\pisoco.jpg',5)
    glGenTextures(tex)
    glBegin(GL_QUADS)
    #glColor3f(1.0,0.0,-1.0)
    glTexCoord2f(260,100)
    glVertex3f(260,100,18.5)
    glTexCoord2f(260,100)
    glVertex3f(260,100,-80.5)
    glTexCoord2f(260,140)
    glVertex3f(260,140,-80.5)
    glTexCoord2f(260,140)
    glVertex3f(260,140,18.5)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    #borde de las puertas de las habitaciones 
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(120,180,18.5)
    glVertex3f(120,180,-10.5)
    glVertex3f(120,265,-10.5)
    glVertex3f(120,265,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(120,180,18.5)
    glVertex3f(120,180,-80.5)
    glVertex3f(120,220,-80.5)
    glVertex3f(120,220,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.3,0.3,0.3)
    glVertex3f(100,180,18.5)
    glVertex3f(100,180,-10.5)
    glVertex3f(100,265,-10.5)
    glVertex3f(100,265,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.3,0.3,0.3)
    glVertex3f(100,180,18.5)
    glVertex3f(100,180,-80.5)
    glVertex3f(100,220,-80.5)
    glVertex3f(100,220,18.5)
    glEnd()
    ###
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(200,180,18.5)
    glVertex3f(200,180,-10.5)
    glVertex3f(200,265,-10.5)
    glVertex3f(200,265,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(200,180,18.5)
    glVertex3f(200,180,-80.5)
    glVertex3f(200,200,-80.5)
    glVertex3f(200,200,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(200,240,18.5)
    glVertex3f(200,240,-80.5)
    glVertex3f(200,270,-80.5)
    glVertex3f(200,270,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.9,0.4,0.0)
    glVertex3f(220,180,18.5)
    glVertex3f(220,180,-10.5)
    glVertex3f(220,265,-10.5)
    glVertex3f(220,265,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.9,0.4,0.0)
    glVertex3f(220,180,18.5)
    glVertex3f(220,180,-80.5)
    glVertex3f(220,200,-80.5)
    glVertex3f(220,200,18.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.9,0.4,0.0)
    glVertex3f(220,240,18.5)
    glVertex3f(220,240,-80.5)
    glVertex3f(220,270,-80.5)
    glVertex3f(220,270,18.5)
    glEnd()
    #paredes sin ventana
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(10,335,18.5)
    glVertex3f(120,335,18.5)
    glVertex3f(120,335,-80.5)
    glVertex3f(10,335,-80.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(10,200,18.5)
    glVertex3f(120,200,18.5)
    glVertex3f(120,200,-80.5)
    glVertex3f(10,200,-80.5)
    glEnd()
    
     
    glBegin(GL_QUADS)
    glNormal3f(0,0,1)
    glColor3f(1.0,1.0,0.0)
    glVertex3f(200,335,18.5)
    glVertex3f(320,335,18.5)
    glVertex3f(320,335,-80.5)
    glVertex3f(200,335,-80.5)
    glEnd()
   
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,0.0)
    glVertex3f(200,200,18.5)
    glVertex3f(320,200,18.5)
    glVertex3f(320,200,-80.5)
    glVertex3f(200,200,-80.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,-1.0)
    glVertex3f(20,20,18.5)
    glVertex3f(20,20,-80.5)
    glVertex3f(20,200,-80.5)
    glVertex3f(20,200,18.5)
    glEnd()

    #ventanas delanteras
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(30,0,-5.5)
    glVertex3f(80,0,-5.5)
    glVertex3f(80,0,-42.5)
    glVertex3f(30,0,-42.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(100,0,-5.5)
    glVertex3f(160,0,-5.5)
    glVertex3f(160,0,-42.5)
    glVertex3f(100,0,-42.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(270,0,-5.5)
    glVertex3f(330,0,-5.5)
    glVertex3f(330,0,-60.5)
    glVertex3f(270,0,-60.5)
    glEnd()

    #ventan de los lados 
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(0,210,0.5)
    glVertex3f(0,335,0.5)
    glVertex3f(0,335,-45.5)
    glVertex3f(0,210,-45.5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(320,210,5.5)
    glVertex3f(320,320,5.5)
    glVertex3f(320,320,-45.5)
    glVertex3f(320,210,-45.5)
    glEnd()

    x = 0  # definimos x para posicion a lo ancho
    # a continuacion se van a contruir las 5 capas
    # CAPA1
    for m in np.rot90(capa1, -1):
        y = 0  # definimos x para posicion a lo ancho
        for n in m:
            if n == 1:
                # se dinujara un cubo si el elemento de la matriz es uno
                glBegin(GL_QUADS)
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x, y, -10.0)
                glVertex3f(x+20, y, -10.0)
                glVertex3f(x+20, y+20, -10.0)
                glVertex3f(x, y+20, -10.0)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x, y, 10.0)
                glVertex3f(x+20, y, 10.0)
                glVertex3f(x+20, y+20, 10.0)
                glVertex3f(x, y+20, 10.0)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x, y, -10.0)
                glVertex3f(x+20, y, -10.0)
                glVertex3f(x+20, y+20, 10.0)
                glVertex3f(x, y+20, 10.0)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x, y, 10.0)
                glVertex3f(x+20, y, 10.0)
                glVertex3f(x+20, y+20, -10.0)
                glVertex3f(x, y+20, -10.0)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x, y, 10.0)
                glVertex3f(x+20, y, -10.0)
                glVertex3f(x+20, y+20, -10.0)
                glVertex3f(x, y+20, 10.0)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x, y, -10.0)
                glVertex3f(x+20, y, 10.0)
                glVertex3f(x+20, y+20, 10.0)
                glVertex3f(x, y+20, -10.0)

                glEnd()
                glFlush()
            y = y+20  # aumentamos tanto x como y|
        x = x+20
    # CAPA2
    for m in np.rot90(capa2, -1):
        y = 0  # definimos x para posicion a lo ancho
        for n in m:
            if n == 1:
                # se dinujara un cubo si el elemento de la matriz es uno
                glBegin(GL_QUADS) #cara de atraz
                glColor3f(1.0, 1.0, 1.0)
                glNormal3f(0,0,1)
                glVertex3f(x-ajustex, y, (-10.0)-ajustez)
                glVertex3f(x+20-ajustex, y, (-10.0)-ajustez)
                glVertex3f(x+20-ajustex, y+20, (-10.0)-ajustez)
                glVertex3f(x-ajustex, y+20, (-10.0)-ajustez)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0) #cara de eenfrente
                glVertex3f(x-ajustex, y, (10.0)-ajustez)
                glVertex3f(x-ajustex+20, y, (10.0)-ajustez)
                glVertex3f(x-ajustex+20, y+20, (10.0)-ajustez)
                glVertex3f(x-ajustex, y+20, (10.0)-ajustez)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0) #cara de uno de los lados
                glVertex3f(x-ajustex, y, (-10.0)-ajustez)
                glVertex3f(x-ajustex+20, y, (-10.0)-ajustez)
                glVertex3f(x-ajustex+20, y+20, (10.0)-ajustez)
                glVertex3f(x-ajustex, y+20, (10.0)-ajustez)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0) #cara del lado izquierdo 
                glVertex3f(x-ajustex, y, (10.0)-ajustez)
                glVertex3f(x-ajustex+20, y, (10.0)-ajustez)
                glVertex3f(x-ajustex+20, y+20, (-10.0)-ajustez)
                glVertex3f(x-ajustex, y+20, (-10.0)-ajustez)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0) #cara de otro de los lados 
                glVertex3f(x-ajustex, y, (10.0)-ajustez)
                glVertex3f(x-ajustex+20, y, (-10.0)-ajustez)
                glVertex3f(x-ajustex+20, y+20, (-10.0)-ajustez)
                glVertex3f(x-ajustex, y+20, (10.0)-ajustez)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex, y, (-10.0)-ajustez)
                glVertex3f(x-ajustex+20, y, (10.0)-ajustez)
                glVertex3f(x-ajustex+20, y+20, (10.0)-ajustez)
                glVertex3f(x-ajustex, y+20, (-10.0)-ajustez)

                glEnd()
                glFlush()

            y = y+20  # aumentamos tanto x como y|
        x = x+20
    # CAPA 3
    for m in np.rot90(capa3, -1):
        y = 0  # definimos x para posicion a lo ancho
        for n in m:
            if n == 1:
                # se dinujara un cubo si el elemento de la matriz es uno
                glBegin(GL_QUADS)
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0,1.0)
                glVertex3f(x-ajustex2, y, (-10.0)-ajustez2)
                glVertex3f(x+20-ajustex2, y, (-10.0)-ajustez2)
                glVertex3f(x+20-ajustex2, y+20, (-10.0)-ajustez2)
                glVertex3f(x-ajustex2, y+20, (-10.0)-ajustez2)
                

                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex2, y, (10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y, (10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y+20, (10.0)-ajustez2)
                glVertex3f(x-ajustex2, y+20, (10.0)-ajustez2)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex2, y, (-10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y, (-10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y+20, (10.0)-ajustez2)
                glVertex3f(x-ajustex2, y+20, (10.0)-ajustez2)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex2, y, (10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y, (10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y+20, (-10.0)-ajustez2)
                glVertex3f(x-ajustex2, y+20, (-10.0)-ajustez2)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex2, y, (10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y, (-10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y+20, (-10.0)-ajustez2)
                glVertex3f(x-ajustex2, y+20, (10.0)-ajustez2)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex2, y, (-10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y, (10.0)-ajustez2)
                glVertex3f(x-ajustex2+20, y+20, (10.0)-ajustez2)
                glVertex3f(x-ajustex2, y+20, (-10.0)-ajustez2)

                glEnd()
                glFlush()

            y = y+20  # aumentamos tanto x como y|
        x = x+20
    # CAPA 4
    for m in np.rot90(capa4, -1):
        y = 0  # definimos x para posicion a lo ancho
        for n in m:
            if n == 1:
                # se dinujara un cubo si el elemento de la matriz es uno
                glNormal3f(0,0,1)
                glBegin(GL_QUADS)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex3, y, (-10.0)-ajustez3)
                glVertex3f(x+20-ajustex3, y, (-10.0)-ajustez3)
                glVertex3f(x+20-ajustex3, y+20, (-10.0)-ajustez3)
                glVertex3f(x-ajustex3, y+20, (-10.0)-ajustez3)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex3, y, (10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y, (10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y+20, (10.0)-ajustez3)
                glVertex3f(x-ajustex3, y+20, (10.0)-ajustez3)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex3, y, (-10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y, (-10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y+20, (10.0)-ajustez3)
                glVertex3f(x-ajustex3, y+20, (10.0)-ajustez3)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex3, y, (10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y, (10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y+20, (-10.0)-ajustez3)
                glVertex3f(x-ajustex3, y+20, (-10.0)-ajustez3)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex3, y, (10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y, (-10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y+20, (-10.0)-ajustez3)
                glVertex3f(x-ajustex3, y+20, (10.0)-ajustez3)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex3, y, (-10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y, (10.0)-ajustez3)
                glVertex3f(x-ajustex3+20, y+20, (10.0)-ajustez3)
                glVertex3f(x-ajustex3, y+20, (-10.0)-ajustez3)

                glEnd()
                glFlush()

            y = y+20  # aumentamos tanto x como y|
        x = x+20
    # CAPA 5
    for m in np.rot90(capa5, -1):
        y = 0  # definimos x para posicion a lo ancho
        for n in m:
            if n == 1:
                # se dinujara un cubo si el elemento de la matriz es uno
                glBegin(GL_QUADS)
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex4, y, (-10.0)-ajustez4)
                glVertex3f(x+20-ajustex4, y, (-10.0)-ajustez4)
                glVertex3f(x+20-ajustex4, y+20, (-10.0)-ajustez4)
                glVertex3f(x-ajustex4, y+20, (-10.0)-ajustez4)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex4, y, (10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y, (10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y+20, (10.0)-ajustez4)
                glVertex3f(x-ajustex4, y+20, (10.0)-ajustez4)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex4, y, (-10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y, (-10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y+20, (10.0)-ajustez4)
                glVertex3f(x-ajustex4, y+20, (10.0)-ajustez4)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex4, y, (10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y, (10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y+20, (-10.0)-ajustez4)
                glVertex3f(x-ajustex4, y+20, (-10.0)-ajustez4)
                
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex4, y, (10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y, (-10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y+20, (-10.0)-ajustez4)
                glVertex3f(x-ajustex4, y+20, (10.0)-ajustez4)
               
                glNormal3f(0,0,1)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(x-ajustex4, y, (-10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y, (10.0)-ajustez4)
                glVertex3f(x-ajustex4+20, y+20, (10.0)-ajustez4)
                glVertex3f(x-ajustex4, y+20, (-10.0)-ajustez4)

                glEnd()
                glFlush()

            y = y+20  # aumentamos tanto x como y|
        x = x+20
    
    # gluPerspective(0,1.0,0.2,0.5)


def Mimatriz():
    a = 80
    # multiplicamos nuestro ancho y alto por 10 para que se vea
    glViewport(0, 0, (w*a), (h*a))
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección

    glLoadIdentity()  # Limpiamos la matriz seleccionada
    # glFrustum(0.0,1000,0.0,1000,100,100)
    #gluPerspective(30,1000/1000,1,200)
    # Definimos la proyección a usar como una ortogonal
    glOrtho(0.0, (w*a), 0.0, (h*a), -(h*a), (h*a))
    #(-90, 0,0 , 0)
    #gluPerspective(10,(w*20)/(h*20),10,11)
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo

    glLoadIdentity()


def desplegar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    glClearColor(0.6, 0.9, 0.6, 0)
    Mimatriz()
    cuadrados()

    glutSwapBuffers()


def llaves(llave, x, y):
    global punto_x
    global punto_y
    global punto_z
    global ojo_x
    global ojo_y
    global ojo_z
    global vector_x
    global vector_y
    global vectorz

    if (llave == GLUT_KEY_UP):
        punto_x = punto_x+5
        ojo_z = ojo_z-5
    elif (llave == GLUT_KEY_DOWN):
        punto_x = punto_x-5
        ojo_z = ojo_z+5
    elif (llave == GLUT_KEY_LEFT):
        punto_y = punto_y+5
        ojo_z = ojo_z+5
    elif (llave == GLUT_KEY_RIGHT):
        punto_y = punto_y-5
        ojo_z = ojo_z-5
    glutPostRedisplay()


def main():
    glutInit()  # Iniciamos la instancia de glut
    # Asignamos la parte de profunidad para indicar que existe el ejex
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # Damos el tamaño de la ventana que se mostrará
    glutInitWindowSize((h*20), (w*20))
    # Coordenadas en donde aparecerá la venta en la pantalla
    glutInitWindowPosition(0, 0)
    # Damos un titulo para la ventana
    wind = glutCreateWindow("Casa")
    glEnable(GL_DEPTH_TEST)  # activamos la profunidad
    
    # Designamos la función que contiene los elemntos que serán mostrados en la escena
    glutDisplayFunc(desplegar)
    glutIdleFunc(desplegar)
    glutSpecialFunc(llaves)
    glutMainLoop()  # Iniciamos el loop principal


main()