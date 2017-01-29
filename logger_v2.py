import RPi.GPIO as GPIO
from IMU import read_euler, read_temp, read_gyro, read_accel
from ultra import get_distance
import time

Distance = open('Distance.txt', 'a')
Distance.write('metadata:____________\n')

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

duration = 10000
Update_interval = 10
tic = time.time()
toc = time.time()
update = time.time()

try:
    while toc-tic < duration:
        timestamp = time.time()
        dist = get_distance()
        temp = '[', str(timestamp), ', ', str(dist), ']\n'
        Distance.write(temp)

        heading, roll, pitch = read_euler()
        temp = '[', str(timestamp), ', ', str(heading), ']\n'
        Heading.write(temp)

        temp = '[', str(timestamp), ', ', str(roll), ']\n'
        Roll.write(temp)

        temp = '[', str(timestamp), ', ', str(pitch), ']\n'
        Pitch.write(temp)

        temperature = read_temp()
        temp = '[', str(timestamp), ', ', str(temperature), ']\n'
        Temp.write(temp)

        Gx, Gy, Gz = read_gyro()
        temp = '[', str(timestamp), ', ', '[', str(Gx), ', ', str(Gy), ', ', str(Gz), ']', ']\n'
        Gyro.write(temp)

        Ax, Ay, Az = read_accel()
        temp = '[', str(timestamp), ', ', '[', str(Ax), ', ', str(Ay), ', ', str(Az), ']', ']\n'
        Accel.write(temp)

        n_data += 1
        toc = time.time()
        if toc - update > Update_interval:
            update = time.time()
            print('Time: {0}    Data points: {1}'.format(timestamp, toc-tic))
        time.sleep(0.06)


    print('# data points={0} \n Gathered over {1}s \n Frequency: {2}Hz'.format(
              n_data, toc-tic, n_data/(toc-tic)))
    print('Data Saved')

except KeyboardInterrupt:
        toc = time.time()
        print('N_data:{0}, {1}s of data at {2}Hz'.format(n_data, toc-tic, n_data/(toc-tic)))
finally:
    GPIO.cleanup()
    Distance.close()
    Heading.close()
    Roll.close()
    Pitch.close()
    Temp.close()
    Gyro.close()
    Accel.close()

