import pandas as pd

cliente = {"Nome": ['Eduarda', 'Marcela', 'Cauã', 'Beatriz'],
           "Idade": [21, 35, 13, 20]}

print(cliente)
print("\n\n")

dataframe = pd.DataFrame((cliente), index= ['1', '2', '3', '4']) #é assim que se muda o indice
print(dataframe)
