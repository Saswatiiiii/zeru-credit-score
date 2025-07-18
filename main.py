import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from feature_engineering import extract_features
from model import load_model

def score_wallets(json_path):
    df = pd.read_json(json_path)
    features = extract_features(df)

    wallet_ids = features["userWallet"]
    X = features.drop("userWallet", axis=1)

    model, scaler = load_model()
    X_scaled = scaler.transform(X)
    scores = model.predict(X_scaled)

    result = pd.DataFrame({"walletAddress": wallet_ids, "credit_score": scores})
    result["credit_score"] = result["credit_score"].clip(0, 1000)
    result.to_csv("wallet_scores.csv", index=False)

    return result

def plot_credit_score_distribution(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(df["credit_score"], bins=30, kde=True, color="skyblue")
    plt.title("Credit Score Distribution of Wallets", fontsize=16)
    plt.xlabel("Credit Score")
    plt.ylabel("Number of Wallets")
    plt.tight_layout()
    plt.savefig("credit_score_distribution.png")
    plt.show()

if __name__ == "__main__":
    result = score_wallets("data/user_transactions.json")
    print(result.head())
    plot_credit_score_distribution(result)
