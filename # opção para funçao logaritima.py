# opção para funçao logaritima

import matplotlib.pyplot as plt
import numpy as np

def log (base, logaritimando):
    resultado = 0
    base_inicio = base
    resultados = []
    while base <= logaritimando:
        base *= base_inicio
        resultado +=1
        resultados.append(resultado)

    return resultado

def plot_log(base, logaritimando):
    resultados = log(base, logaritimando)
    plt.plot(range( 1, len(resultados)+ 1), resultados, marker = 'o' )
    plt.xlabel(' logaritimando ')
    plt.ylabel(' resultado de "x" na base {base}')
    plt.title( ' função log{base}(x)')
    plt.grid(True)
    plt.show()

print(' funçao log: f(x) = logbase(logaritimando)')
base = int(input(' digite a base da função logaritima: '))
logaritimando = int(input(' digite o logaritimando da função logaritima: '))
print(log(base,  logaritimando))
plot_log(base, logaritimando)