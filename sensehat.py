from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Hello my name is JD!!")



while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    print("pitch={0}, roll={1}, yaw={}\n".format(pitch,yaw,roll))

