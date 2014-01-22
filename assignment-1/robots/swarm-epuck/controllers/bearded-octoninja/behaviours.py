import imagepro
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

    front_sensors = [sensor.getValue() for sensor in [sensors.proximity[0], sensors.proximity[7]]];

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
    threshold = 0
    left_sensors = [sensor.getValue() for sensor in sensors.light[4:]]
    right_sensors = [sensor.getValue() for sensor in sensors.light[:4]]

    front_sensors = [sensor.getValue() for sensor in [sensors.proximity[0], sensors.proximity[7]]];

    left_robots = max(sum(left_sensors), threshold)
    right_robots = max(sum(right_sensors), threshold)


    if left_robots + right_robots > 10000 and sum(front_sensors) > 800:
        sensors.epuck.turn_on_pushingleds()
    else:
        sensors.epuck.turn_off_pushingleds()

    # threshold = 0
    # img = sensors.get_image()
    # list = imagepro.columns_max_spikes_green(img, band="green").tolist()
    # left = sum(map(lambda x: 178 if x == 178 else 0,list[26:])) or 1
    # right = sum(map(lambda x: 178 if x == 178 else 0,list[:26])) or 1
    # front_sensors = [sensor.getValue() for sensor in [sensors.proximity[0], sensors.proximity[7]]];
    # if left > right:
    #     actuators.set_rotation_speed(-0.5)

    # elif left < right:
    #     actuators.set_rotation_speed(0.5)

    
def realign(sensors, actuators):
    pass


def reposition(sensors, actuators):
    # front_sensors = [sensor.getValue() for sensor in [sensors.proximity[0], sensors.proximity[7]]]
    # accelerometer = sensors.accelerometer
    # values = accelerometer.getValues()
    # if (sum(front_sensors) > 800 and (values[0] + values[1]) < 0.05):
    #     if (random.random() < 0.05):
    #         while(sensors.epuck.step(64) < 100):
    #             avoid_objects(sensors, actuators)
    # pass



