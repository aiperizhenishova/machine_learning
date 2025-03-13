from pandas import read_csv
from pandas import set_option  # позволяет изменять настройки отображения
# данных в pandas, например, количество отображаемых строк или столбцов.
from matplotlib import pyplot as plt  # для отображения графиков.
import matplotlib.pyplot as pyplot
from pandas.plotting import scatter_matrix


filename = "water_quality/water_potability.csv"
# names = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity', 'Potability']
data = read_csv(filename)
print(data.shape)

peek = data.head(10)  # метод, который возвращает первые 10 строк.
print(peek)

shape = data.shape
print(shape)

types = data.dtypes
print(types)

set_option('display.width', 100)  # устанавливает ширину вывода в 100 символов
# ограничивает количество знаков после запятой до 3.
set_option('display.precision', 3)
description = data.describe()
# метод, который выводит статистическое описание числовых данных в DataFrame, включая такие параметры, как среднее значение, стандартное отклонение, минимальное и максимальное значение, квартали и т. д.
print(description)


# группирует данные по столбцу и считает количество элементов в каждой группе.
class_counts = data.groupby('Hardness').size()
print(class_counts)

skew = data.skew()
print(skew)

data.hist()
plt.show()  # для создания графика

data.plot(kind='density', subplots=True, layout=(4, 3), sharex=False)
pyplot.show()

data.plot(kind='box', subplots=True, layout=(4, 3),
          sharex=False, sharey=False)
pyplot.show()

scatter_matrix(data)  # строит матрицу рассеяния
pyplot.show()
