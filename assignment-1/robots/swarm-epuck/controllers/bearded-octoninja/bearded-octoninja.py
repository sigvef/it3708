from controller import *   # controller comes with Webots
import time                # A Python primitive module
import math                #   "            "
import Image               # An extra Python module (that you'll have to download)
import imagepro            # A module provided by Keith Downing for this assignment
from behaviours import wander, avoid_objects

class BeardedOctoNinja(DifferentialWheels):

    num_dist_sensors = 8

    def basic_setup(self, tempo = 1.0):
        self.timestep = int(self.getBasicTimeStep()) # Fetched from WorldInfo.basicTimeStep (in the Webots world)
        self.tempo = tempo
        self.enableEncoders(self.timestep)
        self.camera = self.getCamera('camera')
        self.camera.enable(4*self.timestep)
        print "Camera width: " , self.camera.getWidth()

        self.dist_sensor_values = [0 for i in range(self.num_dist_sensors)]
        self.dist_sensors = [self.getDistanceSensor('ps'+str(x)) for x in range(self.num_dist_sensors)]  # distance sensors
        map((lambda s: s.enable(self.timestep)), self.dist_sensors) # Enable all distance sensors
        self.speed = 0.0
        self.rotation_speed = 0.0


    #
    # Movement
    #

    def _update_wheel_speeds(self):
        left_wheel_speed = self.speed * (0.5 + self.rotation_speed)
        right_wheel_speed = self.speed * (0.5 - self.rotation_speed)
        if left_wheel_speed > 1000:
            ratio = 1000 / left_wheel_speed
            left_wheel_speed = 1000
            right_wheel_speed *= ratio
        if right_wheel_speed > 1000:
            ratio = 1000 / right_wheel_speed
            right_wheel_speed = 1000
            left_wheel_speed *= ratio
        self.setSpeed(left_wheel_speed,
                      right_wheel_speed)

    def set_speed(self, speed):
        self.speed = speed
        self._update_wheel_speeds()

    def set_rotation_speed(self, rotation_speed):
        self.rotation_speed = rotation_speed
        self._update_wheel_speeds()
    
    def accelerate(self, acceleration):
        self.set_speed(self.speed + acceleration)

    def stop(self):
        self.set_speed(0)
        self.set_rotation_speed(0)

    #
    # Sensors and Camera
    #

    # Returns proximities
    def get_proximities(self):
        return [sensor.getValue() for sensor in self.dist_sensors]

    # Returns parsed image
    def snapshot(self, show = False):
        im = self.get_image()
        if show: 
            im.show()
        return im

    # Delegate method
    def get_image(self):
        strImage=self.camera.getImage()
        im = Image.fromstring('RGB',(self.camera.getWidth(), self.camera.getHeight()), strImage)
        return im

    def get_sensors(self):
        sensors = {
            'proximity': self.get_proximities(),
        }
        return sensors

    def apply_actuators(self, actuators):
        self.set_speed(actuators['speed'])
        self.set_rotation_speed(actuators['rotation_speed'])

    #
    # Simulation loop
    #
    def simulate(self):
        while self.step(1) != -1:
            actuators = {}
            sensors = self.get_sensors()
            wander(sensors, actuators)
            avoid_objects(sensors, actuators)
            self.apply_actuators(actuators)


controller = BeardedOctoNinja()
controller.basic_setup()
controller.simulate()
