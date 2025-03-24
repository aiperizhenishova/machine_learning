from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler  # Added scaler for data preprocessing

# Load data
filename = 'diabetes (1).csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
Array = dataframe.values
X = Array[:, 0:8]
Y = Array[:, 8]

# Feature scaling 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scaling the features

# Feature extraction using RFE
model = LogisticRegression(max_iter=200)  # Increased max_iter to ensure convergence
rfe = RFE(model, n_features_to_select=3)
fit = rfe.fit(X_scaled, Y)  # Use scaled data

# Display the results
print(" RFE choose preg, mass and pedi as the first 3 best features. They are marked as 1 in the output.")
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)
