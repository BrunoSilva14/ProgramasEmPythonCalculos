while True:
    nota1 = float(input( "nota 1:" ))
    nota2 = float(input( "nota 2:" ))
    nota3 = float(input( "nota 3:" ))
    média = (nota1+nota2+nota3)/3
    if média == 0:
        break
    print( f"Média: {média:4.1f}\n" )
print( "Programa executado com sucesso" )
