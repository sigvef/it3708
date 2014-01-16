def wander(sensors, actuators):
    actuators.set_rotation_speed(0)
    actuators.set_speed(2000)


def avoid_objects(sensors, actuators):
    threshold = 250
    left_sensors = [sensor.getValue() for sensor in sensors.proximity[5:]]
    right_sensors = [sensor.getValue() for sensor in sensors.proximity[:3]]
    left_walls = max(sum(left_sensors), threshold)
    right_walls = max(sum(right_sensors), threshold)
    maximum = max(left_walls, right_walls) + 1
    actuators.set_rotation_speed((left_walls - right_walls) / maximum)


def converge(sensors, actuators):
    threshold = 0
    left_sensors = [sensor.getValue() for sensor in sensors.light[4:]]
    right_sensors = [sensor.getValue() for sensor in sensors.light[:4]]
    left_robots = max(sum(left_sensors), threshold)
    right_robots = max(sum(right_sensors), threshold)
    maximum = max(left_robots, right_robots) + 1
    if left_robots + right_robots > 100:
        actuators.set_rotation_speed((left_robots - right_robots) / maximum)


def retrieve(sensors, actuators):
    pass


def realign(sensors, actuators):
    pass


def reposition(sensors, actuators):
    pass
