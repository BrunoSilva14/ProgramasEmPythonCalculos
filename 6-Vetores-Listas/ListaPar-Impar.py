listaA=[]
a=0
while a>=0:
    a=int(input('Digite o número a ser adicionado: '))
    if a>=0:
        listaA.append(a)

listaB=[]
listaC=[]
contador=0
while contador!=len(listaA):
    if listaA[contador]%2==0:
        listaB.append(listaA[contador])
    else:
        listaC.append(listaA[contador])
    contador+=1
print(f'Conjunto lido: {listaA}')
print(f'Conjunto dos pares: {listaB}')
print(f'Conjunto dos ímpares: {listaC}')