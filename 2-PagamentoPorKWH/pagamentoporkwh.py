#Desafio 2: Conta de energia
NomeCliente= input("Nome do Cliente: ")
ConsumoMedioAnterior= int( input("Valor do consumo médio do ano anterior em KWH: "))
ConsumoAtual= int(input("Consumo atual em KWH: "))
ValorBruto= (ConsumoAtual)*1.1271522
TaxaBand= (ConsumoAtual)//100
BandVermelha= TaxaBand*3.971
if (ConsumoAtual) > (ConsumoMedioAnterior)*(0.9):
        (TotalPagar) = (ValorBruto)
if (ConsumoMedioAnterior)*(0.8) < (ConsumoAtual) and (ConsumoAtual) <= (ConsumoMedioAnterior)*(0.9):
        (TotalPagar) = (ValorBruto)*(0.97)
if (ConsumoMedioAnterior)*(0.6) <= (ConsumoAtual) and (ConsumoAtual) <= (ConsumoMedioAnterior)*(0.8):
        (TotalPagar) = (ValorBruto)*(0.93) 
if (ConsumoAtual) < (ConsumoMedioAnterior)*(0.6):
        (TotalPagar) = (ValorBruto)*(0.88)
if (ConsumoAtual) >= (ConsumoMedioAnterior):
        (TotalPagar) = (ValorBruto)
if (TotalPagar)<=(23.00):
        (TotalPagar)=(23.00)
print ("Nome do Cliente: ", NomeCliente)
print ("Consumo médio: ", ConsumoMedioAnterior)
print ("Consumo informado: ", ConsumoAtual)
print ("Valor Bruto: R$", round(ValorBruto, 2))
print ("Total a pagar: R$", round(TotalPagar, 2))
print ("Adicional da bandeira vermelha: R$", round(BandVermelha, 2))
print ("Programa executado com sucesso")  