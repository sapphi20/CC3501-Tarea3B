import glfw

from models.HistoricalData import HistoricalData


class Controller(object):
    def __init__(self):
        self.context = None
        self.data = HistoricalData()

    def on_key(self, window, key, scancode, action, mods):
        if action != glfw.PRESS:
            return
        elif key == glfw.KEY_ESCAPE:
            glfw.terminate()
        elif key == glfw.KEY_P:
            self.data.draw_plt()
        elif key == glfw.KEY_RIGHT:
            print("Día " + str(self.context.get_current_day()))
            print("Sanos: " + str(self.context.healthy_people()))
            print("Contagiados: " + str(self.context.sick_people()))
            print("Fallecidos: " + str(self.context.dead_people()))
            self.data.save_healthy(self.context.healthy_people())
            self.data.save_sick(self.context.sick_people())
            self.data.save_dead(self.context.dead_people())
            self.context.next_day()

    def set_context(self, cont):
        self.context = cont