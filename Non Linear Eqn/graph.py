import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)
y = x**3 - 2400*(x**2) - 3*x + 2

plt.figure(figsize = (10, 10))
plt.plot(x, y, 'r')
plt.title('Molar dissociation of H20')
plt.ylabel('Y Axis')
plt.ylim(-1, 2)
plt.grid()
plt.show()