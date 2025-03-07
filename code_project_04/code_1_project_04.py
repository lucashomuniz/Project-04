"""
========
IMPORTS
========
"""

import joblib
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.core.display_functions import display
from matplotlib import pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, auc, roc_auc_score, confusion_matrix
from sklearn.metrics import accuracy_score
import imblearn
from imblearn.over_sampling import SMOTE

# Load the data
dados = pd.read_csv('dados/dataset.csv')

# Sample data
dados.sample(10)

"""
==========================
EXPLORATORY DATA ANALYSIS
==========================
"""

# Data types
print(dados.dtypes)

# Categorical variables
print(dados.dtypes[dados.dtypes == 'object'])

# Non-categorical variables
print(dados.dtypes[dados.dtypes != 'object'])

# Exploration of Numerical Variables
dados.describe()

# Plot 
dados.hist(figsize = (15, 15), bins = 10)
plt.show()

# Apparently there is an outlier in the variables "Alamine_Aminotransferase" and "Aspartate_Aminotransferase"
# Due to the fact that the maximum value is much higher than the average value.
# The dataset column (target variable) has '1' for liver disease and '2' for no liver disease.
# Let's adjust the variable by putting values that are easier to interpret. The negative class (does not have the disease) will be zero.

# Function to adjust target variable
def ajusta_var(x):
    if x == 2:
        return 0
    return 1

# Apply the function
dados['Dataset'] = dados['Dataset'].map(ajusta_var)

# Let's adjust the target variable name
dados.rename({'Dataset':'Target'}, axis = 'columns', inplace = True)

# Correlation between variables
dados.corr()

# Exploration of the Categorical Variable
dados.describe(include = ['object'])

# Plot
sns.countplot(data = dados, x = 'Gender', label = 'Count')

# Value counts
M, F = dados['Gender'].value_counts()

# Print
print('Number of male patients: ', M)
print('Number of female patients: ', F)

# Let's take advantage of this and transform the categorical variable into its numeric representation using label encoding.
# In addition to reducing work later, it will make it easier to create charts to follow.
# Function for label encoding
def encoding_func(x):
    if x == 'Male':
        return 0
    return 1

# Apply the function
dados['Gender'] = dados['Gender'].map(encoding_func)
dados.sample(5)

# Checking the Relationship Between Attributes
dados.corr()

# Set the background style
sns.set_style('darkgrid')  

# Facetgrid
sns.FacetGrid(dados, hue = 'Target', size = 5).map(plt.scatter, 'Total_Bilirubin', 'Direct_Bilirubin').add_legend()

# Set the background style
sns.set_style('darkgrid')  

# Facetgrid
sns.FacetGrid(dados, hue = 'Gender', size = 5).map(plt.scatter, 'Total_Bilirubin', 'Direct_Bilirubin').add_legend()

# Set the background style
sns.set_style('whitegrid') 

# Facetgrid
sns.FacetGrid(dados, hue = 'Target', size = 5).map(plt.scatter, 'Total_Bilirubin', 'Albumin').add_legend()

# Set the background style
sns.set_style('whitegrid') 

# Facetgrid
sns.FacetGrid(dados, hue = 'Gender', size = 5).map(plt.scatter, 'Total_Bilirubin', 'Albumin').add_legend()

# Checking for Missing Values and Duplicate Records
# Checking for missing values
print(dados[dados.isnull().values])

# Checking for duplicate records (complete cases)
# Complete cases also refer to lines where there are no missing values
print(dados[dados.duplicated(keep = False)])

"""
======================
ATTRIBUTE ENGINEERING
======================
"""

# Handling Duplicate Records
print(dados.shape)

# Remove duplicate records (remove one of the duplicates)
dados = dados.drop_duplicates()
print(dados.shape)

# Handling Outliers
dados.describe()

# Boxplot
sns.boxplot(dados.Alamine_Aminotransferase)

# Are the extreme values really outliers? Frequency count by value
dados.Alamine_Aminotransferase.sort_values(ascending = False).head()

# Boxplot
sns.boxplot(dados.Aspartate_Aminotransferase)

# Frequency count by value
dados.Aspartate_Aminotransferase.sort_values(ascending = False).head()

# Keep only records where the value is less than or equal to 3000
dados = dados[dados.Aspartate_Aminotransferase <= 3000]

# Boxplot
sns.boxplot(dados.Aspartate_Aminotransferase)

