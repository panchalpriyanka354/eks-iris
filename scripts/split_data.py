# scripts/split_data.py
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the Iris dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Split the data into training and testing datasets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Save the datasets as CSV files
train_data.to_csv('./data/iris_train.csv', index=False)
test_data.to_csv('./data/iris_test.csv', index=False)
