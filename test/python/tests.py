#Импортируем библиотеку pandas
import pandas as pd

#Загрузим данные из файла
names_data = pd.read_csv("people.txt")
addresses_data = pd.read_csv("addresses.txt")
#Соединим данные в один DataFrame по столбцу ID
merge_data = pd.merge(names_data, addresses_data, on="ID")

# Расчет среднего возраста для каждого города/улицы/номера дома
mean_age_by_location = merge_data.groupby(["City", "Street", "House"])["Age"].mean().reset_index()

#Вывод датафрейма
print(merge_data)
