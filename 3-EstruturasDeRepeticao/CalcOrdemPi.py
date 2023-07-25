#Desafio 2
#Criando a série
import math
import time
start = time.time()
Lim= float(input("Digite a ordem : "))
termo=1
S=0
k=1
while True:
    if abs(termo)<Lim:
        break
    S=S+termo
    k=k+1
    termo=(1/(2*k-1)**3)*((-1)**(k+1))
n= k-1
print("valor de S é: ",S)
#calculando pi
pi=((32*S)**(1/3))
print("o valor de pi é: ", float(pi))
diferença = math.pi - pi
print("diferença entre a constante pi e o pi encontrado: ", diferença)
end = time.time()
print("o último termo definido é: ",termo)
print("o número de termos da série é: ", n)
print("o tempo de execução do programa é",end-start)
print("Programa executado com sucesso")