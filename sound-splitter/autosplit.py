import subprocess, json, sys, random, time, os, re
import os.path
from datetime import datetime, timedelta

def checkFileCreated(filename):
    try:
        with open(splitFilepath + filename) as f:
            # print("File exists")
            return True
    #     # Do something with the file
    except IOError:
        print("Split files do not exist")
        return False

def check_files(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

def songsplit(sourcePath, sourceFilename):
    command = ('spleeter separate -i %s -o audio_output' % sourcePath)
    splitFiles2stem = ['vocals.wav', 'accompaniment.wav', 'bass.wav', 'drums.wav', 'piano.wav']
    splitFolder = sourceFilename.split(".")[0].strip(" ")
    for each in splitFiles2stem:
        if check_file(each):
            print(each + " file exists")
        else:
            break
            p = os.system(command)

    for filename in splitFiles2stem:
        check_files(filename, outPath, sourcePath)

filepath = os.getcwd() + "\\"

configFile = "splitConfig.txt"
configs = []
with open(filepath + configFile) as cFile:
    for c in cFile:
        entry = c.split('=',1)
        entry0 = entry[1].replace('\n','')
        entry[1] = entry0
        configs.append(entry)
config = (dict(configs))

#setting appropriate variables to their counterparts in config file
originalAudio = config['originalAudio'].strip(" ")
splitType = config['splitType'].strip(" ")
splitFolder = originalAudio.split(".")[0].strip(" ")

print(originalAudio, splitType)

command = ('spleeter separate -i %s -o audio_output' % originalAudio)

splitFilepath = filepath + "audio_output\\" + splitFolder + "\\"
print(splitFilepath)
splitFiles2stem = ['vocals.wav', 'accompaniment.wav']

for each in splitFiles2stem:
    if checkFileCreated(each):
        print(each + " file exists")
    else:
        break
        p = os.system(command)
# p.wait(10)

for each in splitFiles2stem:
    print(each + "")
    if checkFileCreated(each):
        print(each + " file exists")

        s = open(filepath + 'splitFilePaths.txt')
        editFile = s.readlines()
        editFile[0] = 'vocal=' + splitFilepath + 'vocals.wav' + '\n'
        editFile[1] = 'accompaniment=' + splitFilepath + 'accompaniment.wav'
        s.close()
        s = open(filepath + 'splitFilePaths.txt', "w")
        s.writelines(editFile)
        s.close()
