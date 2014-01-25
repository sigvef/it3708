from controller import Supervisor
import random


class SimulationRunner(Supervisor):

    def __init__(self):
        super(SimulationRunner, self).__init__()
        self.foods = map(self.getFromDef, ['FOOD', 'FOOD2'])
        self.epucks = map(self.getFromDef,
                          ['epuck' + str(i) for i in range(7)])

    def reset_simulation(self):
        #self.simulationRevert()
        for item in self.foods + self.epucks:
            item.getField('translation').setSFVec3f([random.random() - 0.5,
                                                    0, random.random() - 0.5])
            item.getField('rotation').setSFRotation([0, 1, 0, random.random() *
                                                    3.141592])

    def is_food_pushed_to_wall(self, food_number):
        EDGE = 0.62
        x, _, y = self.foods[food_number].getPosition()
        return x > EDGE or x < -EDGE or y > EDGE or y < -EDGE

    def are_all_foods_pushed_to_wall(self):
        return False not in map(self.is_food_pushed_to_wall,
                                range(len(self.foods)))

    def simulate(self):
        self.reset_simulation()
        while self.step(1) != -1:
            if self.are_all_foods_pushed_to_wall():
                print self.getTime()
                self.reset_simulation()

simulation_runner = SimulationRunner()
simulation_runner.simulate()
