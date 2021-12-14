# Import Modules
from sense_hat import SenseHat
import numpy as np

# Define Accelerometer Read Function
def read_accel(sense):
    """ read_accel - reads and formats data from the accelerometer on the sensehat
        
        Inputs:
        sense - sensehat object
        
        Outputs:
        accel - 3x1 array in units of m/s^2
     """   
    
    # set value for acceleration due to gravity in Minot, ND
    g0 = 9.80772;

    # get raw acceleration measurement from accel
    accel_raw = sense.get_accelerometer_raw()
    
    # format accel in units of m/s^2 in a 3x1 array
    accel = np.array([[accel_raw['x']],
                      [accel_raw['y']],
                      [accel_raw['z']]]) * g0
    
    # return accel vector
    return accel

#---------------------------------------------------------------------------------------
# Define Gyroscope Read Function
def read_gyro(sense):
    """ read_gyro - reads and formats data from the gyroscope on the sensehat
        
        Inputs:
        sense - sensehat object
        
        Outputs:
        gyro - 3x1 array in units of rad/s
     """
    
    # get raw angular velocity measurement
    gyro_raw = sense.get_gyroscope_raw()
    
    # format gyro in units of rad/s in a 3x1 array
    gyro = np.array([[gyro_raw['x']],
                     [gyro_raw['y']],
                     [gyro_raw['z']]])
    
    # return gyro vector
    return gyro

#---------------------------------------------------------------------------------------
# Define Magnetometer Read Function
def read_mag(sense):
    """ read_mag - reads and formats data from the magnetometer on the sensehat
        
        Inputs:
        sense - sensehat object
        
        Outputs:
        mag - 3x1 array in units of micro-Tesla (a.k.a. 10^-6)
     """
     
    # read raw magnetometer values
    mag_raw = sense.get_compass_raw()
     
    # format mag in units of micro-Teslas in a 3x1 array
    mag = np.array([[mag_raw['x']],
                     [mag_raw['y']],
                     [mag_raw['z']]])
     
    # return mag vector
    return mag
    
#---------------------------------------------------------------------------------------
# Define Barometer Read Function
def read_baro(sense):
    """ read_baro - reads and formats data from the pressure_sensor on the sensehat
        
        Inputs:
        sense - sensehat object
        
        Outputs:
        baro - 1 float in units of kPa
     """
     
    # read raw pressure sensor values
    baro_raw = sense.get_pressure()
     
    # format mag in units of kila-Pascals in a single float value
    baro = baro_raw / 10.0
     
    # return baro
    return baro
     
#---------------------------------------------------------------------------------------
# Define Ful IMU Read Function
def read_imu(sense):
    """ read_imu - reads and formats data from the pressure_sensor on the sensehat
        
        Inputs:
        sense - sensehat object
        
        Outputs:
        A list containing in order:
        accel - 3x1 array in units of m/s^2
        gyro  - 3x1 array in units of rad/s
        mag   - 3x1 array in units of micro-Teslas
        baro  - 1 float in units of kPa
     """
    
    # Call all IMU functions
    accel = read_accel(sense)
    gyro = read_gyro(sense)
    mag = read_mag(sense)
    baro = read_baro(sense)
    
    # Define list to return
    imu_data = (accel, gyro, mag, baro)
    
    # return list
    return imu_data