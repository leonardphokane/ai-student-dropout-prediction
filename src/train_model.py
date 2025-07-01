import joblib
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train, output_path="model/random_forest_dropout_predictor.pkl"):
    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    rf.fit(X_train, y_train)
    joblib.dump(rf, output_path)
    return rf
