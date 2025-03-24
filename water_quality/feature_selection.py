from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_classif


print("")
print("1.  Univariate Selection")
print(" Statistical tests can be used to select those features that have the strongest relationship with the output variable.")
# Загружаем данные
data = load_iris()
X = data.data
y = data.target

# Удаление строк с NaN
X_clean = X[~np.isnan(X).any(axis=1)]
y_clean = y[~np.isnan(X).any(axis=1)]

# Выбор признаков с помощью SelectKBest
selector = SelectKBest(f_classif, k=2)
X_new = selector.fit_transform(X_clean, y_clean)
print(X_new)


print("")
print("2.  Recursive Feature Elimination")
print("  works by recursively removing attributes and building a model on thoseattributes that remain.")

# Загружаем данные
filename = "water_quality/water_potability.csv"
dataframe = pd.read_csv(filename)

# Убираем строки с пропущенными значениями
dataframe = dataframe.dropna()

# Разделяем признаки и целевую переменную
X = dataframe.iloc[:, :-1].values  # Все столбцы, кроме последнего
Y = dataframe.iloc[:, -1].values   # Последний столбец (Potability)

# Масштабируем признаки
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Feature extraction
model = LogisticRegression(max_iter=1000)  # Увеличиваем количество итераций
rfe = RFE(model, n_features_to_select=3)
fit = rfe.fit(X_scaled, Y)

# Вывод результатов
print("Num Features:", fit.n_features_)
print("Selected Features:", fit.support_)
print("Feature Ranking:", fit.ranking_)


print("")
print("3. Principal Component Analysis (PCA)")
print("  works by recursively removing attributes and building a model on those attributes that remain.")

# Загружаем данные
filename = "water_quality/water_potability.csv"
dataframe = pd.read_csv(filename)

# Убираем строки с пропущенными значениями
dataframe = dataframe.dropna()

array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)
# summarize components
print("Explained Variance:", fit.explained_variance_ratio_)
print(fit.components_)
