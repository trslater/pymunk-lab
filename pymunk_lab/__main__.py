import pyglet
from pyglet.window import Window
from pymunk import Body, Poly, Space
from pymunk.pyglet_util import DrawOptions


def init():
    window = Window(800, 600, "Marble Addition")
    options = DrawOptions()

    space = Space()
    space.gravity = 0, -1000

    body = Body(1, 1500)
    body.position = 50, 100
    poly = Poly.create_box(body)

    space.add(body, poly)

    @window.event
    def on_draw():
        window.clear()
        space.debug_draw(options)

    def update(dt):
        space.step(dt)

    return update


def main():
    update = init()

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()


if __name__ == "__main__":
    main()
