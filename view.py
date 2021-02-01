import glfw  # Usada para interactuar con un usuario (mouse, teclado, etc)
import json
from OpenGL.GL import *  # importa las funciones de OpenGL
import numpy as np
import sys

from controller import Controller
from models.PopulationConditions import PopulationConditions
import utils.easy_shaders as es


if __name__ == "__main__":
    try:
        archivo = sys.argv[1]
        f = open(archivo, "r")
        data = json.load(f)[0]
        radio = data["Radius"]
        prob_contagio = data["Contagious_prob"]
        prob_muerte = data["Death_rate"]
        dias = data["Days_to_heal"]
        poblacion_ini = data["Initial_population"]
        f.close()

        glfw.init()

        width = 600
        height = 600
        window = glfw.create_window(width, height, "ContagionSim", None, None)

        glfw.make_context_current(window)

        ctrl = Controller()

        glfw.set_key_callback(window, ctrl.on_key)

        pipeline = es.SimpleTransformShaderProgram()

        glClearColor(0.9, 0.9, 0.9, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        scenario = PopulationConditions(
            radio, prob_contagio, prob_muerte, poblacion_ini, dias
        )
        ctrl.set_context(scenario)

        while not glfw.window_should_close(window):
            # Using GLFW to check for input events
            glfw.poll_events()

            # Clearing the screen in both, color and depth
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(pipeline.shaderProgram)
            scenario.draw_scene(pipeline)

            # Once the render is done, buffers are swapped, showing only the complete scene.
            glfw.swap_buffers(window)
    except Exception as e:
        print(e)
    finally:
        glfw.terminate()
        sys.exit()
