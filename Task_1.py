from graph import *


def motion(event):
    x, y = event.x, event.y
    print('x-{}, y-{}'.format(x, y))


mainWindow().bind('<Motion>', motion)

# Размер базового окна 500 x 600 px

penColor('black')
brushColor(255, 255, 0)

circle(250, 300, 220)

# Черный рот
brushColor('black')
rectangle(150, 410, 355, 460)

brushColor('red')
circle(150, 255, 45)  # Левый глаз
brushColor('black')
circle(150, 255, 20)

brushColor('red')  # Правй глаз
circle(345, 260, 35)
brushColor('black')
circle(345, 260, 20)

penSize(24)
line(50, 124, 218, 230)
line(297, 230, 460, 155)

if __name__ == '__main__':
    run()
