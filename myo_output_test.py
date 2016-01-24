import myo
import sys

m = myo.Myo(myo.NNClassifier(), sys.argv[1] if len(sys.argv) >= 2 else None)


def data_print(data):
        print (data)

m.add_raw_pose_handler(data_print)

m.connect()

while True:
    m.run()
