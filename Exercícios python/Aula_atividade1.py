n1 = float(input('Digite sua primeira nota da prova: '))
n2 = float(input('Digite sua segunda nota da prova: '))
n3 = float(input('Digite sua terceira nota da prova: '))
n4 = float(input('Digite sua quarta nota da prova: '))
media = (n1 + n2 + n3 + n4) / 4

print('A sua media foi {:.1f}'.format(media))
if media >= 7.0:
    print('A sua média foi boa! PARABÉNS, VOCÊ FOI APROVADO!')
else:
    print('Sua média foi ruim! VOCÊ FOI REPROVADO,ESTUDE MAIS!')

