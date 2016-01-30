import pygame
import pygame_cursor
import myo
import myo_raw
import sys
import math
import mathutils

class MyoCursor(pygame_cursor.Cursor):
    myo_band = None

    pose = None
    pose_raw = None
    previous_pose = None

    acc = (0, 0, 0)
    gyro = (0, 0, 0)

    quat_raw = mathutils.Quaternion((0, 0, 0, 0))
    quat = mathutils.Quaternion((0, 0, 0, 0))
    quat_reference = mathutils.Quaternion((0, 0, 0, 0))

    euler_reference = mathutils.Euler()
    euler_center = mathutils.Euler()

    x_angle = 0
    y_angle = 0
    left_angle = -1

    monitor_width_inches = 19
    monitor_height_inches = 10.5

    user_distance_inches = 0

    pixels_per_inch = 100

    def __init__(self, radius):
        self.position = (0, 0)
        super().__init__(self.position, radius)

        self.myo_band = myo.Myo(myo.NNClassifier(), sys.argv[1] if len(sys.argv) >= 2 else None)
        self.myo_band.add_imu_handler(self.set_imu)
        self.myo_band.add_raw_pose_handler(self.set_pose)

        self.myo_band.connect()

    def run(self):
        self.myo_band.run()

    def update(self, surface):
        self.previous_pose = self.pose
        self.pose = self.pose_raw
        self.user_distance_inches = (self.monitor_width_inches / 2) / math.tan(abs(self.left_angle))
        self.user_distance_inches = 45

        self.set_x(int(self.user_distance_inches * math.tan(self.x_angle) * self.pixels_per_inch * -1 + surface.get_width() / 2))

        self.set_y(int(self.user_distance_inches * math.tan(self.y_angle) * self.pixels_per_inch * -1 + surface.get_height() / 2))

        print(self.position)

        super().update(surface)

    def set_pose(self, pose):
        self.pose_raw = pose

    def set_imu(self, quat, acc, gyro):
        self.quat_raw = mathutils.Quaternion(quat)
        self.acc = acc
        self.gyro = gyro
        self.quat = self.quat_raw.copy()
        #self.quat.rotate(self.quat_center)

        self.x_angle = self.quat.to_euler()[0] - self.euler_center[0]
        self.y_angle = self.quat.to_euler()[1] - self.euler_center[1]

    def set_center(self):
        self.euler_center = self.quat.to_euler()

    def set_reference(self):
        self.euler_reference = self.quat.to_euler()
        #self.quat_center = self.quat.inverted()
        #print("Center set at", self.quat)

    def calibrate(self):
        self.left_angle = self.x_angle

    def pose_clicked(self, pose):
        if self.pose is pose and self.previous_pose is not pose:
            return True
        return False

    def pose_held(self, pose):
        if self.pose is pose and self.pose_clicked(pose) is False:
            return True
        return False

    def pose_released(self, pose):
        if self.pose is not pose and self.previous_pose is pose:
            return True
        return False

    def get_actions(self):
        actions_list = []

        if self.pose_clicked(myo_raw.Pose.FIST):
            actions_list.append("click_1")
        if self.pose_released(myo_raw.Pose.FIST):
            actions_list.append("release_1")
        if self.pose_held(myo_raw.Pose.FIST):
            actions_list.append("hold_1")
        if self.pose_held(myo_raw.Pose.THUMB_TO_PINKY):
            actions_list.append("myo_set_center")
        if self.pose_held(myo_raw.Pose.WAVE_IN):
            actions_list.append("myo_calibrate")

        return actions_list


