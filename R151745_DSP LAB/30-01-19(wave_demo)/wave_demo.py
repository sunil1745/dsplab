import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
fs,data=wav.read('my voice.wav')
fs1,data1=wav.read('my voice1.wav')
fs11,data11=wav.read('high_my voice.wav')
print(fs,fs1)
t1=np.arange(0,len(data1)/fs,1.0/fs1)
t11=np.arange(0,len(data11)/fs,1.0/fs11)
t=np.arange(0,len(data)/fs,1.0/fs)
#temp=np.zeros((t1.shape))
#temp[0;len(data11)]=data11;
print(t11,len(data11))
#plt.subplot(311);plt.plot(t1,data1)
#plt.subplot(312);plt.plot(t11,data11)
#plt.subplot(313);plt.plot(t,data)
plt.show()

