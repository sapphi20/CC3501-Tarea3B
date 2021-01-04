import matplotlib.pyplot as plt

class HistoricalData(object):
    def __init__(self):
        self.healthy = []
        self.sick = []
        self.dead = []

    def get_healthy_hist(self):
        return self.healthy

    def get_sick_hist(self):
        return self.sick
        
    def get_dead_hist(self):
        return self.dead
    
    def save_healthy(self, data):
        self.healthy.append(data)
    
    def save_sick(self, data):
        self.sick.append(data)

    def save_dead(self, data):
        self.dead.append(data)

    def draw_plt(self):
        days = [x for x in range(len(self.get_healthy_hist()))]
        plt.plot(days, self.get_healthy_hist(), '-', label='Sanos')
        plt.plot(days, self.get_sick_hist(), '-', label='Contagiados')
        plt.plot(days, self.get_dead_hist(), '-', label='Muertos')
        plt.xlabel("Días")
        plt.ylabel("Número de personas")
        plt.legend()
        plt.show()
