import RPi.GPIO as GPIO
from IMU import read_euler, read_temp, read_gyro, read_accel, get_cal
import time



import signal

def handler(signum, frame):
    raise RuntimeError

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)

Heading = open('Heading.txt', 'a')
Heading.write('metadata:____________\n')

Roll = open('Roll.txt', 'a')
Roll.write('metadata:____________\n')

Pitch = open('Pitch.txt', 'a')
Pitch.write('metadata:____________\n')

Temp= open('Temp.txt', 'a')
Temp.write('metadata:____________\n')

Gyro = open('Gyro.txt', 'a')
Gyro.write('metadata:____________\n')

Accel = open('Accel.txt', 'a')
Accel.write('metadata:____________\n')

data = []
n_data = 0
since_save = 0
print('Recording Data')

duration = 100000000
Update_interval = 60
tic = time.time()
toc = time.time()
update = time.time()

try:
    while toc-tic < duration:
        timestamp = time.time()
        signal.alarm(1)
        try:
            heading, roll, pitch = read_euler()
        except RuntimeError:
            print('read_euler - TimeoutError')
        signal.alarm(1)
        try:
            temp = '[' + str(timestamp) + ', ' + str(heading) + ']\n'
            Heading.write(temp)
        except RuntimeError:
            print('Heading Write - TimeoutError')
        signal.alarm(1)
        try:
            temp = '[' + str(timestamp) + ', ' + str(roll) + ']\n'
            Roll.write(temp)
        except RuntimeError:
            print('Roll Write - TimeoutError')
        signal.alarm(1)
        try:
            temp = '[' + str(timestamp) + ', ' + str(pitch) + ']\n'
            Pitch.write(temp)
        except RuntimeError:
            print('Pitch Write - TimeoutError')
        signal.alarm(1)
        try:
            temperature = read_temp()
        except RuntimeError:
            print('read_temp - TimeoutError')
        signal.alarm(1)
        try:
            temp = '[' + str(timestamp) + ', ' + str(temperature) + ']\n'
            Temp.write(temp)
        except RuntimeError:
            print('Temp Write - TimeoutError')
        signal.alarm(1)
        try:
            Gx, Gy, Gz = read_gyro()
        except RuntimeError:
            print('read_gyro - TimeoutError')
        signal.alarm(1)
        try:
            temp = '[' + str(timestamp) + ', ' + '[' + str(Gx) + ', ' + str(Gy) + ', ' + str(Gz) + ']' + ']\n'
            Gyro.write(temp)
        except RuntimeError:
            print('Gyro Write - TimeoutError')
        signal.alarm(1)
        try:
            Ax, Ay, Az = read_accel()
        except RuntimeError:
            print('read_accel - TimeoutError')
        signal.alarm(1)
        try:
            temp = '[' + str(timestamp) + ', ' + '[' + str(Ax) + ', ' + str(Ay) + ', ' + str(Az) + ']' + ']\n'
            Accel.write(temp)
        except RuntimeError:
            print('Accel Write - TimeoutError')
        signal.alarm(0)
        n_data += 1
        toc = time.time()
        if toc - update > Update_interval:
            update = time.time()
            print('Time: {0}    Data points: {1}'.format(timestamp, toc-tic))
            sys, gyro, accel, mag = get_cal()
            print('Sys_cal={0} Gyro_cal={1} Accel_cal={2} Mag_cal={3}'.format(
                sys, gyro, accel, mag))
        time.sleep(0.09)

    print('# data points={0} \n Gathered over {1}s \n Frequency: {2}Hz'.format(
              n_data, toc-tic, n_data/(toc-tic)))
    print('Data Saved')

except KeyboardInterrupt:
        toc = time.time()
        print('N_data:{0}, {1}s of data at {2}Hz'.format(n_data, toc-tic, n_data/(toc-tic)))
finally:
    GPIO.cleanup()
    Heading.close()
    Roll.close()
    Pitch.close()
    Temp.close()
    Gyro.close()
    Accel.close()
