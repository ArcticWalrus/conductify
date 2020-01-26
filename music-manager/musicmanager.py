from autosplitr import autosplitr
from octave import Octave


x = Octave()
filename, song_title = x.getSongs("hello")
print(song_title)
y = autosplitr('music', filename)
y.split()
