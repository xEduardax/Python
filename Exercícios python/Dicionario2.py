Filmes = dict()
Locadora = list()
for f in range (0,3):
    Filmes['Título'] = str(input('Titulo do filme: '))
    Filmes['Ano'] = int(input('Ano do filme: '))
    Locadora.append(Filmes.copy())

for f in Locadora:
   print (f)