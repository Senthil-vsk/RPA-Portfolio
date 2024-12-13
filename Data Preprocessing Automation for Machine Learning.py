import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(data):
    # Handling missing values
    data = data.fillna(data.mean())
    
    # Encoding categorical variables
    le = LabelEncoder()
    data['Category'] = le.fit_transform(data['Category'])
    
    # Scaling numerical features
    scaler = StandardScaler()
    data[['Price', 'Quantity']] = scaler.fit_transform(data[['Price', 'Quantity']])
    
    return data

# Usage example
df = pd.read_csv('product_data.csv')
processed_df = preprocess_data(df)
print(processed_df.head())