# Frequency count by value
dados.Aspartate_Aminotransferase.sort_values(ascending = False).head()

# Keep only records where the value is less than or equal to 2500
dados = dados[dados.Aspartate_Aminotransferase <= 2500]
dados.describe()

# Handling Missing Values. Check for missing value
dados.isnull().values.any()

# Check how many columns have missing value
dados.isnull().values.any().sum()

# List missing values
print(dados[dados.isnull().values])

# Drop records with missing values in any column (any)
dados = dados.dropna(how = 'any')  

# List missing values
print(dados[dados.isnull().values])

"""
====================
PRE-PROCESSING DATA
====================
"""

# Given the high correlation between variables Direct_Bilirubin and Total_Bilirubin, let's remove Direct_Bilirubin
dados = dados.drop('Direct_Bilirubin', 1)

# Split into Training and Test
dados.head()

# Create a separate object for the target variable
y = dados.Target

# Create a separate object for input variables
X = dados.drop('Target', axis = 1)

# Split into training and test data with stratified sampling
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y,
test_size = 0.25, random_state = 1234, stratify = dados.Target)
len(X_treino)
len(X_teste)

# Print do shape
print(X_treino.shape, X_teste.shape, y_treino.shape, y_teste.shape)
X_treino.head(2)

# Class Balancing
# As it stands, we have a lot more information about the variable target(1) than the variable(0)
# With this, we will be giving the model many more examples of the first class than the second class
# Making it learn much more about a class than about another, generating a biased model.
y_treino.value_counts()

# A first strategy would be to reduce the majority class records by removing some records from Class 1
# This strategy can greatly reduce the size of the dataframe, thus having fewer examples to train the model
# Another strategy would be the technique of oversampling and increasing the number of examples of the minority class
# In order to detect the pattern of the records of the class (0), and create synthetic data with the same pattern.
# Increasing with this the amount of lines of the minority class.
over_sampler = SMOTE(k_neighbors = 2)

# Explain why class balancing is done with training data only.
# Apply oversampling (should only be done with training data)
X_res, y_res = over_sampler.fit_resample(X_treino, y_treino)
len(X_res)
len(y_res)
y_res.value_counts()

# Set the training dataset name to X
X_treino = X_res

# Set the training dataset name to y
y_treino = y_res

# Data standardization
# The goal is to resize the variables so that they have properties of
# A normal distribution with mean equal to zero and standard deviation equal to one.
X_treino.head()

# Calculate mean and standard deviation of training data
treino_mean = X_treino.mean()
treino_std = X_treino.std()
print(treino_mean)
print(treino_std)

# Standardization
X_treino = (X_treino - treino_mean) / treino_std
X_treino.head()
X_treino.describe()

# We use training mean and deviation to standardize the test dataset
X_teste = (X_teste - treino_mean) / treino_std
X_teste.head()

"""
========================================
MODEL 1: LOGISTIC REGRESSION (BENCHMARK)
========================================
"""

# For the first version of the model, the ideal is to choose a simple and easy-to-understand algorithm.
# As part of the process involves randomness, the results may be slightly different each run.
# Define list of hyperparameters
tuned_params_v1 = {'C': [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], 'penalty': ['l1', 'l2']}

# We will create the model with GridSearch
# Several models will be created with different combinations of hyperparameters
modelo_v1 = GridSearchCV(LogisticRegression(), tuned_params_v1, scoring = 'roc_auc', n_jobs = -1)

# Model training
modelo_v1.fit(X_treino, y_treino)

# Select the best model
print(modelo_v1.best_estimator_)

# Predictions with test data
y_pred_v1 = modelo_v1.predict(X_teste)

# Show the first 10 predictions
# This algorithm shows both the classes as well as the probability.
print(y_pred_v1[:10])

# Get predictions in probability format for each class
y_pred_proba_v1 = modelo_v1.predict_proba(X_teste)

# Show the first 10 predictions
print(y_pred_proba_v1[:10])

# Get the predictions in probability format by filtering for the positive class
# Need this to calculate the ROC Curve
y_pred_proba_v1 = modelo_v1.predict_proba(X_teste)[:,1]

# Show the first 10 predictions
print(y_pred_proba_v1[:10])

