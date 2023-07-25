#LISTA A:
listaA=[]
a=0
while a!=(-1):
        a=int(input('Digite o número: '))
        if a!=(-1): 
            listaA.append(a)

#LISTA B:
listaB=[]
contador=0 
natural=1
impar=9
while contador!=len(listaA):
    listaB.append(natural)
    listaB.append(impar)
    natural+=1
    impar+=2
    contador+=1

#LISTA C:
listaC=[]
contador=0
print('\nA     B     C')
while contador!=len(listaA):
    if listaA[contador]%5==0:
        listaC.append(listaA[contador]+listaB[contador])
    else:
        listaC.append(listaA[contador]*2)
    print(f'{listaA[contador]: <4}  {listaB[contador]: <4}  {listaC[contador]}')
    contador+=1