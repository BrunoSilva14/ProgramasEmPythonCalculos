# imprimir titulos
print("\n Brincando com a função f(x) = 7,8 - x*x ")
print("    X       F(X) ")
# variar x entre -4 e +4 de 0.25 em 0.25
# armazena em x o valor inicial -4.0
x = -4.0
#enquanto x for menor ou igual a 4.0, repita:
while x <= 4.0: 
    # calcular f(x)
    fx = 7.8-x**2
    #imprimir x e f(x)
    print(f"{x:7.2f}  {fx:7.2f}")
    #calcular o próximo valor de x
    x = x + 0.25
    # fim do escopo do comando while,retorne ao inicio
print("Aluno:Bruno Soares e Silva")
print("Programa executado com sucesso")
