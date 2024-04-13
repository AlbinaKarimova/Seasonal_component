
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "10.csv"
dfv = pd.read_csv(file)

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

for j in range(0, len(dfv)//2):
    aj, bj = calculate_coefficients(dfv['xi'], j, len(dfv))
    alphas.append(aj)
    betas.append(bj)
    Pj = aj**2 + bj**2
    P.append(Pj)

# Поиск индексов наибольших значений P(j) для выявления гармоник
num_harmonics = 3  # Количество выбираемых гармоник
J = np.argsort(P)[-num_harmonics:]

print("Индексы выбранных гармоник:", J)
print("Самые существенные сезонные компоненты: ", [P[j] for j in J])
print("Период 1-й гармоники: ", len(dfv)/J[0], ", Доля амплитуды: ", P[J[0]]/(sum(P)-P[len(P)-1]))
print("Период 2-й гармоники: ", len(dfv)/J[1], ", Доля амплитуды: ", P[J[1]]/(sum(P)-P[len(P)-1]))
print("Период 3-й гармоники: ", len(dfv)/J[2], ", Доля амплитуды: ", P[J[2]]/(sum(P)-P[len(P)-1]))

X = []
for i in range(len(dfv)-1):
    X.append(dfv['xi'][i])

#функция сезонной компоненты
def season(t):
   S = 0
   for j in J:
    S += alphas[j]*np.cos(2 * np.pi * j * t / len(dfv)) + betas[j]*np.sin(2 * np.pi * j * t / len(dfv))
   return S

Seas = []
for t in range(len(dfv)):
    Seas.append(season(t))

# Построение графика периодограммы
def periodogramm(P_j):
    plt.plot(range(len(P_j)), P_j, color='Green')
    plt.plot(np.array(J), [P[j] for j in J], 'ro', label='Самые существенные компоненты')
    plt.xlabel('Период (n/j)')
    plt.ylabel('Значение периодограммы P(j)')
    plt.title('Периодограмма')

#Сравнение исходной выборочной траектории и сезонной компоненты
def compare(x, s):
    plt.plot(range(len(x)), x, color='Red', label='Исходная выборочная траектория')
    plt.plot(range(len(s)), s, label='Сезонная компонента')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.title('Сравнение исходной выборочной траектории и сезонной компоненты')

plt.figure(figsize=(10, 6))
#periodogramm(P)
compare(X, Seas)
plt.grid(True)
plt.show()






