import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = x**2

plt.plot(x, y)
plt.xlabel("X axel")
plt.ylabel("Y axel")
plt.title("Function graph y = x**2")
plt.grid(True)
plt.show()