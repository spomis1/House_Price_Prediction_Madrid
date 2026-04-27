import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from xgboost import XGBRegressor
import joblib

# ── Carga ────────────────────────────────────────────────────────────────────
df = pd.read_csv("../Data/Processed/madrid.csv")

# Orden de features compartido por ambos modelos
FEATURES = ['Latitud', 'Precio_Medio_cp', 'Superficie_m2', 'Habitaciones',
            'Baños', 'Ascensor', 'Parking', 'Balcon', 'Aire_Acondicionado',
            'Calefaccion', 'Piscina', 'Terraza']

X = df[FEATURES]
y = df['Precio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ── Random Forest ─────────────────────────────────────────────────────────────
# Mejor modelo en precisión global según comparación en notebook 02
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
print(f"[RF]  R²: {r2_score(y_test, y_pred_rf):.4f}  MAE: €{mean_absolute_error(y_test, y_pred_rf):,.0f}")

# ── XGBoost con restricciones de monotonicidad ────────────────────────────────
# Precio_Medio_cp (idx 1) y Superficie_m2 (idx 2) son monotónicamente crecientes.
# Dejar el resto sin restricción permite al modelo mayor flexibilidad y mejor R².
# Esto garantiza que más m² y mejor zona siempre impliquen mayor precio.
#
# Constraints por feature:
# Latitud=0, Precio_Medio_cp=1, Superficie_m2=1, Habitaciones=0,
# Baños=0, Ascensor=0, Parking=0, Balcon=0, AC=0, Calefaccion=0, Piscina=0, Terraza=0
MONOTONE_CONSTRAINTS = (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

xgb = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    min_child_weight=3,
    monotone_constraints=MONOTONE_CONSTRAINTS,
    random_state=42,
    n_jobs=-1,
)
xgb.fit(X_train, y_train)

y_pred_xgb = xgb.predict(X_test)
print(f"[XGB] R²: {r2_score(y_test, y_pred_xgb):.4f}  MAE: €{mean_absolute_error(y_test, y_pred_xgb):,.0f}")

# ── Guardado ──────────────────────────────────────────────────────────────────
_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(_dir, "..", "Models")

joblib.dump(rf,  os.path.join(models_dir, "Rf.joblib"))
joblib.dump(xgb, os.path.join(models_dir, "Xgb.joblib"))
print("Modelos guardados en Models/")
