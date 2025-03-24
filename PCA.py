# Feature Extraction with PCA
from pandas import read_csv
from sklearn.decomposition import PCA

# load data
filename = 'diabetes (1).csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]

# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)

# summarize components
print("PCA (Principal Component Analysis) is a method to simplify data by reducing its dimensions. It's like compressing the data without losing the important stuff. ")
print("Explained Variance: %s" % fit.explained_variance_ratio_)
print(fit.components_)


