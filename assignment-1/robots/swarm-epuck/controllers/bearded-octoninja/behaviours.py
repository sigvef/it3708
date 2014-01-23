import random


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
    if left_robots + right_robots > 10000:
        actuators.set_rotation_speed((left_robots - right_robots) / maximum)


def retrieve(sensors, actuators):
    front_light_sensors = sum([sensor.getValue()
                               for sensor in [sensors.light[0]] +
                               [sensors.light[7]]])
    threshold = 250
    left_sensors = [sensor.getValue() for sensor in sensors.proximity[5:]]
    right_sensors = [sensor.getValue() for sensor in sensors.proximity[:3]]
    left_walls = max(sum(left_sensors), threshold)
    right_walls = max(sum(right_sensors), threshold)
    maximum = max(left_walls, right_walls) + 1
    if front_light_sensors < 6000:
        actuators.set_rotation_speed((right_walls - left_walls) / maximum)


def reposition(sensors, actuators):
    front_sensors = sum([sensor.getValue()
                         for sensor in [sensors.proximity[0]] +
                         [sensors.proximity[7]]])
    side_sensors = sum([sensor.getValue()
                        for sensor in [sensors.proximity[2],
                                       sensors.proximity[5]]])

    if front_sensors > 6000:
        timer = max(side_sensors, 1) ** 0.9
        while timer > 0:
            timer -= 1
            retrieve(sensors, actuators)
            sensors.epuck.step(1)
        actuators.set_speed(-2000)
        actuators.set_rotation_speed((random.random() - 0.5) / 10)
        timer = 10
        while timer > 0:
            timer -= 1
            sensors.epuck.step(1)
        timer = 30
        while timer > 0:
            timer -= 1
            wander(sensors, actuators)
            avoid_objects(sensors, actuators)
            sensors.epuck.step(1)
