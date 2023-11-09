import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

vertices_cube = [
    (-0.5, -0.5, -0.5),  # Вершины куба
    (0.5, -0.5, -0.5),
    (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, -0.5, 0.5),
    (0.5, -0.5, 0.5),
    (0.5, 0.5, 0.5),
    (-0.5, 0.5, 0.5)
]

faces_cube = [
    (0, 1, 2, 3),  # Грани куба (вершины, образующие грани)
    (1, 5, 6, 2),
    (5, 4, 7, 6),
    (4, 0, 3, 7),
    (3, 2, 6, 7),
    (4, 5, 1, 0)
]

vertices_sphere = []  # Список вершин сферы
edges_sphere = []  # Список ребер сферы
slices = 30  # Количество сегментов по горизонтали
stacks = 30  # Количество сегментов по вертикали

def create_sphere_vertices():
    """
    Создает вершины сферы и добавляет их в список vertices_sphere.
    """
    for j in range(stacks + 1):
        lat = math.pi * (-0.5 + (j / float(stacks)))
        z = math.sin(lat)
        zr = math.cos(lat)

        for i in range(slices + 1):
            lng = 2 * math.pi * (i / float(slices))
            x = math.cos(lng)
            y = math.sin(lng)

            vertices_sphere.append((x * zr, y * zr, z))

def create_sphere_edges():
    """
    Создает ребра сферы и добавляет их в список edges_sphere.
    """
    for j in range(stacks):
        for i in range(slices):
            v1 = j * (slices + 1) + i
            v2 = v1 + slices + 1

            edges_sphere.append((v1, v1 + 1))
            edges_sphere.append((v1 + 1, v2 + 1))
            edges_sphere.append((v2 + 1, v2))
            edges_sphere.append((v2, v1))

def draw_cube():
    """
    Рисует куб, используя вершины из vertices_cube и грани из faces_cube.
    """
    glBegin(GL_QUADS)
    for face in faces_cube:
        for vertex in face:
            glVertex3fv(vertices_cube[vertex])
    glEnd()

def draw_sphere():
    """
    Рисует сферу, используя вершины из vertices_sphere и ребра из edges_sphere.
    """
    glBegin(GL_LINES)
    for edge in edges_sphere:
        for vertex in edge:
            glVertex3fv(vertices_sphere[vertex])
    glEnd()

def check_intersection_sphere_cube(radius):
    """
    Проверяет пересечение сферы с кубом.
    Возвращает True, если сфера пересекает куб, и False в противном случае.
    """
    for vertex in vertices_cube:
        distance = np.linalg.norm(np.array(vertex) - np.array((0, 0, 0)))
        if distance <= radius:
            return True
    return False

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    create_sphere_vertices()
    create_sphere_edges()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Вращение куба и сферы

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        glColor3f(0.5, 0.1, 1.0)
        draw_sphere()

        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(0.7, 0.0, 0.0)  # Сдвиг куба по оси X
        draw_cube()
        glPopMatrix()

        pygame.display.flip()#обновляет экран, отображая нарисованные объекты
        pygame.time.wait(10)#задерживает выполнение программы
        # на 10 миллисекунд для ограничения частоты обновления экрана.

if __name__ == "__main__":
    main()