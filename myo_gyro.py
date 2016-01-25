import myo
import sys

m = myo.Myo(myo.NNClassifier(), sys.argv[1] if len(sys.argv) >= 2 else None)


def data_print(quat, acc, gyro):
    if gyro[0] >= 0:
        print ("X = +")
    else:
        print ("X = -")

    if gyro[1] >= 0:
        print ("Y = +")
    else:
        print ("Y = -")

    if gyro[2] >= 0:
        print ("Z = +")
    else:
        print ("Z = -")
m.add_imu_handler(data_print)

m.connect()

while True:
    m.run()
