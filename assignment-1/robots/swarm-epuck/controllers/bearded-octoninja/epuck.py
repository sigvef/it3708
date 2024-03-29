from controller import DifferentialWheels


class Sensors(object):

    def __init__(self, epuck):
        self.epuck = epuck
        self.proximity = [epuck.getDistanceSensor('ps' + str(x))
                          for x in range(8)]
        self.light = [epuck.getLightSensor('ls' + str(i)) for i in range(8)]
        for sensor in self.proximity + self.light:
            sensor.enable(int(epuck.getBasicTimeStep()/4))


class Actuators(object):
    def __init__(self, epuck):
        self.epuck = epuck

    def set_speed(self, speed):
        self.epuck.set_speed(speed)

    def set_rotation_speed(self, rotation_speed):
        self.epuck.set_rotation_speed(rotation_speed)


class Epuck(DifferentialWheels):

    def __init__(self):
        super(Epuck, self).__init__()
        self.enableEncoders(int(self.getBasicTimeStep()))
        self.sensors = Sensors(self)
        self.actuators = Actuators(self)
        self.speed = 0
        self.rotation_speed = 0

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
