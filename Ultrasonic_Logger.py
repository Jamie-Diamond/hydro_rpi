import RPi.GPIO as GPIO
from ultra import get_distance
import time

import signal

def handler(signum, frame):
    raise RuntimeError

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)



Distance = open('Distance.txt', 'a')
Distance.write('metadata: N/A\n')


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
        n_data = n_data + 1
        signal.alarm(1)
        try:
            dist = get_distance()
        except RuntimeError:
            print('Distance Read - TimeoutError')
        signal.alarm(1)
        try:
            temp = '[' + str(timestamp) + ', ' + str(dist) + ']\n'
            Distance.write(temp)
        except RuntimeError:
            print('Distance Write - TimeoutError')
        signal.alarm(1)
        
        if toc - update > Update_interval:
            update = time.time()
            print('Time: {0}    Data points: {1}'.format(timestamp, toc-tic))
        # time.sleep(0.04)
    print('# data points={0} \n Gathered over {1}s \n Frequency: {2}Hz'.format(
              n_data, toc-tic, n_data/(toc-tic)))
    print('Data Saved')

except KeyboardInterrupt:
        toc = time.time()
        print('N_data:{0}, {1}s of data at {2}Hz'.format(n_data, toc-tic, n_data/(toc-tic)))
finally:
    GPIO.cleanup()
    Distance.close()

