import scipy.io.wavfile as wav
from matplolib import pyplot as plt
fs,data=wave.read('my voice.wav')
print(fs,len(data))
plt.plot(x);plt.show
