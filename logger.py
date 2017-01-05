import RPi.GPIO as GPIO
from IMU import read_euler, read_temp, read_gyro, read_accel
from ultra import get_distance
import time

def data_save(data, file='Data_Save'):
    import json
    print('Saving Dictionary to File')
    file += '.json'
    with open(file, 'w') as out_file:
        js = json.dumps(data)
        out_file.write(js)
    return None

data = []
n_data = 0
since_save = 0
print('Recording Data')

duration = 10000
save_interval = 10
tic = time.time()
toc = time.time()
save = time.time()

try:
    while toc-tic < duration:
        timestamp = time.time()
        dist = get_distance()
        heading, roll, pitch = read_euler()
        temp = read_temp()
        Gx, Gy, Gz = read_gyro()
        Ax, Ay, Az = read_accel()
        data.append({'Time':timestamp, 'Distance':dist, 'Heading':heading, 'Roll':roll, 'Pitch':pitch, 'Temp':temp, 'Gyro':[Gx, Gy, Gz], 'Accel':[Ax, Ay, Az]})
        n_data += 1
        toc = time.time()
        if toc - save > save_interval:
            save = time.time()
            data_save(data)
            print('Data Saved at {0}'.format(toc-tic))
        time.sleep(0.06)


    print('# data points={0} \n Gathered over {1}s \n Frequency: {2}Hz'.format(
              n_data, toc-tic, n_data/(toc-tic)))

    data_save(data)
    print('Data Saved')

except KeyboardInterrupt:
        print('N_data:{0}, {1}s of data at {2}Hz, last {3}s of data lost'.format(n_data, toc-tic, n_data/(toc-tic),toc-save))
finally:   
    GPIO.cleanup()
