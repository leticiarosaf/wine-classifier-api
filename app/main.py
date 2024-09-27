from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI()

# Rota de verificação de saúde
@app.get("/api/health")
def health():
    return {"status": "Estou saudável"}

# Definir as features do modelo
class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

# Rota de predição
@app.post("/api/predict")
def predict_wine(features: WineFeatures):
    data = [features.alcohol, features.malic_acid, features.ash, features.alcalinity_of_ash,
            features.magnesium, features.total_phenols, features.flavanoids, features.nonflavanoid_phenols,
            features.proanthocyanins, features.color_intensity, features.hue,
            features.od280_od315_of_diluted_wines, features.proline]
    prediction = predict(data)
    return {"prediction": int(prediction[0])}