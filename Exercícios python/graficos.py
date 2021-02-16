import pandas as pd
import matplotlib.pyplot as plt

data = {'Ano': [1928, 1938 , 1948,1958, 1968, 1978, 1988, 1998, 2000, 2010],
        'Taxa_Desemprego': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3 ]
        }

df = pd.DataFrame(data, columns=['Ano', 'Taxa_Desemprego'])

df.plot(x = 'Ano', y = "Taxa_Desemprego", kind ="bar")
plt.show()