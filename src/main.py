from cobra import *
from math import radians

def main():
    wnd = Window("Flight Sim", Vector2(800, 600))

    cube = load_mesh("assets/models/cube.obj")
    lit = Shader("assets/shaders/lit.vert", "assets/shaders/lit.frag")

    camera = Camera(wnd, radians(60), 1, 100)
    camera.transform.position.z = -5

    plane_trans = Transform()
    plane_trans.scale.x = 2

    lightPos = Vector3(-10, 1000, 0)

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        wnd.clear(Vector3(135/255, 206/255, 235/255))

        lit.use()
        lit.pass_mat4("mvp", camera.get_mvp(plane_trans))
        lit.pass_mat4("model", plane_trans.get_trans_matrix())
        lit.pass_vec3("lightPos", lightPos)
        lit.pass_vec3("viewPos", camera.transform.position),
        lit.pass_vec3("lightColor", Vector3(1, 1, 1))
        lit.pass_vec3("fragColor", Vector3(1, 1, 1))
        cube.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()