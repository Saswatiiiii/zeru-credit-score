import pandas as pd

def extract_features(df):
    features = df.groupby("userWallet")["action"].value_counts().unstack().fillna(0)
    features["total_txn"] = features.sum(axis=1)

    if "repay" in features and "borrow" in features:
        features["repay_borrow_ratio"] = features["repay"] / (features["borrow"] + 1)
    
    if "redeemunderlying" in features and "deposit" in features:
        features["redeem_deposit_ratio"] = features["redeemunderlying"] / (features["deposit"] + 1)

    for col in ["deposit", "borrow", "repay", "redeemunderlying", "liquidationcall"]:
        if col not in features:
            features[col] = 0

    return features.reset_index()
