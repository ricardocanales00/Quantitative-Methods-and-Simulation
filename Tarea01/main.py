import math as ma
import matplotlib.pyplot as plt

data = []

print('Input the name of the file, E.g. data02.txt')
dile = input()

print('Input number of decimals, E.g. 2')
decimals = input()

with open(str(dile)) as file:
    for number in file:
        data.append(float(number))
    data.sort()
file.close()

N = len(data)

C = ma.ceil(1 + 3.3 * ma.log(N, 10))

min = min(data)
max = max(data)

W = ((max - min) / C)

if ((W + (1 * 10**-9)) - W < 1):
    W = W + (5 * 10**-(9 + 1))

W = round(W, 9)

value = 0
rang = []
counter = []

lim1 = min
lim2 = min + W

for i in range(N):
    if (data[i] < lim2) and (data[i] >= lim1):
        value = value + 1
    else:
        counter.append(value)
        rang.append('[' + str(round(lim1, int(decimals))) + ',' +
                    str(round(lim2, int(decimals))) + ')')
        lim1 = lim2
        lim2 = lim2 + W
        value = 1

counter.append(value)
rang.append('[' + str(round(lim1, int(decimals))) + ',' +
            str(round(lim2, int(decimals))) + ')')

print('N: ', N)
print('C = ' + str(C))
print('Max: ' + str(round(max, int(decimals))) + ',  min: ' +
      str(round(min, int(decimals))))
print('W = ' + str(round(W, int(decimals))))

print('\n')

print('Intervals           f')
for x in range(C):
    print(str(rang[x]) + '  ' + str(counter[x]))

print('\n')
print('Sum of frequencies: ', sum(counter))

plt.bar(rang, counter)
plt.show()
