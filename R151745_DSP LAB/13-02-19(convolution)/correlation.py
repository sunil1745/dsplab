import matplotlib.pyplot as plt
import numpy as np
time = np.arange(0, 100, 0.1);
y = np.sin(time)
result = np.correlate(y, y, mode='full')
plt.plot(result[:int(result.size/2 )])
plt.show()
print(result)
