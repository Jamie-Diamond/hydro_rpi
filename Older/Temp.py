import signal

def handler(signum, frame):
    raise TimeoutError

# This function *may* run for an indetermined time...
def loop_forever():
     import time
     for x in range(7):
         print("sec")
         time.sleep(0.5)


# Register the signal function handler
signal.signal(signal.SIGALRM, handler)


# Define a timeout for your function
signal.alarm(2)


try:
    loop_forever()
except TimeoutError:
    print('TimeoutError')


signal.alarm(2)


try:
    loop_forever()
except TimeoutError:
    print('TimeoutError')


signal.alarm(2)


try:
    loop_forever()
except TimeoutError:
    print('TimeoutError')

signal.alarm(0)