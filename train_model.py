from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import mlflow
import mlflow.sklearn
from data_loader import fetch_data

df=fetch_data()
if df.empty:
    raise Exception("No data found in MongoDB!")

x=df.drop(columns=['monthly_charge','customer_id'])
y=df['monthly_charge']

print(x)
print(y)