import os
from distutils.dir_util import copy_tree

from PyQt5 import QtWidgets
from UI import conductify_gui
import sys
from PyQt5.QtCore import QTimer
from musicManager import octave
from musicManager import autosplitr
import pygame
import serial

pygame.mixer.init()
pygame.init()

oct = octave.Octave()
ser = serial.Serial('COM3', baudrate=115200, timeout=1)
wav_list = ["other.wav", "drums.wav", "piano.wav", "bass.wav", "vocals.wav"]

non_select = """
    QProgressBar {
        border: 6px solid grey;
        border-radius: 7px;

    }
    QProgressBar::chunk {
        background-color: #0064c8
    }
"""

select = """
    QProgressBar {
        border: 6px solid grey;
        border-radius: 7px;

    }
    QProgressBar::chunk {
        background-color: red
    }
"""

sound_arr = []


def start():
    for i in range(5):
        print(sound_arr[i])
        sound_arr[i].play()


def stop():
    if sound_arr:
        for i in range(5):
            sound_arr[i].stop()


def reload():
    global sound_arr
    stop()
    sound_arr = []
    pygame.mixer.set_num_channels(26)
    for wav in wav_list:
        print('music/' + wav)
        sound_arr.append(pygame.mixer.Sound('music/' + wav))

reload()

app = QtWidgets.QApplication(sys.argv)
main_window_Qdialog = QtWidgets.QDialog()
ui = conductify_gui.Ui_Form()
ui.setupUi(main_window_Qdialog)
main_window_Qdialog.show()


def read_ser(port):
    port.write(b'.')
    data_raw = port.readline().decode().strip()
    num_arr = []
    if data_raw:
        arr = data_raw.split(', ')
        for i in range(len(arr)):
            num_arr.append(float(arr[i]))
        return num_arr


def change_bar_color(num):
    ui.otherBar.setStyleSheet(non_select)
    ui.otherBar.setProperty("value", sound_arr[0].get_volume()*100)

    ui.drumsBar.setStyleSheet(non_select)
    ui.drumsBar.setProperty("value", sound_arr[1].get_volume()*100)

    ui.pianoBar.setStyleSheet(non_select)
    ui.pianoBar.setProperty("value", sound_arr[2].get_volume()*100)

    ui.bassBar.setStyleSheet(non_select)
    ui.bassBar.setProperty("value", sound_arr[3].get_volume()*100)

    ui.vocalsBar.setStyleSheet(non_select)
    ui.vocalsBar.setProperty("value", sound_arr[4].get_volume()*100)

    if num == 0:
        ui.otherBar.setStyleSheet(select)
    elif num == 1:
        ui.drumsBar.setStyleSheet(select)
    elif num == 2:
        ui.pianoBar.setStyleSheet(select)
    elif num == 3:
        ui.bassBar.setStyleSheet(select)
    elif num == 4:
        ui.vocalsBar.setStyleSheet(select)


def control_volume():
    control = read_ser(ser)

    if control is not None:
        change_bar_color(int(control[2]))
        if control[0] == 1:
            if not control[2] == 255:
                sound_arr[int(control[2])].set_volume(control[1])
                print(control)
            else:
                print("Out of Range")


def search_music():
    filename, songtitle = oct.getSongs(ui.searchInput.toPlainText())
    filename2 = filename.split("//")[1]
    print(filename2, songtitle)
    splitter = autosplitr.Autosplitr('music/', filename2)
    print("spath: " + splitter.s_path)

    vocal_files = ['vocals.wav', 'bass.wav', 'drums.wav', 'piano.wav', 'other.wav']
    if os.path.exists(splitter.s_path):
        os.remove(splitter.s_path)

    print(os.path.exists(splitter.s_path))
    if filename == '':
        print('Song not found. Try again')
        return 1
    splitter.split()

    for file in vocal_files:
        if os.path.isfile('music/' + file):
            os.remove('music/' + file)

    print("spath: splitter.s_path: " + splitter.s_path)
    copy_tree(splitter.s_path, 'music')

    reload()
    start()
    return 0


main_window_Qdialog.qTimer = QTimer()
main_window_Qdialog.qTimer.setInterval(1)
main_window_Qdialog.qTimer.timeout.connect(control_volume)

main_window_Qdialog.qTimer.start()
ui.start_pushButton.clicked.connect(start)
ui.search.clicked.connect(search_music)
ui.stop_pushButton.clicked.connect(stop)

sys.exit(app.exec_())