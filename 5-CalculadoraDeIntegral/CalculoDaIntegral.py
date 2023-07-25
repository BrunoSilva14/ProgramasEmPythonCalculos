#Cálculo da integral
from math import *
while True:
    def funcao(x):
        return(1/(16-x**2))
#Cálculo da integral pela regra do trapézio
    def integral(a, b, n):
        h=(b-a)/n
        xf=0
        while a<b:
            xf+=(((funcao(a))+(funcao(a+h)))/2)*h
            a+=h
        return(xf)
    valA=int(input('Digite o valor de a: '))
    valB=int(input('Digite o valor de b: '))
    valN=int(input('Digite o valor de n: '))
    print(f'\nO valor da integral com a = {valA}; b = {valB}; n = {valN} é: {integral(valA, valB, valN):.6f}\n')
    print('Programa executado com sucesso.')
    input()
