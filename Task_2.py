from graph import *


def motion(event):
    x, y = event.x, event.y
    # print('x-{}, y-{}'.format(x, y))


def callback(event):
    print('({},{}),'.format(event.x, event.y), end='')


mainWindow().bind("<Button>", callback)
mainWindow().bind('<Motion>', motion)

# Сатурн
penColor('white')
brushColor(85, 0, 0)
rectangle(0, 0, 500, 600)
penColor('black')
brushColor('black')
rectangle(0, 0, 500, 300)
penColor(170, 136, 0)
brushColor(170, 136, 0)
circle(378, 176, 80)

# Ракета
penColor('black')
brushColor(204, 204, 204)
polygon([(60, 72), (75, 50), (90, 72)])
polygon([(50, 210), (75, 155), (100, 210)])
rectangle(60, 72, 90, 185)  # ось 75
brushColor(153, 153, 153)
penColor(72, 72, 72)
porthole_y = 0

# Иллюминаторы
for i in range(3):
    circle(75, porthole_y + 90, 10)
    porthole_y += 30

# Пламя
brushColor(255, 204, 0)
penColor('black')
# polygon([(99, 227), (117, 309), (127, 356),
#          (141, 412), (159, 467), (179, 516),
#          (195, 551), (100, 588), (85, 586),
#          (76, 578), (72, 565), (70, 555),
#          (71, 546), (74, 535), (77, 525),
#          (92, 456), (96, 412), (97, 353),
#          (100, 297), (100, 252), (100, 230)
#          ])
# Космонавт
brushColor(153, 153, 153)
penColor(153, 153, 153)
oval(397, 412, 430, 465)  # Ось 415 тело
axis = 412
circle(415, 406, 13)  # Голова

oval(415, 455, 430, 490)  # Нога_1
oval(413, 480, 430, 508)  # Нога_2
oval(416, 511, 440, 500)  # Нога_3
circle(427, 422, 7)  # Рука_1
circle(436, 425, 6)  # Рука_2
circle(443, 432, 5)  # Рука_3

oval(axis - (415 - axis), 455, axis - (430 - axis), 490)  # Нога_1
oval(axis - (413 - axis), 480, axis - (430 - axis), 508)  # Нога_2
oval(axis - (416 - axis), 511, axis - (440 - axis), 500)  # Нога_3
circle(axis - (427 - axis), 422, 7)  # Рука_1
circle(axis - (436 - axis), 425, 6)  # Рука_2
circle(axis - (443 - axis), 432, 5)  # Рука_3

brushColor('black')
penColor('black')
oval(405, 395, 427, 412)
# brushColor(120, 33, 33)
# penColor(120, 33, 33)
# arc(230, 55, 500, 281, 0, 360)

if __name__ == '__main__':
    run()
