#Proyecto Parcial 01
#Ricardo Lopez Canales A01422699
#Omar David Hernández Aguirre A01383543
#Bernardo Garcia Zermeno A00570682

def metodo_lineal_congruencial(n_numeros=10, x_0=6, a=32, c=3, m=80):
  x_i = x_0
  X = []
  R = []

  #Calculo de X y R
  for i in range(n_numeros):
      result_x = ((a * x_i) + c) % m
      X.append(result_x)
      R.append(result_x / m)
      x_i = result_x

  return R

  

def leer_archivo_pruebas(nombreArchi, arreglo, decimal):
    #Lectura de archivo cuyos datos se regresan en un arreglo
    with open(nombreArchi) as archivo:
        for linea in archivo:
            arreglo.append(round(float(linea), decimal))

    archivo.close()
    return arreglo


def prueba_chi_cuadrada(a, decimales=4):
    rangos = []
    freq = []
    Xresul = []
    intervalo = 10
    sumXresul = 0
    N = len(a)
    W = 0.1
    limiteInf = 0
    limiteSup = limiteInf + W
    
    #Creacion de rangos
    for x in range(intervalo):
        rangos.append('[' + str(limiteInf) + ', ' + str(limiteSup) + ')')
        limiteInf = round(limiteSup, decimales)
        limiteSup = round(limiteSup + W, decimales)
    
    #Calculo de frecuencias
    limiteInf = 0
    limiteSup = limiteInf + W
    valorRep = 0
    indice = 0
    
    while (indice < N):
        if (a[indice] >= limiteInf) and (a[indice] < limiteSup):
            valorRep = valorRep + 1
        else:
            freq.append(valorRep)
            valorRep = 0
            limiteInf = round(limiteSup, decimales)
            limiteSup = round(limiteSup + W, decimales)

            if (a[indice] >= limiteInf) and (a[indice] < 1):
                indice = indice - 1
        indice = indice + 1
    freq.append(valorRep)
  
    # Si el limite superior no alcanza 1 dentro del ciclo, tendremos que meter los datos restantes(0) en el arreglo
  
    while (limiteSup < 1):
        freq.append(0)
        limiteSup = round(limiteSup + W, decimales)
    
    #Valor esperado
    E = N / intervalo

    for y in range(intervalo):
        Xresul.append(((freq[y] - E)**2) / E)

    sumXresul = round(sum(Xresul), decimales)
  
    #Determinar si se rechaza o no la hipotesis
    alfa = 0.05
    GI = intervalo - 1

    if (alfa == 0.05 and GI == 9):
        H0 = 16.9190

    estatuto1 = 'H0: Generated numbers are not different from the uniform distribution'
    estatuto2 = 'H1: Generated numbers are different from the uniform distribution'

    if (sumXresul > H0):
        estado = 'is REJECTED'
        simbolo = ' > '
    else:
        estado = 'is NOT REJECTED'
        simbolo = ' < '
    
    #Imprimir resultados
    print('Intervals\tObserved\tExpected\t(O-E)^2/E')
    for x in range(intervalo):
      print(f"{rangos[x]}\t\t{freq[x]}\t\t {3.0000}\t\t\t{round(Xresul[x], decimales)}")

    print('X^2 = ' + str(sumXresul))
    print('\n')

    print(estatuto1)
    print(estatuto2)

    print('Since ' + str(sumXresul) + simbolo + str(H0) + ' H0 ' + estado +
          '\n')


def prueba_de_rachas(data):
    #Calculo de simbolos
    for h in range(len(data) - 1):
        if (data[h + 1] - data[h] > 0):
            sim.append('+')
        else:
            sim.append('-')
    
    #Calculo de rachas
    rach = 1
    for i in range(len(sim) - 1):
        if (sim[i] != sim[i + 1]):
            rach = rach + 1

    miu = round(((2 * len(sim) - 1) / 3), decimales)
    sig = (16 * len(sim) - 29) / 90
    sigma = round(sig**(1 / 2), decimales)

    zScore = round(((rach - miu) / sigma), decimales)
    # Por defecto se imprimen 15 signos nada más
    if len(sim) > 15:
      seleccion = input('Se generaron más de 15 signos. ¿Deseas imprimir todos? S/N\n')
      if (seleccion == 'S'):
        print("Signos generados: ")
        print(sim)
      elif seleccion == 'N':
        print(sim[:14])
    else:
      print(sim)

    print('Total: ' + str(len(sim)))
    print('Total Runs: ' + str(rach))

    print('Statistics')
    print('Miu= ' + str(miu))
    print('Sigma= ' + str(sigma))
    print('zScore= ' + str(zScore) + '\n')

    estatutoh0 = 'H0: Appereance of the numbers is random'
    estatutoh1 = 'H1: Appereance of the numbers is not random'

    print(estatutoh0)
    print(estatutoh1)

    if (abs(zScore) > 1.96):
        simbolo2 = '>'
        estado2 = 'Rejected'
    else:
        simbolo2 = '<'
        estado2 = 'NOT Rejected'

    print('Since | ' + str(zScore) + ' |' + simbolo2 + ' | 1.96 |, H0 is ' +
          str(estado2))

    return


if __name__ == "__main__":  
  
  #Desarrollo del metodo lineal congruencial
  R = metodo_lineal_congruencial()
  print('Método lineal congruencial:')
  print(R)
  print('\n')

  data = []
  decimales = 4
  leer_archivo_pruebas("chi_data.txt",data,decimales)
  
  #Desarrollo del metodo de chi cuadrada
  prueba_chi_cuadrada(sorted(data))

  #Arreglos a llenar
  data = []
  decimales = 5
  sim = []
  leer_archivo_pruebas("runs_data.txt",data,decimales)
  #Desarrollo del metodo de chi cuadrada
  prueba_de_rachas(data)