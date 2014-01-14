from controller import *   # controller comes with Webots

class BeardedOctoNinja(DifferentialWheels):

    def continuous_run(self):
        self.setSpeed(-1000, 1000)

controller = BeardedOctoNinja()
controller.continuous_run()
