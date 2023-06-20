import pandas as pd
import matplotlib.pyplot as plt

s = '''Страна    Год    Объем
США       2010   500
США       2011   550
США       2012   600
Китай     2010   450
Китай     2011   520
Китай     2012   590
Германия  2010   400
Германия  2011   420
Германия  2012   440'''

def write_data(file_name, data):
    f = open(file_name, 'w', encoding='utf-8')
    f.write(data)
    f.close()


data = [row.split() for row in s.split('\n')]
res = '\n'.join([','.join(row) for row in data])
print(res)
write_data('trade_data.csv', res)
#-----
data = pd.read_csv('trade_data.csv')
data['Год'] = data['Год'].astype('str')

plt.figure(figsize=(10, 6))
for country in data['Страна'].unique():
    country_data = data[data['Страна'] == country]
    plt.plot(country_data['Год'], country_data['Объем'], label=country)
plt.xlabel('Год')
plt.ylabel('Объем торговли')
plt.legend()
plt.savefig('trade_volume.png')
plt.show()