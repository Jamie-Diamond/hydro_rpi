from IMU import read_euler, read_temp, read_gyro, read_accel
from ultra import get_distance
import time

data = []
n_data = 0

print('Recording Data')

while n_data < 300:
    timestamp = time.time()
    dist = get_distance()
    heading, roll, pitch = read_euler()
    temp = read_temp()
    Gx, Gy, Gz = read_gyro()
    Ax, Ay, Az = read_accel()
    data.append({'Time':timestamp, 'Distance':dist, 'Heading':heading, 'Roll':roll, 'Pitch':pitch, 'Temp':temp, 'Gyro':[Gx, Gy, Gz], 'Accel':[Ax, Ay, Az]})
    n_data += 1
  

print('# data points={0}\n '.format(
          n_data))


def data_save(data, file='Data_Save'):
    import json
    print('Saving Dictionary to File')
    file += '.json'
    with open(file, 'w') as out_file:
        js = json.dumps(data)
        out_file.write(js)
    return None

data_save(data)

print('Data Saved')
