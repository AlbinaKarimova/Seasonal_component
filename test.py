import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = "C:/Users/Альбина/Desktop/Учеба/Случайные процессы/data_for_problem_1_05-107/05-107/3.csv"
dfv = pd.read_csv(file)
n = len(dfv)
# Функция для вычисления коэффициентов а и b для гармоники j
def calculate_coefficients(xi, j, n):
    a = 0
    b = 0
    for i in range(n):
        a += xi[i] * np.cos(2 * np.pi * j * i / n)
        b += xi[i] * np.sin(2 * np.pi * j * i / n)
    a *= 2 / n
    b *= 2 / n
    return a, b

# Вычисление α и β для каждой гармоники
alphas, betas = [], []
P = []

for j in range(1, n//2 + 1):
    aj, bj = calculate_coefficients(dfv['xi'], j, n)
    alphas.append(aj)
    betas.append(bj)
    Pj = aj**2 + bj**2
    P.append(Pj)

## Определение двух самых существенных сезонных компонент
num_harmonics = 2
P_sorted_indices = np.argsort(P)
J = P_sorted_indices[-num_harmonics:][::-1]

print("Две самые существенные сезонные компоненты:")
for idx in J:
    print(f"Гармоника с периодом n/{idx + 1}")

# Построение графика периодограммы
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(P) + 1), P)
plt.plot(np.array(J) + 1, [P[j] for j in J], 'ro', label='Самые существенные компоненты')
plt.xlabel('Период (n/j)')
plt.ylabel('Значение периодограммы P(j)')
plt.title('Периодограмма')
plt.grid(True)
plt.legend()
plt.show()