# As an example, let's check one of the data points (change the value of i if you wish)
# For data point 16, actual class=1, predicted class=0, predicted probability = 0.463
i = 16
print('for the data point {}, real class = {}, expected class = {}, predicted probability = {}'.
      format(i, y_teste.iloc[i], y_pred_v1[i], y_pred_proba_v1[i]))

# Confusion matrix
confusion_matrix(y_teste, y_pred_v1)

# Extracting each value from the CM
tn, fp, fn, tp = confusion_matrix(y_teste, y_pred_v1).ravel()
print(tn, fp, fn, tp)

# Calculates the global metric AUC (Area Under The Curve) with real data and test predictions
roc_auc_v1 = roc_auc_score(y_teste, y_pred_v1)
print(roc_auc_v1)

# Calculate the ROC curve with test data and predictions
fpr_v1, tpr_v1, thresholds = roc_curve(y_teste, y_pred_proba_v1)

# AUC test
auc_v1 = auc(fpr_v1, tpr_v1)
print(auc_v1)

# Accuracy test
acuracia_v1 = accuracy_score(y_teste, y_pred_v1)
print(acuracia_v1)

# Feature Importance
# Building the model again with the best hyperparameters
# This is necessary as the final version must not have GridSearchCV
modelo_v1 = LogisticRegression(C = 1)
modelo_v1.fit(X_treino, y_treino)

# Get the coefficients by greatest using np.argsort
indices = np.argsort(-abs(modelo_v1.coef_[0, :]))
print("Most important variables for the result of model_v1: ")
print(50*'-')
for feature in X.columns[indices]:
    print(feature)

# Save the model to disk
with open('modelos/modelo_v1.pkl', 'wb') as pickle_file:
      joblib.dump(modelo_v1, 'modelos/modelo_v1.pkl') 

# Create a dataframe to receive metrics from each model
df_modelos = pd.DataFrame()

# Dictionary with model_v1 metrics
dict_modelo_v1 = {'Name': 'model_v1', 'Algorithm': 'Logistic Regression',
'ROC_AUC Score': roc_auc_v1, 'AUC Score': auc_v1, 'Accuracy': acuracia_v1}

# Add the dict to the dataframe
df_modelos = df_modelos.append(dict_modelo_v1, ignore_index = True)
display(df_modelos)

"""
=======================
MODEL 2: RANDOM FOREST
=======================
"""

# Our challenge now is to try to get a better model than version 1. Let's try the Random Forest algorithm.
# Hyperparameter grid
tuned_params_v2 = {'n_estimators': [100, 200, 300, 400, 500], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4]}

# Create the model with RandomizedSearchCV to search for the best combination of hyperparameters
modelo_v2 = RandomizedSearchCV(RandomForestClassifier(), tuned_params_v2, n_iter = 15, scoring = 'roc_auc', n_jobs = -1)

# Train the model
modelo_v2.fit(X_treino, y_treino)

# Extract the best model
print(modelo_v2.best_estimator_)

# Forecasts test
y_pred_v2 = modelo_v2.predict(X_teste)

# Get predictions for the positive class
y_pred_proba_v2 = modelo_v2.predict_proba(X_teste)[:,1]

# Confusion Matrix
confusion_matrix(y_teste, y_pred_v2)

# ROC curve on test data and predictions
roc_auc_v2 = roc_auc_score(y_teste, y_pred_v2)
print(roc_auc_v2)

# ROC curve on test data and predictions
fpr_v2, tpr_v2, thresholds = roc_curve(y_teste, y_pred_proba_v2)

# AUC test
auc_v2 = auc(fpr_v2, tpr_v2)
print(auc_v2)

# Accuracy test
acuracia_v2 = accuracy_score(y_teste, y_pred_v2)
print(acuracia_v2)

# Feature Importance
# Recreate the model with the best hyperparameters
modelo_v2 = RandomForestClassifier(n_estimators = 200, min_samples_split = 5, min_samples_leaf = 4)
modelo_v2.fit(X_treino, y_treino)

# Most relevant variables
indices = np.argsort(-modelo_v2.feature_importances_)
print("Most important variables for the v2_model result:")
print(50*'-')
for feature in X.columns[indices]:
    print(feature)

# Save the model to disk
with open('modelos/modelo_v2.pkl', 'wb') as pickle_file:
      joblib.dump(modelo_v2, 'modelos/modelo_v2.pkl') 

