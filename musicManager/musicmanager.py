from autosplitr import autosplitr
from octave import Octave


x = Octave()
filename, song_title = x.getSongs("kiss with a fist")
print(song_title)
y = autosplitr('', filename)
y.split()
