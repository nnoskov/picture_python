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
polygon([(75, 72), (90, 50), (105, 72)])
polygon([(65, 210), (90, 155), (115, 210)])
rectangle(75, 72, 105, 185)  # ось 90
brushColor(153, 153, 153)
penColor(72, 72, 72)
porthole_y = 0

# Иллюминаторы
for i in range(3):
    circle(90, porthole_y + 90, 10)
    porthole_y += 30

# Пламя
brushColor(255, 204, 0)
penSize(1)
penColor(255, 204, 0)

curved_polygon(
    [(117, 234), (132, 309), (149, 373), (169, 441),
     (188, 490), (204, 520), (212, 537), (213, 537),
     (183, 552), (147, 569), (119, 581), (105, 585),
     (96, 580), (92, 576), (89, 566), (89, 555),
     (92, 548), (96, 534), (101, 521), (107, 498),
     (117, 456), (121, 406), (122, 359), (121, 314),
     (119, 274), (118, 244)], smooth=True, splinesteps=True)

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
