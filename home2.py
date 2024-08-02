import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 10
x = np.random.rand(num_samples)
y = np.random.rand(num_samples)

# Создание диаграммы рассеяния
plt.scatter(x, y, alpha=0.5, edgecolors='w', linewidth=0.5)
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')
plt.grid(True)
plt.show()