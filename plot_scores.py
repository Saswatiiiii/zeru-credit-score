import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("wallet_scores.csv")

plt.figure(figsize=(10, 6))
sns.histplot(df["credit_score"], bins=20, kde=True)
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.show()
