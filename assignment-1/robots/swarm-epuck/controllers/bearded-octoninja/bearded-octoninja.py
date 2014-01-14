from controller import *   # controller comes with Webots


"""avoid obstacles"""

class BeardedOctoNinja(DifferentialWheels):



    def set_speed(self, speed):
        """moving either forward or backwards"""
        pass
    
    def accelerate(self, acceleration):
        """increment speed"""
        pass

    def stop(self):
        """stops the epuck"""
        pass 

    def set_rotation(self, rotations_speed):
        """ passing in rotationspeed and calculates speed on left/ and right wheel """
        pass

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
