import serial
import io


def getVals(port, baud):
    active = False
    channel = 0
    volume = 0.0

    ser = serial.Serial(port, baudrate=9600, timeout=1)

    ser.write('h')

    last_received = ''
    buffer_string = ''
    for i in range(100):
        buffer_string = buffer_string + ser.read(ser.in_waiting)

        if '\n' in buffer_string:
            lines = buffer_string.split('\n')  # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            break

    print(last_received)

    if len(last_received):
        strings = last_received.split(',')

        active = strings[0] == '1'
        volume = float(strings[1])
        channel = int(strings[2])

    ser.close()
    print(active, channel, volume)

    return active, channel, volume


getVals(12, 12)