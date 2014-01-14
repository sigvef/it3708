from controller import *   # controller comes with Webots
import time                # A Python primitive module
import math                #   "            "
import Image               # An extra Python module (that you'll have to download)
import imagepro            # A module provided by Keith Downing for this assignment


class BeardedOctoNinja(DifferentialWheels):

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
        self.setSpeed(1000 * left_wheel_speed,
                      1000 * right_wheel_speed)

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
        for i in range(self.num_dist_sensors):
            self.dist_sensor_values[i] = self.dist_sensors[i].getValue()
            return self.dist_sensor_values

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


controller = BeardedOctoNinja()
controller.basic_setup()
