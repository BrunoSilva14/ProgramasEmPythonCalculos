#Formativa 9 Desafio 2
arquivo = open("af09ds2.dad", "r")
notas=[]
provas=[]
linha=arquivo.readline()
listaGab=list(linha)
linha=arquivo.readline()
while linha!='':
    aluno=[]
    for x in range(0, 3):
        aluno+=linha[x]
    aluno=''.join(aluno)
    provas.append(aluno)
    nota=0
    for x in range (0,10):
        if listaGab[x]==linha[x+4]:
            nota+=1
    notas.append(nota)
    linha=arquivo.readline()
print('Prova Nota')
for x in range (0, len(provas)):
    print(f' {provas[x]}   {notas[x]: >3}')
media=(sum(notas))/len(notas)
print(f'Nota média:  {media:.2f}')
print('   Aprovados\nAlunos Nota')
for x in range (0, len(provas)):
    if notas[x]>=int(media):
        print(f' {provas[x]}   {notas[x]: >3}')