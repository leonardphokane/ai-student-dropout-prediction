import pandas as pd
import joblib
import argparse
from sklearn.preprocessing import StandardScaler

def preprocess_input(data_dict):
    # Convert dictionary to DataFrame
    df = pd.DataFrame([data_dict])

    # One-hot encoding for categorical columns
    df['language_English'] = 1 if data_dict['language'] == 'English' else 0
    df['language_French'] = 1 if data_dict['language'] == 'French' else 0
    df['location_Rural'] = 1 if data_dict['location'] == 'Rural' else 0
    df['location_Suburban'] = 1 if data_dict['location'] == 'Suburban' else 0
    df['location_Urban'] = 1 if data_dict['location'] == 'Urban' else 0

    # Drop original categorical columns
    df = df.drop(columns=['language', 'location'])

    # Normalize numeric columns
    scaler = StandardScaler()
    df[['time_spent', 'quiz_score']] = scaler.fit_transform(df[['time_spent', 'quiz_score']])

    return df

def predict_dropout(student_profile):
    df = preprocess_input(student_profile)

    model = joblib.load("random_forest_dropout_predictor.pkl")







    prediction = model.predict(df)[0]

    return "Dropped Out" if prediction == 1 else "Continued"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict if a student is at risk of dropping out.")
    parser.add_argument("--gender", type=str, required=True)
    parser.add_argument("--age", type=int, required=True)
    parser.add_argument("--language", type=str, choices=["English", "French"], required=True)
    parser.add_argument("--location", type=str, choices=["Urban", "Suburban", "Rural"], required=True)
    parser.add_argument("--time_spent", type=float, required=True)
    parser.add_argument("--quiz_score", type=float, required=True)
    parser.add_argument("--login_count", type=int, required=True)

    args = parser.parse_args()

    student = {
        "gender": args.gender,
        "age": args.age,
        "language": args.language,
        "location": args.location,
        "time_spent": args.time_spent,
        "quiz_score": args.quiz_score,
        "login_count": args.login_count,
    }

    result = predict_dropout(student)
    print("🔮 Prediction:", result)
