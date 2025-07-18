import pandas as pd
from feature_engineering import extract_features
from model import train_model

# Load and inspect JSON
df = pd.read_json("data/user_transactions.json")

# Check the structure (optional)
print(df.columns)
print(df.head())

features = extract_features(df)
features["credit_score"] = (features["repay_borrow_ratio"] * 600 +
                            features["redeem_deposit_ratio"] * 300 +
                            features["total_txn"] * 0.5)
features["credit_score"] = features["credit_score"].fillna(0).clip(0, 1000)

X = features.drop(["userWallet", "credit_score"], axis=1)
y = features["credit_score"]

train_model(X, y)
print("Model trained and saved!")
