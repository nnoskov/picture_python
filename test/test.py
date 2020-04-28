from graph import *


def curved_polygon(points, **polygon_opts):
    _C = canvas()
    coord = unpackCoord(points)
    if points[0] != points[-1]:
        points.append(points[0])
    tk_opts = {"outline": penColor(),
               "width": penSize(),
               "fill": brushColor()}
    for _key in ["smooth", "splinesteps"]:
        if _key in polygon_opts.keys():
            tk_opts[_key] = polygon_opts[_key]
    plg = _C.create_polygon(*coord, tk_opts)
    return plg


if __name__ == '__main__':
    windowSize(800, 400)
    canvasSize(800, 400)
    mainWindow()
    curved_polygon([(0, 0),
                    (100, 0),
                    (300, 200),
                    (400, 200),
                    (600, 0),
                    (700, 0),
                    (700, 100),
                    (400, 200),
                    (400, 300)
                    ], smooth=True, )
    run()
