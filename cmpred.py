import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load your dataset (replace with your actual dataset path)
data = pd.read_csv("open_shopping_data.csv")

# Preprocess the data: Ensure 'price' and 'item_type' are present
data = data.dropna(subset=['price', 'item_type'])

# Convert item_type into a numerical value (e.g., one-hot encoding or label encoding)
data = pd.get_dummies(data, columns=['item_type'])

# Split into features (X) and target (y)
X = data.drop(columns=['price'])
y = data['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Predicting the average price for a new item (example)
new_item = np.array([[1, 0, 0, 0, 0]])  # Replace with actual item features
predicted_price = model.predict(new_item)
print(f"Predicted Price: {predicted_price[0]}")
