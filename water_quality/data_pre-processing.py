# Rescale data (between 0 and 1)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


print("");
print("1. RESCALE DATA");
print(" rescaled into the range between 0 and 1");

filename = "water_quality/water_potability.csv"
# names = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity', 'Potability']
data = read_csv(filename)
dataframe = read_csv(filename)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:5,:])


print("");
print("2. STANDARDIZE DATA");
print("Standardization is when you scale data to have a mean of 0 and a standard deviation of 1.");
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
#use StandardScaler class to rescale the data
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:5,:])



from sklearn.preprocessing import Normalizer
import numpy as np
print("");
print("3. NORMALIZE  DATA");
print(" is the process of scaling data so that each row has a length of 1.");
X = array[:,0:8]
Y = array[:,8]
X_cleaned = X[~np.isnan(X).any(axis=1)]  # Remove rows with NaN values

# Normalize the cleaned data
normalizer = Normalizer()
X_normalized = normalizer.fit_transform(X_cleaned)

set_printoptions(precision=1)
print(X_normalized[0:5,:])



from sklearn.preprocessing import Binarizer
from sklearn.impute import SimpleImputer
from numpy import set_printoptions
import numpy as np

print("");
print("4. BINARIZE  DATA");
print("All values above the threshold are marked as 1, and all values equal to or below the threshold are marked as 0.");

X = array[:,0:8]
Y = array[:,8]

imputer = SimpleImputer(strategy='mean')  # Можно использовать 'median' или 'constant'
X_imputed = imputer.fit_transform(X)

binarizer = Binarizer(threshold=0.0)
X_binarized = binarizer.fit_transform(X_imputed)

binaryX = binarizer.transform(X_imputed)
# Summarize transformed data

# Summarize transformed data
from numpy import set_printoptions
set_printoptions(precision=3)
print(binaryX[0:5, :])  # Printing the first 5 rows of transformed data
