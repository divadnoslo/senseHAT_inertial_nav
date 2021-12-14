from sense_hat import SenseHat
# import numpy as np
import sensehat_imu_functions as imu
sense = SenseHat()

# test functions
imu_data = imu.read_imu(sense)

# accel
print("accel data: \n")
print(imu_data[0])

# gyro
print("gyro data: \n")
print(imu_data[1])

# magnetometer
print("mag data: \n")
print(imu_data[2])

# baro
print("baro data: \n")
print(imu_data[3])