import random
import matplotlib.pyplot as plt

contadores = [0,0,0,0,0,0]

print ("Simulando lanzamiento del dado...")

for int in range (1000):
  numero_alteatorio = random.randint(0,5)
  print ("El número aleatorio generado es: ", numero_alteatorio)
  contadores[numero_alteatorio] += 1

x = ['1','2','3','4','5','6']
plt.bar(x,contadores)
plt.show()