# Dictionary with model_v2 metrics
dict_modelo_v2 = {'Name': 'model_v2', 'Algorithm': 'Random Forest', 'ROC_AUC Score': roc_auc_v2,
'AUC Score': auc_v2, 'Accuracy': acuracia_v2}

# Add the dict to the dataframe
df_modelos = df_modelos.append(dict_modelo_v2, ignore_index = True)
display(df_modelos)

"""
=============
MODEL 3: KNN
=============
"""

# Let's now try a simpler algorithm, KNN. For this algorithm, we first need
# define the value of K, which is the number of nearest neighbors.
# List of possible values of K
vizinhos = list(range(1, 20, 2))

# List for scores
cv_scores = []

# Cross-validation to determine the best value of k
for k in vizinhos:
    knn = KNeighborsClassifier(n_neighbors = k)
    scores = cross_val_score(knn, X_treino, y_treino, cv = 5, scoring = 'accuracy')
    cv_scores.append(scores.mean())   

# Adjusting the sort error
erro = [1 - x for x in cv_scores]

# Determining the best value of k (with the smallest error)
optimal_k = vizinhos[erro.index(min(erro))]
print('The ideal value of k is %d' % optimal_k)

# We create the model version 3
modelo_v3 = KNeighborsClassifier(n_neighbors = optimal_k)

# Training
modelo_v3.fit(X_treino, y_treino)

# Forecasts
y_pred_v3 = modelo_v3.predict(X_teste)

# Confusion Matrix
confusion_matrix(y_teste, y_pred_v3)

# Positive class probability prediction
y_pred_proba_v3 = modelo_v3.predict_proba(X_teste)[:, 1]

# Calculate ROC_AUC test
roc_auc_v3 = roc_auc_score(y_teste, y_pred_v3)
print(roc_auc_v3)

# Calculate ROC curve
fpr_v3, tpr_v3, thresholds = roc_curve(y_teste, y_pred_proba_v3)

# Calculate AUC on test
auc_v3 = auc(fpr_v3, tpr_v3)
print(auc_v3)

# Calculate Accuracy
acuracia_v3 = accuracy_score(y_teste, y_pred_v3)
print(acuracia_v3)

# Note: With the KNN algorithm we do not extract the most important variables, because the concept of the algorithm is different.
# Save the model to disk
with open('modelos/modelo_v3.pkl', 'wb') as pickle_file:
      joblib.dump(modelo_v3, 'modelos/modelo_v3.pkl')

# Dictionary with model_v3 metrics
dict_modelo_v3 = {'Name': 'model_v3', 'Algorithm': 'KNN', 'ROC_AUC Score': roc_auc_v3,
'AUC Score': auc_v3, 'Accuracy': acuracia_v3}

# Add the dict to the dataframe
df_modelos = df_modelos.append(dict_modelo_v3, ignore_index = True)
display(df_modelos)

"""
=======================
MODEL 4: DECISION TREE
=======================
"""

# In version 4 of the model we will use a decision tree model.
# hyperparameters
tuned_params_v4 = {'min_samples_split': [2, 3, 4, 5, 7], 'min_samples_leaf': [1, 2, 3, 4, 6],
'max_depth': [2, 3, 4, 5, 6, 7]}

# Create the model with RandomizedSearchCV
modelo_v4 = RandomizedSearchCV(DecisionTreeClassifier(), tuned_params_v4, n_iter = 15, scoring = 'roc_auc', n_jobs = -1)

# Training
modelo_v4.fit(X_treino, y_treino)

# Best Model
print(modelo_v4.best_estimator_)

# Class Predictions
y_pred_v4 = modelo_v4.predict(X_teste)

# Probability Predictions
y_pred_proba_v4 = modelo_v4.predict_proba(X_teste)[:,1]

# confusion Matrix
confusion_matrix(y_teste, y_pred_v4)

# Calculate ROC AUC score
roc_auc_v4 = roc_auc_score(y_teste, y_pred_v4)
print(roc_auc_v4)

# ROC curve
fpr_v4, tpr_v4, thresholds = roc_curve(y_teste, y_pred_proba_v4)

# Calculate AUC
auc_v4 = auc(fpr_v4, tpr_v4)
print(auc_v4)

# Calculate Accuracy
acuracia_v4 = accuracy_score(y_teste, y_pred_v4)
print(acuracia_v4)

# Feature Importance
# Recreating the model
modelo_v4 = DecisionTreeClassifier(min_samples_split = 2, min_samples_leaf = 6, max_depth = 4)
modelo_v4.fit(X_treino, y_treino)

