import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load the data with the specified path
dados = pd.read_csv('/Users/lucashomuniz/Library/Mobile Documents/com~apple~CloudDocs/Archives/work_files/work_projects/mondelez_international/PROJECT_UAT/dataset_project_06.csv')

# Handle missing values in Albumin_and_Globulin_Ratio by filling with the mean
dados['Albumin_and_Globulin_Ratio'] = pd.to_numeric(dados['Albumin_and_Globulin_Ratio'], errors='coerce')
dados['Albumin_and_Globulin_Ratio'].fillna(dados['Albumin_and_Globulin_Ratio'].mean(), inplace=True)

# Encode Gender to numeric (0 for Female, 1 for Male)
le = LabelEncoder()
dados['Gender'] = le.fit_transform(dados['Gender'])

# Convert Dataset to a continuous target (1.0 for disease, 0.0 for no disease)
dados['Dataset'] = dados['Dataset'].map({1: 1.0, 2: 0.0})

# Define features and target
X = dados.drop('Dataset', axis=1)
y = dados['Dataset']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1234)

# Initialize a dictionary to store results and predictions
results = {}
predictions = {}

# Model 1: Gradient Boosting Machine (GBM)
gbm = GradientBoostingRegressor(random_state=1234)
gbm.fit(X_train, y_train)
y_pred_gbm = gbm.predict(X_test)
results['GBM'] = {
    'MAE': mean_absolute_error(y_test, y_pred_gbm),
    'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_gbm)),
    'R2': r2_score(y_test, y_pred_gbm)
}
predictions['GBM'] = y_pred_gbm

# Model 2: K-Nearest Neighbors (KNN)
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
results['KNN'] = {
    'MAE': mean_absolute_error(y_test, y_pred_knn),
    'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_knn)),
    'R2': r2_score(y_test, y_pred_knn)
}
predictions['KNN'] = y_pred_knn

# Model 3: Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
results['LINEAR REGRESSION'] = {
    'MAE': mean_absolute_error(y_test, y_pred_lr),
    'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_lr)),
    'R2': r2_score(y_test, y_pred_lr)
}
predictions['LINEAR REGRESSION'] = y_pred_lr

# Model 4: Elastic Net
en = ElasticNet(random_state=1234)
en.fit(X_train, y_train)
y_pred_en = en.predict(X_test)
results['ELASTIC NET'] = {
    'MAE': mean_absolute_error(y_test, y_pred_en),
    'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_en)),
    'R2': r2_score(y_test, y_pred_en)
}
predictions['ELASTIC NET'] = y_pred_en

# Model 5: Random Forest
rf = RandomForestRegressor(random_state=1234)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
results['RANDOM FOREST'] = {
    'MAE': mean_absolute_error(y_test, y_pred_rf),
    'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_rf)),
    'R2': r2_score(y_test, y_pred_rf)
}
predictions['RANDOM FOREST'] = y_pred_rf

# Create a DataFrame from the results
df_results = pd.DataFrame(results).T.reset_index()
df_results.columns = ['MODEL', 'MAE', 'RMSE', 'R2']

# Round the values to 5 decimal places
df_results['MAE'] = df_results['MAE'].round(5)
df_results['RMSE'] = df_results['RMSE'].round(5)
df_results['R2'] = df_results['R2'].round(5)

# Display the table
print("Results Table:")
print(df_results.to_string(index=False))

# Scatter Plot for Predicted vs Actual Values
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Predicted vs Actual Values for Each Model', fontsize=16)

for ax, (model, preds) in zip(axes.flatten(), predictions.items()):
    ax.scatter(y_test, preds, alpha=0.5)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)  # Diagonal line for perfect prediction
    ax.set_title(f'{model}')
    ax.set_xlabel('Actual Values')
    ax.set_ylabel('Predicted Values')
    ax.grid(True)

# Remove the empty subplot (if any)
if len(predictions) < 6:
    axes.flatten()[-1].remove()

plt.tight_layout()
plt.show()