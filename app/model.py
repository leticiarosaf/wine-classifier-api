import joblib
import os

# Saved model path
model_path = os.path.join(os.path.dirname(__file__), 'wine_model.pkl')

# Load model
model = joblib.load(model_path)

# Função para fazer a predição
def predict(data):
    return model.predict([data])