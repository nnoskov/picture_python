from graph import *


def motion(event):
    x, y = event.x, event.y
    # print('x-{}, y-{}'.format(x, y))


def callback(event):
    print('({},{}),'.format(event.x, event.y), end='')


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


# ring = [(338, 246), (174, 136), (153, 139), (160, 155), (247, 251), (396, 383), (439, 383), (451, 367), (377, 307),
#         (390, 333), (389, 346), (381, 334), (277, 236), (246, 207), (333, 250)]
# curved_polygon(ring, smooth=True, splinesteps=True)

# Ракета
def rocket_builder(pos_x: int, pos_y: int, scale):
    penColor('black')
    brushColor(int(204 * scale), int(204 * scale), int(scale * 204))
    # Верхняя часть ракеты
    head = [(-15, 22), (0, 0), (15, 22)]
    head_is_scalled = [(int(x * scale) + pos_x, int(y * scale) + pos_y) for (x, y) in head]
    polygon(head_is_scalled)

    # Нижняя часть ракеты
    nozzle = [(-25, 153), (0, 103), (25, 153)]
    nozzle_is_scalled = [(int(x * scale) + pos_x, int(y * scale) + pos_y) for (x, y) in nozzle]
    polygon(nozzle_is_scalled)

    # Центральная часть ракеты
    body = [(0, 22), (15, 22), (15, 131), (-15, 131), (-15, 22), (0, 22)]
    body_is_scalled = [(int((x * scale)) + pos_x, int((y * scale)) + pos_y) for (x, y) in body]
    polygon(body_is_scalled)

    # Иллюминаторы
    brushColor(int(153 * scale), int(153 * scale), int(153 * scale))
    penColor(int(72 * scale), int(72 * scale), int(72 * scale))
    porthole_y = int(40 * scale)

    for i in range(3):
        circle(pos_x, porthole_y + pos_y, int(10 * scale))
        porthole_y += int(30 * scale)


def flame_builder(pos_x: int, pos_y: int, scale: float):
    """Рисует пламя на основании одного полигона

    :param pos_x: Координата X верхнй точки пламени
    :param pos_y: Координата Y верхней точки пламени
    :param scale: Масштаб пламени (0 ~ 1.0)

    """
    penColor('black')
    mirror_scale = -60 * scale
    # Пламя Желтая часть
    flame_yellow = [(-2, -9), (13, 66), (30, 130), (50, 198),
                    (69, 247), (85, 277), (93, 294), (94, 294),
                    (64, 309), (28, 326), (0, 338), (-14, 342),
                    (-23, 337), (-27, 333), (-30, 323), (-30, 312),
                    (-27, 305), (-23, 291), (-18, 278), (-12, 255),
                    (-2, 213), (2, 163), (3, 116), (2, 71), (0, 31),
                    (-1, 1)]
    flame_yellow = [(int(x * scale), int(y * scale)) for (x, y) in flame_yellow]
    flame_yellow = [(x + pos_x, y + pos_y) for (x, y) in flame_yellow]

    brushColor(int(255 * scale), int(204 * scale), int(0 * scale))  # FFCC00
    curved_polygon(flame_yellow, smooth=True, splinesteps=True)

    # Пламя Желтая часть - Зеркальная
    flame_yellow_mirror = [(2 * pos_x + mirror_scale - x, y) for (x, y) in flame_yellow]
    curved_polygon(flame_yellow_mirror, smooth=True, splinesteps=True)

    # Пламя Оранжевая часть
    flame_orange = [(x + 9 * scale, y + 70 * scale) for (x, y) in flame_yellow]
    brushColor(int(scale * 255), int(scale * 102), int(scale * 0))  # FF6600
    curved_polygon(flame_orange, smooth=True, splinesteps=True)

    # Пламя Оранжевая часть - Зеркальная
    flame_orange_mirror = [(2 * pos_x + mirror_scale - x, y) for (x, y) in flame_orange]
    curved_polygon(flame_orange_mirror, smooth=True, splinesteps=True)

    # Пламя Красная часть
    flame_red = [(x + 24 * scale, y + 200 * scale) for (x, y) in flame_yellow]
    brushColor(int(scale * 255), int(scale * 0), int(scale * 0))  # FF0000
    curved_polygon(flame_red, smooth=True, splinesteps=True)

    # Пламя Красная часть - Зеркальная
    flame_red_mirror = [(2 * pos_x + mirror_scale - x, y) for (x, y) in flame_red]
    curved_polygon(flame_red_mirror, smooth=True, splinesteps=True)


# Космонавт
def astronaut_builder(axis):
    brushColor(153, 153, 153)
    penColor(153, 153, 153)
    oval(397, 412, 430, 465)  # Ось 412 тело
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


def pain_picture(scale: float = 1.0):
    rocket_builder(210, 50, scale * 0.5)
    flame_builder(224, 133, scale * 0.5)

    rocket_builder(478, 131, 0.2)
    flame_builder(484, 162, 0.2)

    rocket_builder(89, 66, scale)
    flame_builder(116, 238, scale)

    astronaut_builder(412)


# brushColor(120, 33, 33)
# penColor(120, 33, 33)
# arc(230, 55, 500, 281, 0, 360)

if __name__ == '__main__':
    mainWindow().bind("<Button>", callback)
    mainWindow().bind('<Motion>', motion)

    pain_picture(1)
    run()
