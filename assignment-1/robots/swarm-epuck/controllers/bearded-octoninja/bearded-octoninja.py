from epuck import Epuck
from behaviours import wander, avoid_objects, \
    converge, retrieve, reposition, unstick


class BeardedOctoNinja(Epuck):

    def __init__(self):
        super(BeardedOctoNinja, self).__init__()
        self.behaviours = [
            wander,
            avoid_objects,
            converge,
            retrieve,
            reposition,
            unstick,
        ]

    def simulate(self):
        while self.step(1) != -1:
            for behaviour in self.behaviours:
                behaviour(self.sensors, self.actuators)


controller = BeardedOctoNinja()
controller.simulate()
