import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
#загружаем данные
with open('events.json','r', encoding='utf-8') as f:
    data=json.load(f)

events=data['events']
df=pd.DataFrame(events)
print(df.head) #мы получили данные в виде таблицы
#строим график
plt.figure(figsize=(10,10))
sns.countplot(x='signature', data=df)
plt.title('Распределение типов событий')
plt.xticks(rotation=90)
plt.show()
