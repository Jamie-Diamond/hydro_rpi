import sys
import time

from Adafruit_BNO055 import BNO055

bno = BNO055.BNO055(rst=18)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))
sys, gyro, accel, mag = bno.get_calibration_status()
print('Sys_cal={0} Gyro_cal={1} Accel_cal={2} Mag_cal={3}'.format(
          sys, gyro, accel, mag))

def read_euler():
    # Read the Euler angles for heading, roll, pitch (all in degrees).
    heading, roll, pitch = bno.read_euler()
    return heading, roll, pitch

def read_temp():
    temp_c = bno.read_temp()
    return temp_c

def read_gyro():
    x,y,z = bno.read_gyroscope()
    return x, y, z

def read_accel():
    x,y,z = bno.read_accelerometer()
    return x, y, z
