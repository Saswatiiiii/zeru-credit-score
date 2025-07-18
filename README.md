# README.md

# Zeru Credit Score Assignment

##  Problem Statement

Given raw transaction data of blockchain wallets, the goal is to assign a **credit score** (0–1000) to each wallet based on its transaction behavior. This helps identify the trustworthiness or risk associated with different wallets.

##  Dataset

The input dataset is a JSON file containing user wallet transactions. Each transaction includes:

- `walletAddress`
- `action` (e.g., deposit, borrow, repay, redeemunderlying, liquidationcall)

##  Approach

### Feature Engineering

We extracted the following features from the transaction history:

- Total number of each action per wallet
- `repay_borrow_ratio = repay / (borrow + 1)`
- `redeem_deposit_ratio = redeemunderlying / (deposit + 1)`
- `total_txn` = sum of all actions

### Model

We used a **Random Forest Regressor** to predict credit scores.

- Input features were scaled using `MinMaxScaler`.
- The model was trained on a manually generated score (e.g., sum of weights for different actions).

##  Project Architecture

```
data/user_transactions.json
          ↓
  Feature Engineering
          ↓
     Model Training
          ↓
  Score Generation
          ↓
wallet_scores.csv + Plot
```

##  How to Run

1. Place your dataset in the `data/` folder (e.g., `user_transactions.json`).
2. Run `train.py` to train and save the model:
   ```bash
   python train.py
   ```
3. Run `main.py` to score wallets:
   ```bash
   python main.py
   ```
   This generates:
   - `wallet_scores.csv` (wallets and their scores)
   - `score_distribution.png` (score histogram)

##  Files Included

| File                     | Description                              |
| ------------------------ | ---------------------------------------- |
| `feature_engineering.py` | Extracts features from raw data          |
| `model.py`               | Trains and loads the Random Forest model |
| `main.py`                | Scores wallets using the trained model   |
| `train.py`               | Generates mock credit scores and trains  |
| `wallet_scores.csv`      | Output credit scores                     |
| `score_distribution.png` | Plot of credit score distribution        |
| `analysis.md`            | Credit behavior analysis based on scores |

##  Requirements

Install the following libraries before running the code:

```bash
pip install pandas scikit-learn matplotlib seaborn joblib
```

##  Author

Saswati Chatterjee
[saswatic006@gmail.com]