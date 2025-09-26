import random

caras = [1, 2, 3, 4, 5, 6]
pesos = [1, 1, 1, 1, 1, 10]

resulado = random.choices(caras, weights=pesos)

print(resulado)