import random

from .Person import Person


class PopulationConditions(object):
    def __init__(self, radius, cont_prob, death_rate, init_pop, days_to_heal):
        self.radius = radius
        self.contagious_prob = cont_prob
        self.death_rate = death_rate
        self.pop = init_pop
        self.heal = days_to_heal
        self.list_people = self.list_of_people()
        self.current_day = 0

    def list_of_people(self):
        people = [
            Person(self.radius, self.contagious_prob, self.death_rate, self.heal)
            for i in range(self.pop)
        ]
        rand_index = random.randint(0, self.pop-1)
        people[rand_index].set_status(1)
        return people

    def healthy_people(self):
        count = 0
        for p in self.list_people:
            if p.is_healthy():
                count += 1
        return count

    def sick_people(self):
        count = 0
        for p in self.list_people:
            if p.is_sick():
                count += 1
        return count

    def dead_people(self):
        count = 0
        for p in self.list_people:
            if p.is_dead():
                count += 1
        return count

    def recovered_people(self):
        count = 0
        for p in self.list_people:
            if p.has_recovered():
                count += 1
        return count

    def contagion_process(self):
        copy = tuple(self.list_people)
        for i in range(len(copy)):
            current = self.list_people[i]
            if current.is_sick():
                for other in range(len(copy)):
                    current.when_near_other(self.list_people[other])

    def next_day(self):
        self.set_current_day(self.get_current_day() + 1)
        for p in self.list_people:
            self.contagion_process()
            p.update()

    def get_current_day(self):
        return self.current_day

    def set_current_day(self, num):
        self.current_day = num

    def draw_scene(self, pipeline):
        for p in self.list_people:
            p.draw(pipeline)