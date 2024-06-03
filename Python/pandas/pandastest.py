import pandas as pd

nombres = ['Fabian','Ernesto','Erny','Si','6']
rut = ['213427989','168465422','54879548','123456789','32154878']
data = {
    'Nombres': nombres,
    'Rut': rut
}

dataframe = pd.DataFrame(data)
print(dataframe.set_index("Rut"))