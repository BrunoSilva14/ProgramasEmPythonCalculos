def criarmatriz(x):
    arquivo=open(x, 'r')
    X=[]
    linha=arquivo.readline()
    linha = linha.split()
    while linha != []:
        X.append(linha)
        linha=arquivo.readline()
        linha= linha.split()
        
    for i in range (0, len(X)):
        for j in range (0, len(X[0])):
            X[i][j]=float(X[i][j])
    arquivo.close()
    return X

def multiplicacao(A, B):
    m=len(A)
    n=len(A[0])
    p=len(B[0])

    C=[]
    for i in range(m):
        a=[]
        for j in range(p):
            a.append(0)
        C.append(a)

    for i in range (0, m):
        for j in range (0, p):
            for k in range (0, n):
                C[i][j]+=A[i][k]*B[k][j]
    return C

def imprimeMatriz(Matriz ,Titulo):
    nl = len (Matriz)
    nc = len (Matriz[0])
    print (f"\n{' ' *nc*3} {Titulo}\n")
    for lin in range (0,nl):
        for col in range (0,nc):
            print (f" {Matriz [lin] [col]:5.2f} {' '*2}", end =' ')
        print()

def imprimeMatrizC(Matriz ,Titulo):
    nl = len (Matriz)
    nc = len (Matriz[0])
    print (f"\n{' ' *nc*3} {Titulo}\n")
    for lin in range (0,nl):
        for col in range (0,nc):
            print (f"{Matriz [lin] [col]:5.2f} {' '*2}", end =' ')
        print ()

def somatorio(X):
    lista=[]
    for j in range (0, len(X)):
        soma=0
        for i in range (0, len(X[j])):
            soma+=X[j][i]
        lista.append(soma)
    return(lista)

meses=['Janeiro', 'Fevereiro', 'Março']

Producao=criarmatriz('Producao.dad')
Custo=criarmatriz('Custo.dad')
Faturamento=multiplicacao(Producao, Custo)
imprimeMatriz(Producao, '              Matriz de Produção')
imprimeMatriz(Custo, 'Matriz de Custos')
imprimeMatrizC(Faturamento, 'Matriz de Custos Totais')

print('\n   Relatório Final\n')
for i in range (0, len(somatorio(Custo))):
    print(f'Preço produto{i+1}: R${somatorio(Custo)[i]:6.2f}')
for i in range (0, len(somatorio(Faturamento))):
    print(f'Faturamento do mes de {meses[i]}: R${somatorio(Faturamento)[i]:.2f}')

maiorfaturamento=max(somatorio(Faturamento))
print(f'Maior faturamento: {meses[somatorio(Faturamento).index(maiorfaturamento)]} R${maiorfaturamento:.2f}')
for i in range (0, len(Faturamento)):
    print(f'Imposto pago em {meses[i]}: R${Faturamento[i][1]:.2f}')

faturamentototal=0
for i in range (0, len(Faturamento)):
    for j in range (0, len(Faturamento[0])):
        faturamentototal+=Faturamento[i][j]
print(f'Faturamento do trimestre: R${faturamentototal:.2f}')
lucro=0
for i in range (0, len(Faturamento)):
    lucro+=Faturamento[i][2]
print(f'Lucro do trimestre: R${lucro:.2f}')