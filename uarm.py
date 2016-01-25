import numpy
import UArmForPython.uarm_python

class UArm:
    arm = None

    arm_x = 0
    arm_y = 0
    arm_z = 0

    arm_x_range = (-180, 180)
    arm_y_range = (-180, 180)
    arm_z_range = (-180, 180)

    def __init__(self, device):
        #self.arm = Uarm(device)
        #self.arm.uarmAttach()
        print ("Initializing")

    def go_to_origin(self):
        self.arm_x = 0
        self.arm_y = 0
        self.arm_z = 0
        #self.arm.moveTo(0, 0, 0)

    def set_position(self, x, y, z):
        self.arm_x = self.arm_x + x
        self.arm_y = self,arm_y + y
        self.arm_z = self.arm_z + z

        # Keeps the servos from trying to go beyond their range
        x_clipped = numpy.clip(arm_x, arm_x_range[0], arm_x_range[1])
        y_clipped = numpy.clip(arm_y, arm_y_range[0], arm_y_range[1])
        z_clipped = numpy.clip(arm_z, arm_z_range[0], arm_z_range[1])

        #self.arm.moveTo(x_clipped, y_clipped, z_clipped)
        print ((x_clipped, y_clipped, z_clipped))

    def set_gripper(self, value):
        print ("Setting gripper to", value)
        #Set the servo to close to value
        #TODO: Add a failsafe to get the servo to stop when already secure


