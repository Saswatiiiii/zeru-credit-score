from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(X, y):
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)

    joblib.dump(model, "credit_model.pkl")
    joblib.dump(scaler, "scaler.pkl")

def load_model():
    model = joblib.load("credit_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler
