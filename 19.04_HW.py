import pandas as pd
import datetime as dt

df = pd.read_csv('source_data.csv')
df['date'] = pd.to_datetime(df['date'])
df_january = df.loc[df['date'].dt.month == 1]

#1. У всех ли order_price == 0?
answer = df.query('order_price != 0')
#2. Какой процент таких заказов за весь январь?
answer = len(df_january.query('order_price == 0'))/ len(df_january['order_price'])*100
#10.569136892197873
#3. Найти, в какие дни у нас есть заказы с ценой == 0
thing = df.query('order_price == 0')
answer = thing['date'].dt.date.unique()
#[datetime.date(2022, 1, 1)]
#4. Топ 100 пользователей, которые пользуются доставкой?
answer = df['uid'].value_counts()[:100]
#5. Топ 10 пользователей, которые заказывают больше всего столовых приборов?
answer = df.groupby('uid')['cutlery'].sum().sort_values(ascending=False)[:10]
#answer.plot(kind='pie')
#6. Топ 20 пользователей, оставивших чаевые?
answer = df.groupby('uid')['tips'].sum().sort_values(ascending=False)[:20]
#answer.plot(kind='pie')
#7. топ 20 дней, когда чаевых было  больше всего?
df['day'] = df['date'].dt.date
answer = df.groupby('day')['tips'].sum().sort_values(ascending=False)[:20]
#answer.plot(kind='pie')
#8. Какое количество столовых приборов пользуется популярностью?
answer = df['cutlery'].value_counts()
#9. Сколько пользователей в этих данных?
answer = df['uid'].nunique()
#10. В какое время суток чаще всего осуществляют заказы?
df['hour'] = df['date'].dt.hour
answer = df['hour'].value_counts()
#answer.plot(kind='pie')
#больше всего в утреннее
#11. Топ-10 пользователей, которые потратили наибольшее количество денег в сервисе
answer = df.groupby('uid')['order_price'].sum().sort_values(ascending=False)[:10]
#answer.plot(kind='pie')
#12. Топ 5 дней, в которые было больше всего заказов? (вывести день и количество заказов)
filtered= df.loc[df["order_price"]!=0]
answer = filtered['day'].value_counts()[:5]
#answer.plot(kind='pie')