# Most important variables
indices = np.argsort(-modelo_v4.feature_importances_)
print("Most important variables for the v4_model result:")
print(50*'-')
for feature in X.columns[indices]:
    print(feature)

# Save the model to disk
with open('modelos/modelo_v4.pkl', 'wb') as pickle_file:
      joblib.dump(modelo_v4, 'modelos/modelo_v4.pkl') 

# Dictionary with model_v4 metrics
dict_modelo_v4 = {'Name': 'model_v4', 'Algorithm': 'Decision Tree', 'ROC_AUC Score': roc_auc_v4, 'AUC Score': auc_v4,
'Accuracy': acuracia_v4}

# Add the dict to the dataframe
df_modelos = df_modelos.append(dict_modelo_v4, ignore_index = True)
display(df_modelos)

"""
=============
MODEL 5: SVM
=============
"""

# For the fifth and final version of the model we will use SVM.
# Function to select hyperparameters
def svc_param_selection(X, y, nfolds):
    Cs = [0.001, 0.01, 0.1, 1, 10]
    gammas = [0.001, 0.01, 0.1, 1]
    param_grid = {'C': Cs, 'gamma' : gammas}
    grid_search = GridSearchCV(SVC(kernel = 'rbf'), param_grid, cv = nfolds)
    grid_search.fit(X_treino, y_treino)
    grid_search.best_params_
    return grid_search.best_params_

# Apply the function
svc_param_selection(X_treino, y_treino, 5)

# Create the model with the best hyperparameters
modelo_v5 = SVC(C = 1, gamma = 1, probability = True)

# Training
modelo_v5.fit(X_treino, y_treino)

# Class predictions
y_pred_v5 = modelo_v5.predict(X_teste)
confusion_matrix(y_teste, y_pred_v5)

# Probability predictions
y_pred_proba_v5 = modelo_v5.predict_proba(X_teste)[:, 1]

# Calculate ROC AUC score
roc_auc_v5 = roc_auc_score(y_teste, y_pred_v5)
print(roc_auc_v5)

# Calculate ROC curve
fpr_v5, tpr_v5, thresholds = roc_curve(y_teste, y_pred_proba_v5)

# Calculate AUC score
auc_v5 = auc(fpr_v5, tpr_v5)
print(auc_v5)

# Calculate Accuracy
acuracia_v5 = accuracy_score(y_teste, y_pred_v5)
print(acuracia_v5)

# Save the model to disk
with open('modelos/modelo_v5.pkl', 'wb') as pickle_file:
      joblib.dump(modelo_v5, 'modelos/modelo_v5.pkl') 

# Dictionary with model_v5 metrics
dict_modelo_v5 = {'Name': 'model_v5', 'Algorithm': 'SVM', 'ROC_AUC Score': roc_auc_v5,
'AUC Score': auc_v5,'Accuracy': acuracia_v5}

# Add the dict to the dataframe
df_modelos = df_modelos.append(dict_modelo_v5, ignore_index = True)
display(df_modelos)

# Selection of the Best Model
# We will use the model that had the highest AUC Score, as it is a global metric
# The AUC score is ideal for comparing models of different algorithms
df_melhor_modelo = df_modelos[df_modelos['AUC Score'] == df_modelos['AUC Score'].max()]

# Predictions with the Best Trained Model
# Get the name of the best model
modelo = df_melhor_modelo.Nome.to_string(index = False)

# Load the best model from disk
melhor_modelo = joblib.load('models/' + modelo + '.pkl')

# Raw data of a new patient
# The number of columns must be the same as used in training
novo_paciente = [72, 1, 0.8, 186, 15, 29, 7.1, 3.4, 0.97]

# Convert object to array
arr_paciente = np.array(novo_paciente)

# We use training mean and deviation to standardize new data
arr_paciente = (arr_paciente - treino_mean) / treino_std

# Convert object to array
arr_paciente = np.array(arr_paciente)

# Standardized patient data (exactly how the model expects to receive the data)
print(arr_paciente)

# Class predictions
pred_novo_paciente = melhor_modelo.predict(arr_paciente.reshape(1, -1))

# Check the value and print the final result
if pred_novo_paciente == 1:
    print('This patient must have liver disease!')
else:
    print('This patient must not have liver disease!')
