import myo
import sys
import uarm

class MyoUArm(uarm.UArm):
    myo_band = None

    def __init__(self):
        self.myo_band = myo.Myo(myo.NNClassifier(), sys.argv[1] if len(sys.argv) >= 2 else None)
        self.myo_band.add_imu_handler(self.position_control)
        self.myo_band.add_raw_pose_handler(self.pose_control)

        self.myo_band.connect()

    def position_control(self, quat, acc, gyro):
        self.arm.set_position(gyro[0], gyro[1], gyro[2])

    def pose_control(self, pose):
        print (pose)

    def run(self):
        myo_band.run()


myo_arm = myoUArm()


while True:
    myo_arm.run()
