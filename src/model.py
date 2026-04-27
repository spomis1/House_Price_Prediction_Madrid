import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# ── Carga ────────────────────────────────────────────────────────────────────
df = pd.read_csv("../Data/Processed/madrid.csv")

X = df.drop(columns=["Precio"])
y = df["Precio"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ── Entrenamiento ─────────────────────────────────────────────────────────────
# RandomForestRegressor con parámetros por defecto resultó ser el mejor modelo
# según la comparación en notebook 02 (R²=0.892, MAE=€82.128)
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)

# ── Evaluación ────────────────────────────────────────────────────────────────
y_pred = rf.predict(X_test)
print(f"R²:  {r2_score(y_test, y_pred):.4f}")
print(f"MAE: €{mean_absolute_error(y_test, y_pred):,.0f}")

# ── Guardado ──────────────────────────────────────────────────────────────────
_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(_dir, "..", "Models", "Rf.joblib")
joblib.dump(rf, output_path)
print(f"Modelo guardado en: {output_path}")
