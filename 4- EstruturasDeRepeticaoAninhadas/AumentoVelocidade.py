#Etapa 1: Ler os valores necessários:
ci=float(input('Marco da cidade origem: '))
cf=float(input('Marco da cidade destino: '))
vi=float(input('Velocidade inicial a ser usada para cálculo do tempo: '))
vf=float(input('Valor da última velocidade a ser testada: '))
inc=float(input('Incremento a ser dado à velocidade para o cálculo dos tempos: '))

#Esta parte do código calcula a distância do trajeto e deixar ela com valor absoluto:
dc=cf-ci
import math
mdc=math.sqrt(dc**2)
v=vi+inc
t=mdc/vi

#Obter o módulo da diferença dos marcos:
print('\nMarco origem:  %.2i' %ci)
print('Marco destino: %.2i' %cf)
print('Distância:     %.2i' %mdc)
print('Velocidade   Tempo')
print('   %.1f      %.2f' %(vi, t))
t=mdc/v
while v<=vf:
    print('   %.1f      %.2f' %(v, t))
    v=v+inc
    t=mdc/v

#3. Fazer os demais trajetos:
ci2=1
while ci2!=0:
    ci2=float(input('Marco da cidade origem: '))
    if ci2!=0:
        cf2=float(input('Marco da cidade destino: '))
        
        #O if abaixo é pra garantir que os cálculos do trajeto só sejam feitos caso o marco final não seja 0:
        vi2=float(input('Velocidade inicial a ser usada para cálculo do tempo: '))
        vf2=float(input('Valor da última velocidade a ser testada: '))
        inc2=float(input('Incremento a ser dado à velocidade para o cálculo dos tempos: '))

        #Esta parte do código calcula a distância do trajeto e deixar ela com valor absoluto:
        dc2=cf2-ci2
        import math
        mdc2=math.sqrt(dc2**2)
        v2=vi2+inc2
        t2=mdc2/vi2

        print('\nMarco origem:  %.2i' %ci2)
        print('Marco destino: %.2i' %cf2)
        print('Distância:     %.2i' %mdc2)
        print('Velocidade   Tempo')
        print('   %.1f      %.2f' %(vi2, t2))
        t2=mdc2/v2
        while v2<=vf2:
            print('   %.1f      %.2f' %(v2, t2))
            v2=v2+inc2
            t2=mdc2/v2
else:
    input('Programa executado com sucesso.')