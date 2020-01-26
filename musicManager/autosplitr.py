import subprocess, json, sys, random, time, os, re
from datetime import datetime, timedelta


class autosplitr:
    def __init__(self, input_path, ogfilename):  # name of original audio fiile, 2/4/5stem splitting
        self.input_path = input_path
        self.ogfilename = self.input_path + ogfilename
        self.ogfolder = ogfilename.split(".")[0]
        self.path = os.getcwd() + "\\"
        self.s_path = self.path + "audio_output\\" + self.ogfolder + "\\"
        self.voice = ""
        self.drums = ""
        self.bass = ""
        self.piano = ""
        self.other = ""

    def split(self):
        status = ""
        if self.checkFiles2Stem():
            status = "Already Split"
        else:
            command = ('spleeter separate -i \"%s\" -p spleeter:5stems -o audio_output' % self.ogfilename)
            os.system(command)
            self.voice = "voice.wav"
            self.drums = "drums"
            self.bass = "bass.wav"
            self.piano = "piano.wav"
            self.other = "other.wav"
            status = "Finished splitting."
        return status

    def checkFiles2Stem(self):
        return (os.path.isfile(self.s_path + "vocals.wav")
                and os.path.isfile(self.s_path + "drums.wav")
                and os.path.isfile(self.s_path + "bass.wav")
                and os.path.isfile(self.s_path + "piano.wav")
                and os.path.isfile(self.s_path + "other.wav")
                )
