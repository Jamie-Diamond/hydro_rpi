from sense_emu import SenseHat
import matplotlib.pyplot as plt
sense = SenseHat()

sense.show_message("He")


p = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

plt.figure(1)
while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    p.pop(0)
    p.append(pitch)
    r.pop(0)
    r.append(roll)
    y.pop(0)
    y.append(yaw)
    plt.cla()
    plt.plot(p)
    plt.plot(r)
    plt.plot(y)
    plt.pause(0.000000000001)





