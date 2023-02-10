#audio signals
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

frequency_sampling, audio_signal= wavfile.read("")#this is where we put the audio file in

#idrk about how variables in 
print('\nSignal shape: ',audio_signal.shape)
print('Signal Datatypes: ',audio_signal.dtype)
print('Signal duration: ',round(audio_signal.shape[0]/float(frequency_sampling),2),'seconds')

#normalizing the signal
audio_signal=audio_signal/np.power(2,15)

#i think the wavfile takes values as a list..
#extract the first 100 val to visualize
audio_signal=audio_signal[:100]
time_axis=1000*np.arrange(0,len(audio_signal),1)/float(frequency_sampling)

print('audio signal variable is this type: '+type(audio_signal))

#actually graphing and visualizing commands
plt.plot(time_axis,audio_signal,color='blue')
plt.xlabel('Time(milliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()
