#Avaliação Formativa 8
dados= open("notas.dad", "r")
lista= []
linha= 0
val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
abso = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x=0
soma= 0
acima=0
while int(linha) !=999:
    linha= dados.readline()
    if int(linha)!=999:
        lista.append(int(linha))
        x=int(linha)
        abso[x]=abso[x]+1
        soma=soma+int(linha)
dados.close()
tamanho = len(lista)
media= soma/tamanho
print("Notas Frequência  Frequência\n       Absoluta   Relativa(%)")
for x in range(int(media+1),11):
            acima= acima+ abso[x]
for x in range(0,11):
    rel[x]=rel[x] + float(((abso[x]/tamanho)*100)) 
for x in range (0,11):
    print(f'{val[x]:3d}{" "*5}{abso[x]:3d}{ " "*7} {rel[x]:5.2f}')
media= soma/tamanho
print(f"Nota média:{(media):6.2f}")
print(f"Notas acima da média: {(acima):2}")
print(f"Porcentagem de notas acima da média:  {(100*acima/tamanho):6.2f}")