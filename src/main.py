from cobra import *
from math import radians

def main():
    wnd = Window("Flight Sim", Vector2(800, 600))

    aircraft = load_mesh("assets/models/aircraft.obj")
    ground = load_mesh("assets/models/plane.obj")
    lit = Shader("assets/shaders/unlit.vert", "assets/shaders/unlit.frag")

    camera = Camera(wnd, radians(60), 1, 100)

    ground_trans = Transform()
    ground_trans.position.y -= 50
    ground_trans.scale *= 100000

    aircraft_trans = Transform()
    aircraft_trans.position.z = -8

    lightPos = Vector3(-100, 1000, 1000)
    lightColor = Vector3(1, 1, 1)

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        aircraft_trans.rotation.y += dt

        wnd.clear(Vector3(135/255, 206/255, 235/255))

        lit.use()

        lit.pass_mat4("mvp", camera.get_mvp(ground_trans))
        lit.pass_vec3("fragColor", Vector3(1/255, 50/255, 32/255))
        ground.draw()

        lit.pass_mat4("mvp", camera.get_mvp(aircraft_trans))
        lit.pass_vec3("fragColor", Vector3(1, 1, 1))
        aircraft.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()