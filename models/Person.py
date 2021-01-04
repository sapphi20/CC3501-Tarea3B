import math
import random

import utils.basic_shapes as bs
import utils.easy_shaders as es
import utils.scene_graph as sg
import utils.transformations as tr

SANE = 0
SICK = 1
RECOVERED = 2
DEAD = 3


class Person(object):
    def __init__(self, radius, cont_prob, death_prob, days_recovery):
        self.contagious_prob = cont_prob
        self.death_prob = death_prob
        self.health_status = SANE
        self.radius = radius
        self.days_to_recover = days_recovery
        self.days_sick = 0

        gpu_person = es.toGPUShape(bs.createColorQuad(0, 0, 1))
        person = sg.SceneGraphNode('person')
        person.transform = tr.scale(0.1, 0.1, 0)
        person.childs = [gpu_person]

        self.x = round(random.uniform(-1, 1), 1)
        self.y = round(random.uniform(-1, 1), 1)

        self.model = person

    def get_status(self):
        return self.health_status

    def set_status(self, new_status):
        self.health_status = new_status

    def is_sick(self):
        return self.health_status == SICK

    def is_dead(self):
        return self.health_status == DEAD

    def is_healthy(self):
        return self.health_status == SANE or self.health_status == RECOVERED

    def has_recovered(self):
        return self.health_status == RECOVERED

    def while_sick(self):
        if self.is_sick() and random.random() < self.death_prob:
            self.set_status(DEAD)
        elif self.is_sick() and random.random() >= self.death_prob:
            if self.days_sick > self.days_to_recover:
                self.set_status(RECOVERED)
            else:
                self.days_sick += 1

    def update(self):
        self.x += random.random()
        self.y += random.random()
        self.while_sick()

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    # cuando self es el contagiado, other_person se puede contagiar o no
    def when_near_other(self, other_person):
        if (
            self.distance(other_person) < self.radius
            and other_person.is_healthy()
            and not other_person.has_recovered()
            and random.random() < self.contagious_prob
        ):
            other_person.set_status(SICK)
            self.days_sick += 1

    def draw(self, pipeline):
        self.model.transform = tr.translate(self.x, self.y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")
