import pygame
import serial

pygame.mixer.init()
pygame.init()

ser = serial.Serial('COM18', baudrate=115200, timeout=1)
wav_list = ["vocals.wav", "bass.wav", "drums.wav", "piano.wav", "other.wav"]


def read_ser(port):
    port.flushOutput()
    port.write(b'')
    data_raw = port.readline().decode().strip()
    num_arr = []
    if data_raw:
        arr = data_raw.split(', ')
        for i in range(len(arr)):
            num_arr.append(float(arr[i]))
        return num_arr


pygame.mixer.set_num_channels(26)

sound_arr = []
for wav in wav_list:
    sound_arr.append(pygame.mixer.Sound(wav))

for i in range(4):
    sound_arr[i].play()

while 1:
    control = read_ser(ser)
    if control is not None:
        if control[0] == 1:
            if not control[2] == 255:
                sound_arr[int(control[2])].set_volume(control[1])
                print(control)
            else:
                print("Out of Range")
