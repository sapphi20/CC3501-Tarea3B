import glfw
import json
import sys
from OpenGL.GL import *

from models.PopulationConditions import PopulationConditions
from controller import Controller
from utils import easy_shaders as es

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

        scenario = PopulationConditions(
            radio, prob_contagio, prob_muerte, poblacion_ini, dias
        )

        controlador = Controller()
        controlador.set_context(scenario)

        width = 800
        height = 600
        window = glfw.create_window(width, height, "ContagionSim", None, None)
        glfw.make_context_current(window)

        glfw.set_key_callback(window, controlador.on_key)

        pipeline = es.SimpleTransformShaderProgram()
        glClearColor(0, 0, 0, 0)
        while not glfw.window_should_close(window):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)
            glUseProgram(pipeline.shaderProgram)
            scenario.draw_scene(pipeline)

            glfw.swap_buffers(window)
    except Exception as e:
        print(e)
    finally:
        glfw.terminate()
        sys.exit()