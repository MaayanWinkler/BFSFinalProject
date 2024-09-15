import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, median_absolute_error
from sklearn.utils import resample
from sklearn.model_selection import cross_val_score
import joblib

# Load the dataset
train_data = pd.read_csv('forecasting_data_training.csv', header=0)

# Define features and target variable
features = ['Temperature', 'Humidity', 'Larvae_weight', 'Num_of_pupae', 'Substratebefordrying', 'Substrateafterdrying']
target = 'Pupation_Percentage_for_Day_14'

# Convert all data to numeric and handle errors
train_data[features] = train_data[features].apply(pd.to_numeric, errors='coerce')

# Fill any NaN values
train_data.fillna(train_data.mean(), inplace=True)

# Handle small values in the target variable
epsilon = 1  # A small constant to replace values less than this threshold
train_data[target] = train_data[target].apply(lambda x: x if x > epsilon else epsilon)

# Data Augmentation using Bootstrapping
augmented_data = resample(train_data, replace=True, n_samples=2000, random_state=42)

# Prepare features and target for training
X_augmented = augmented_data[features]
y_augmented = augmented_data[target]

# Initialize the Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10, min_samples_split=10)

# Train the Random Forest model
rf_model.fit(X_augmented, y_augmented)

# Cross-validated scores to evaluate the model
cv_scores = cross_val_score(rf_model, X_augmented, y_augmented, cv=5, scoring='neg_mean_squared_error')
mse_cv = -cv_scores.mean()

# Predict using the trained model
y_pred = rf_model.predict(X_augmented)

# Calculate Evaluation Metrics
mae = mean_absolute_error(y_augmented, y_pred)
mse = mean_squared_error(y_augmented, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_augmented, y_pred)
adj_r2 = 1 - (1 - r2) * (len(y_augmented) - 1) / (len(y_augmented) - X_augmented.shape[1] - 1)
smape = 100 * np.mean(2 * np.abs(y_augmented - y_pred) / (np.abs(y_augmented) + np.abs(y_pred)))
med_ae = median_absolute_error(y_augmented, y_pred)

# Print all scores
print(f"Cross-Validated Mean Squared Error: {mse_cv:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²): {r2:.2f}")
print(f"Adjusted R-squared: {adj_r2:.2f}")
print(f"Symmetric Mean Absolute Percentage Error (SMAPE): {smape:.2f}%")
print(f"Median Absolute Error: {med_ae:.2f}")

# Save the trained Random Forest model to a file
joblib.dump(rf_model, 'random_forest_model.pkl')
