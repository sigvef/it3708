
def avoid_objects(sensors, actuators):
    threshold = 220
    left_sensors = sensors['proximity'][:4]
    right_sensors = sensors['proximity'][4:]
    left_walls = max(sum(left_sensors), threshold)
    right_walls = max(sum(right_sensors), threshold)
    maximum = max(left_walls, right_walls) + 1
    actuators['rotation_speed'] = (right_walls - left_walls) / maximum


def wander(sensors, actuators):
    actuators['rotation_speed'] = 0
    actuators['speed'] = 2000
