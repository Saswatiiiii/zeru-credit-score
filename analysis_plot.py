import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load scores
df = pd.read_csv("wallet_scores.csv")

# Define bins and labels
bins = [0, 100, 200, 300, 400, 500]
labels = ['0-100', '100-200', '200-300', '300-400', '400-500']
df['score_range'] = pd.cut(df['credit_score'], bins=bins, labels=labels, right=True)

# Plot distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='score_range', data=df, palette='viridis')
plt.title('Wallet Credit Score Distribution')
plt.xlabel('Score Range')
plt.ylabel('Number of Wallets')
plt.tight_layout()
plt.savefig('score_distribution.png')
plt.show()
