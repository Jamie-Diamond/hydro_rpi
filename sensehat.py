from sense_emu import SenseHat
import matplotlib.pyplot as plt

sense = SenseHat()

sense.show_message("Hello my name is JD!!")


p = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    p.remove(0)
    p.append(pitch)
    r.remove(0)
    r.append(roll)
    y.remove(0)
    y.append(yaw)
    plt.plot(p)
    plt.plot(r)
    plt.plot(y)
    plt.show()
